# Final project explanation
## Algorithms
in the folder "algo code" there are 6 files
fore algorithem file:
* CCA_final.py
* CroosCorrelation_final.py

## Leap Motion controller & unity 

## Video Conference with Hand Tracking

This project is a video conferencing application with hand tracking capabilities using MediaPipe. The application allows users to see hand landmarks overlaid on their video streams, both locally and remotely.

## Features

- Real-time video conferencing
- Hand tracking and landmark overlay using MediaPipe
- Data logging of hand movements to a CSV file

## Deployment

### Heroku

The application is deployed on Heroku and can be accessed at:

[https://powerful-caverns-44451-c8d559731987.herokuapp.com/](https://powerful-caverns-44451-c8d559731987.herokuapp.com/)

### Local Development

To run the application locally:

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   node server.js
   ```
4. Access the application in your browser at:
   ```
   http://localhost:3000
   ```

## Usage

1. Open the application in your browser.
2. Allow access to your camera when prompted.
3. Open the application in another browser or on another device to start a video call.
4. The application will display your video stream with hand tracking overlaid.
5. Click the "Download CSV" button to download a CSV file with hand movement data.

## Technologies Used

- Node.js
- Express
- Socket.IO
- MediaPipe

