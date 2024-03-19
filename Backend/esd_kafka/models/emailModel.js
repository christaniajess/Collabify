const formData = require('form-data');
const Mailgun = require('mailgun.js');
const mailgun = new Mailgun(formData);
const mg = mailgun.client({username: 'b02bcf9f-d6c98002', key: '05bc8f30070e21bc684a40c3e143e144-b02bcf9f-d6c98002'});

const sendMail = (req, res, recipients, subject, text) => {
	mg.messages.create('sandbox5314bb250fea415fbc2913ee0060a1f5.mailgun.org', {
		from: "Collabify <mailgun@sandbox-123.mailgun.org>",
		to: recipients,
		subject: subject,
		text: text
	})
	.then(msg => console.log(msg)) // logs response data
	.catch(err => console.log(err)); // logs any error
}

module.exports = { sendMail }
