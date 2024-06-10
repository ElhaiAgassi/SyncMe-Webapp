// File: server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from the 'public' directory
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

const PORT = process.env.PORT || 3000;  // Use Heroku's port or 3000 if there's nothing set
server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});
