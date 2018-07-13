const debug = require('debug')('app:adminRoutes');
const express = require('express');
const { MongoClient } = require('mongodb');

const adminRouter = express.Router();

const books = [
  {
    title: 'Python Cookbook',
    genre: 'Programming',
    author: 'David Beazley',
    read: false,
  },
  {
    title: 'Discrete Mathematics and its Applications',
    genre: 'Computer Science',
    author: 'Kenneth Rosen',
    read: false,
  },
  {
    title: 'Python Fluente',
    genre: 'Programming',
    author: 'Luciano Ramalho',
    read: true,
  },
  {
    title: 'Physics Tips',
    genre: 'Physics',
    author: 'Richard P. Feynman',
    read: false,
  },
];

function router(nav) {
  adminRouter.route('/')
    .get((req, res) => {
      const url = 'mongodb://localhost:27017/';
      const dbName = 'libraryApp';

      (async function mongo() {
        let client;

        try {
          client = await MongoClient.connect(url);
          debug('Connected to the server');

          const db = client.db(dbName);
          const response = await db.collection('books').insertMany(books);
          res.json(response);
        } catch (error) {
          debug(error.stack);
        }

        client.close();
      }());
    });
  return adminRouter;
}

module.exports = router;
