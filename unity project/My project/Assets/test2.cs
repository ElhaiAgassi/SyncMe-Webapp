// //author: zeev fischer 

// using System.Collections;
// using System.Collections.Generic;
// using UnityEngine;
// using UnityEngine.UI;
// using System.IO;
// using Leap;
// using Leap.Unity;
// // using UnityEngine;

// public class HandTrackingToCSV : MonoBehaviour
// {
//     // the device itself
//     public LeapProvider leapProvider;
//     // public Transform handTransform;
//     //data list to be saved
//     private List<string> hand_location = new List<string>();
    
//     // Start is called before the first frame update
//     private void Start()
//     {
//         string csvLine = $"{"frame id"}, {"hand"}, {"time"}, {"X"}, {"Y"}, {"Z"}";
//         hand_location.Add(csvLine);
//     }
//     // Update is called once per frame
//     private void Update()
//     {
//         //for each frame all hands location
//         for (int i = 0; i < leapProvider.CurrentFrame.Hands.Count; i++)
//         {
//             //get all hands 
//             Hand _hand = leapProvider.CurrentFrame.Hands[i];
//             // convert to vector 
//             Vector3 handPosition = _hand.PalmPosition;
//             // Format the hand data as a CSV line
//             string csvLine = $"{leapProvider.CurrentFrame.Id}, {Time.time}, {i}, {handPosition.x}, {handPosition.y}, {handPosition.z}";
//             // add to list
//             hand_location.Add(csvLine);
//         }
//     }
//     private void OnApplicationQuit()
//     {
//         // Save the collected hand data to a CSV file
//         string filePath = "hand_tracking_data.csv";
//         File.WriteAllLines(filePath, hand_location.ToArray());
//     }
// }