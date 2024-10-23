# Final project explanation
## Leap Motion controller & unity 
### requierments
1. leap motion controler
2. unity on your pc.  
### how to run
in the folder "unity project/My project" is the intier unity project.
1. download the mentioned folder from the reposetory
2. open unity and open the folder caled "My project"
3. connect the leap motion controler
4. run the unity project
Noat: you may need to download the SDk for the leap see [here](https://leap2.ultraleap.com/downloads/leap-motion-controller-2/)

there are 4 scripts to this project they are alsow presented seperatly in the folder "unity code" if you wish to vreat your own unity project.
* ExtractData.cs - this file will record the hand movment detected by the Leap use "R" to start recording "S" to stop and "T" for a set recording of 15 seconds. this will give you a json file caled "output.json"
* Handdata.cs - this file showes the classes created to save the data in an orderly fashon.
* HandDisplay.cs this can take the file from "ExtractData.cs" and show the recorded hands however in this code you do need to manualy change the path to the created file in the code (line 17)!!
* SwitcHands - there are differand hand displays that are bilt in the Leap api this lest you change thrue them using numbers 0-6

## Algorithms / analyzing data
after runing the unity project and recording hand movments you can run the algorithems on the output file created.
1. downlad the files from this reposetory.
2. creat a python envierment and add the files
3. in main.py change the "hand_recordings" variable to the path of your output file and run main.
   
### file explanation
* CCA_final.py - algorithem file.
* CroosCorrelation_final.py - algorithem file.
* DWT_final.py - algorithem file.
* Wavlet_final.py - algorithem file.
* split_left_right.py - takes the data file that represent two hand movments and splits it to right hand and left hand data files.
* main.py - this is the file to run the code.

Noat:
1. when running main you will get a print of each algorithem analyzing the file each algorithem uses differant feachers to determin if the hands are synced or not what you get is raw data. to determin an accuret synchronisation persentage you may give each feacher and algorithem its respective weight and calculate it yourself
2. the wavelet algorithem is commented and is set not to run as it did not preduce and relevent results
3. remember manual changes may be needed for the input file path.

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

