/*
this is a data extraction class
it creats the file data4.json
the data here is a json file the data corresponds to the MyBone, SerializableFinger, and PalmArm classes created in HandData.cs file
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using Leap;
using Leap.Unity;
using TMPro;
using UnityEditor;
using UnityEngine.UIElements;
using UnityEngine.Playables;
using System.Linq;
using System.Text.Json;
using Palmmedia.ReportGenerator.Core.Common;
using System;
using System.Timers;

public class ExtractData : MonoBehaviour
{
    // the device itself
    public LeapProvider leapProvider;
    string filePath = "output.json";
    // string filePath = "mirrored_data4.json";
    bool isRunning = false;
    const float timerInterval = 20f;
    bool timer_on = false;
    float timer = 0f;

    // Start is called before the first frame update
    private void Start()
    {
        // Uncomment the following lines if you want to delete the file on start
        // if (File.Exists(filePath))
        // {
        //     File.Delete(filePath);
        // }
    }
    // Update is called once per frame
    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            isRunning = true;
        }
        else if (Input.GetKeyDown(KeyCode.S))
        {
            isRunning = false;
        }
        else if (Input.GetKeyDown(KeyCode.T))
        {
            isRunning = true;
            timer_on = true;
            timer = 0f;
        }

        if (isRunning)
        {
            if (timer_on)
            {
                timer += Time.deltaTime;
                if (timer >= timerInterval)
                {
                    isRunning = false;
                    timer = 0f; // Reset timer
                }
                ExtractHandData();
            }
            else
            {
                ExtractHandData();
            }
        }
    }

    private void ExtractHandData()
    {
        // Extraction logic here

        List<string> handDataList = new List<string>();

        Frame frame = leapProvider.CurrentFrame;
        foreach (Hand hand in frame.Hands)
        {
            PalmArm palmArmData = new PalmArm
            {
                frameId = frame.Id,
                isleft = hand.IsLeft,
                PalmPosition = hand.PalmPosition,
                PalmVelocity = hand.PalmVelocity,
                WristPosition = hand.WristPosition,
                ElbowPosition = hand.Arm.ElbowPosition
            };

            foreach (Finger finger in hand.Fingers)
            {
                SerializableFinger serializableFinger = new SerializableFinger
                {
                    Direction = finger.Direction,
                    TipPosition = finger.TipPosition
                };

                for (int i = 0; i < 4; i++)
                {
                    MyBone myBone = new MyBone
                    {
                        Width = finger.bones[i].Width,
                        Length = finger.bones[i].Length,
                        Center = finger.bones[i].Center,
                        NextJoint = finger.bones[i].NextJoint,
                        PrevJoint = finger.bones[i].PrevJoint
                    };

                    serializableFinger.Bones.Add(myBone);
                }

                palmArmData.fingers.Add(serializableFinger);
            }

            string jsonString = JsonUtility.ToJson(palmArmData);
            handDataList.Add(jsonString);
        }

        File.AppendAllLines(filePath, handDataList);

        // Call mirrorJson after creating the JSON file
        // mirrorJson();
    }

    // New function to mirror the JSON data
    public void mirrorJson()
    {
        string mirroredFilePath = "mirrored_data4.json";

        if (File.Exists(filePath))
        {
            string[] lines = File.ReadAllLines(filePath);
            List<string> mirroredLines = new List<string>();

            foreach (string line in lines)
            {
                PalmArm data = JsonUtility.FromJson<PalmArm>(line);

                // Mirror the data by flipping the x-coordinates
                data.PalmPosition.x = -data.PalmPosition.x;
                data.PalmVelocity.x = -data.PalmVelocity.x;
                data.WristPosition.x = -data.WristPosition.x;
                data.ElbowPosition.x = -data.ElbowPosition.x;

                foreach (var finger in data.fingers)
                {
                    finger.Direction.x = -finger.Direction.x;
                    finger.TipPosition.x = -finger.TipPosition.x;

                    foreach (var bone in finger.Bones)
                    {
                        bone.Center.x = -bone.Center.x;
                        bone.NextJoint.x = -bone.NextJoint.x;
                        bone.PrevJoint.x = -bone.PrevJoint.x;
                    }
                }

                string mirroredJsonString = JsonUtility.ToJson(data);
                mirroredLines.Add(mirroredJsonString);
            }

            File.WriteAllLines(mirroredFilePath, mirroredLines);
        }
        else
        {
            Debug.LogError("Original JSON file does not exist.");
        }
    }
}
