var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/* POST request in the home page */
router.post('/', (req, res) => {
  res.send('Got a post request')
});

router.put('/user', (req, res) => {
  res.send('Got a put request for user')
});

router.delete('/user', (req, res) => {
  res.send('got a request to delete a user')
});

module.exports = router;
