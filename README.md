# Final project explanation
## Leap Motion controller & unity 
in order to run this part of the project you do need:
1. leap motion controler
2. unity on your pc.  
in the folder "unity project/My project" is the intier unity project.
1. download the mentioned folder from the reposetory
2. open unity and open the folder caled "My project"
3. connect the leap motion controler
4. run the unity project
Noat: you may need to download the SDk for the leap see here[https://leap2.ultraleap.com/downloads/leap-motion-controller-2/]


## Algorithms / analyzing data
in the folder "algo code" there are 6 files:
* CCA_final.py - algorithem file.
* CroosCorrelation_final.py - algorithem file.
* DWT_final.py - algorithem file.
* Wavlet_final.py - algorithem file.
* split_left_right.py - takes the data file that represent two hand movments and splits it to right hand and left hand data files.
* main.py - this is the file to run the code.

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

