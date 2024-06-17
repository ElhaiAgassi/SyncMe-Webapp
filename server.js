// File: server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);

// Setup CORS and Socket.IO
const io = socketIo(server, {
    cors: {
        origin: "https://powerful-caverns-44451-c8d559731987.herokuapp.com/",
        methods: ["GET", "POST"]
    }
});

// Serve static files from the root directory
app.use(express.static(path.join(__dirname, '.')));

io.on('connection', socket => {
    console.log('New user connected');

    socket.on('offer', (data) => {
        socket.broadcast.emit('offer', data);
    });

    socket.on('answer', (data) => {
        socket.broadcast.emit('answer', data);
    });

    socket.on('ice-candidate', (data) => {
        socket.broadcast.emit('ice-candidate', data);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

// Use server.listen NOT app.listen
const PORT = process.env.PORT || 3000; // Fallback to 3000 if PORT is not set
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
