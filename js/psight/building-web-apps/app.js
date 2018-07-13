const chalk = require('chalk');
const debug = require('debug')('app');
const express = require('express');
const morgan = require('morgan');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

app.use(morgan('tiny'));

app.use(express.static(path.join(__dirname, 'assets')));
app.use('/css', express.static(path.join(__dirname, 'node_modules', 'bootstrap', 'dist', 'css')));
app.use('/js', express.static(path.join(__dirname, 'node_modules', 'bootstrap', 'dist', 'js')));
app.use('/js', express.static(path.join(__dirname, 'node_modules', 'jquery', 'dist')));
app.use('/js', express.static(path.join(__dirname, 'node_modules', 'popper.js', 'dist')));

app.set('views', './src/views');
app.set('view engine', 'ejs');

const nav = [{
  title: 'Books',
  link: '/books',
}, {
  title: 'Authors',
  link: '/authors',
}];
const bookRouter = require('./src/routes/bookRoutes')(nav);
const adminRouter = require('./src/routes/adminRoutes')(nav);

app.use('/books', bookRouter);
app.use('/admin', adminRouter);

app.get('/', (req, res) => {
  res.render(
    'index',
    {
      title: 'Hey, there',
      nav: [{
        title: 'Books',
        link: '/books',
      }, {
        title: 'Authors',
        link: '/authors',
      }],
    },
  );
});

app.listen(port, () => {
  debug(`Listening at port ${chalk.green(port)}`);
});
