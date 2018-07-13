const debug = require('debug')('app:bookRoutes');
const express = require('express');
const {
  MongoClient, ObjectId,
} = require('mongodb');

const bookRouter = express.Router();

function router(nav) {
  bookRouter.route('/')
    .get((req, res) => {
      const url = 'mongodb://localhost:27017/';
      const dbName = 'libraryApp';

      (async function mongo() {
        let client;

        try {
          client = await MongoClient.connect(url);
          debug('Connected to the server');

          const db = client.db(dbName);
          const collection = await db.collection('books');
          const books = await collection.find().toArray();
          res.render('bookListView', {
            title: 'Hey, there',
            nav,
            books,
          });
        } catch (error) {
          debug(error.stack);
        }

        client.close();
      }());
    });

  bookRouter.route('/:id')
    .get((req, res) => {
      const url = 'mongodb://localhost:27017/';
      const dbName = 'libraryApp';

      (async function mongo() {
        let client;

        try {
          client = await MongoClient.connect(url);
          debug('Connected to the server');

          const db = client.db(dbName);
          const collection = await db.collection('books');
          const book = await collection.findOne({ _id: new ObjectId(req.params.id) });
          res.render('bookView', {
            title: 'Hey, there',
            nav,
            book,
          });
        } catch (error) {
          debug(error.stack);
        }

        client.close();
      }());
    });

  return bookRouter;
}
module.exports = router;
