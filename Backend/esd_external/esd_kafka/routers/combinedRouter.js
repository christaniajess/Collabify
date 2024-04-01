const express = require('express');
const { notify } = require('../controller/combinedController');

const router = express.Router();

router.post('/notify', notify);

module.exports = router;