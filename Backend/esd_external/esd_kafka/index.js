const express = require("express");
const http = require("http");
const cors = require("cors");

// express app
const app = express();
const PORT = 3000;

app.use(cors()); // Allows cross-origin requests

app.use(express.json());
app.use("/email", require("./routers/emailRouter"));
app.use("/notification", require("./routers/notificationRouter"));
app.use("/", require("./routers/combinedRouter"));

const server = http.createServer(app);

app.get("/", (req, res) => {
    res.status(200).json({
        message: "server running!",
    });
});

// Start the server
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
