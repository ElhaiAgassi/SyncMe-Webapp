# Final Project Explanation
## Leap Motion Controller & Unity 
### Requirements
1. Leap Motion Controller
2. Unity installed on your PC.  
### How to Run
In the folder "unity project/My project" is the entire Unity project.
1. Download the mentioned folder from the repository.
2. Open Unity and open the folder called "My project."
3. Connect the Leap Motion Controller.
4. Run the Unity project.

Note: You may need to download the SDK for the Leap Motion. See [here](https://leap2.ultraleap.com/downloads/leap-motion-controller-2/).

There are 4 scripts in this project. They are also presented separately in the folder "unity code" if you wish to create your own Unity project.
* `ExtractData.cs` - This file will record the hand movement detected by the Leap. Use "R" to start recording, "S" to stop, and "T" for a set recording of 15 seconds. This will give you a JSON file called `output.json`.
* `Handdata.cs` - This file shows the classes created to save the data in an orderly fashion.
* `HandDisplay.cs` - This can take the file from `ExtractData.cs` and show the recorded hands. However, in this code, you do need to manually change the path to the created file in the code (line 17)!
* `SwitchHands.cs` - There are different hand displays built into the Leap API. This lets you switch through them using numbers 0-6.

## Algorithms / Analyzing Data
After running the Unity project and recording hand movements, you can run the algorithms on the output file created.
1. Download the files from this repository.
2. Create a Python environment and add the files.
3. In `main.py`, change the `hand_recordings` variable to the path of your output file and run `main.py`.

### File Explanation
* `CCA_final.py` - Algorithm file.
* `CrossCorrelation_final.py` - Algorithm file.
* `DWT_final.py` - Algorithm file.
* `Wavelet_final.py` - Algorithm file.
* `split_left_right.py` - Takes the data file that represents two hand movements and splits it into right-hand and left-hand data files.
* `main.py` - This is the file to run the code.

Note:
1. When running `main.py`, you will get a printout of each algorithm analyzing the file. Each algorithm uses different features to determine if the hands are synced or not. What you get is raw data. To determine an accurate synchronization percentage, you may give each feature and algorithm its respective weight and calculate it yourself.
2. The Wavelet algorithm is commented out and is set not to run as it did not produce any relevant results.
3. Remember, manual changes may be needed for the input file path.


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

