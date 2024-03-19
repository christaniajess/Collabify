const express = require('express');
const { sendEmail } = require('../controller/emailController');

const router = express.Router();

router.post('/send', sendEmail);

module.exports = router;