const express = require('express');
const { email_notification } = require('../controller/emailController');

const router = express.Router();

router.post('/send', email_notification);

module.exports = router;