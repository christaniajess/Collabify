const email = require("../models/emailModel");



const sendEmail = async (req, res) => {
    const { recipients, subject, text } = req.body;
    console.log(recipients, subject, text)

    email.sendMail(req, res, recipients, subject, text);

    res.status(200).json({
        message: "Email sent!",
    });
    
}
// const getAllTasks = async (req, res) => {
//   // query db
//   const allTasks = await Tasks.find({});

//   res.status(200).json({
//     allTasks,
//   });
// };



// const createTask = async (req, res) => {
//   //create new task
//   const newTask = req.body;

//   // check if task title already exist in db
//   try {
//     const createdTask = await Tasks.create(newTask);
//     res.status(201).json(createdTask);

//   } catch (err) {
//     res.status(400).json({
//       message: err.message,
//     });
//   }

// };



// const updateTaskStatus = async (req, res) => {
//   const taskID=req.params.id;
//   const foundTask = await Tasks.find({ _id: taskID });
//   if (! foundTask) {
//     res.status(404).json({ message: "Task not found" });
//   }

//   const update={done: !foundTask.done};

//   const updatedTask= await Tasks.updateOne({_id: taskID}, update);
//   console.log(updatedTask)
//   res.status(200).json(updatedTask);
// }

module.exports = {
    sendEmail
};
