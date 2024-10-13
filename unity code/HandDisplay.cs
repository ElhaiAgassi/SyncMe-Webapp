// Author: Zeev Fischer
/*
This class will read two JSON files corresponding to the classes MyBone and SerializableFinger
(again, imported from the file HandData.cs). It will work only after pressing "q"!!
*/
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using UnityEngine.UI;
using System.Text.Json;

public class HandDisplay : MonoBehaviour
{
    // Paths for the two JSON files
    string filePath1 = "sync_left_hand_data.json";
    string filePath2 = "sync_right_hand_data.json";
    string filePath= "unsynced2.json";
    //  string filePath1 = "temp1.json";
    // string filePath2 = "temp2.json";

    // Start is called before the first frame update
    // the commented code is for displaying 2 files where each one represents a hand and the current code shows a full combined file !
    // IEnumerator Start()
    // {
    //     while (true)
    //     {
    //         if (Input.GetKey(KeyCode.Q))
    //         {
    //             // Read the JSON files
    //             string[] jsonLines1 = File.ReadAllLines(filePath1);
    //             string[] jsonLines2 = File.ReadAllLines(filePath2);

    //             // Initialize frame ID for synchronization
    //             long frameid1 = -1;
    //             long frameid2 = -1;

    //             // Iterate through each line in the first file
    //             for (int i = 0; i < jsonLines1.Length && i < jsonLines2.Length; i++)
    //             {
    //                 // Deserialize the JSON data into PalmArm objects
    //                 PalmArm palmArmData1 = JsonUtility.FromJson<PalmArm>(jsonLines1[i]);
    //                 PalmArm palmArmData2 = JsonUtility.FromJson<PalmArm>(jsonLines2[i]);

    //                 if (frameid1 == -1 && frameid2 == -1)
    //                 {
    //                     frameid1 = palmArmData1.frameId;
    //                     frameid2 = palmArmData2.frameId;
    //                 }

    //                 if ((frameid1 != -1 && frameid1 != palmArmData1.frameId) || 
    //                     (frameid2 != -1 && frameid2 != palmArmData2.frameId))
    //                 {
    //                     float delay1 = (palmArmData1.PalmVelocity.magnitude * Time.deltaTime) + 0.009f;
    //                     float delay2 = (palmArmData2.PalmVelocity.magnitude * Time.deltaTime) + 0.009f;
    //                     yield return new WaitForSeconds(Mathf.Max(delay1, delay2));

    //                     ClearCylinders();
    //                     ClearPalmAndWrist();

    //                     frameid1 = palmArmData1.frameId;
    //                     frameid2 = palmArmData2.frameId;
    //                 }

    //                 float radius = 0.03f;

    //                 // Draw first hand
    //                 DrawPalmAndWrist(palmArmData1.PalmPosition, palmArmData1.WristPosition, palmArmData1.ElbowPosition, radius, Color.green, Color.blue, Color.grey);
    //                 foreach (SerializableFinger finger in palmArmData1.fingers)
    //                 {
    //                     foreach (MyBone bone in finger.Bones)
    //                     {
    //                         DrawCylinder(bone.PrevJoint, bone.NextJoint, bone.Width, Color.green);
    //                     }
    //                 }

    //                 // Draw second hand
    //                 DrawPalmAndWrist(palmArmData2.PalmPosition, palmArmData2.WristPosition, palmArmData2.ElbowPosition, radius, Color.yellow, Color.red, Color.cyan);
    //                 foreach (SerializableFinger finger in palmArmData2.fingers)
    //                 {
    //                     foreach (MyBone bone in finger.Bones)
    //                     {
    //                         DrawCylinder(bone.PrevJoint, bone.NextJoint, bone.Width, Color.yellow);
    //                     }
    //                 }
    //             }

    //             // Clear the last drawn hands
    //             ClearCylinders();
    //             ClearPalmAndWrist();
    //         }
    //         yield return null;
    //     }
    // }
    IEnumerator Start()
    {
        while (true)
        {
            if (Input.GetKey(KeyCode.Q))
            {
                // Read the JSON file
                string[] jsonLines = File.ReadAllLines(filePath);
                long frameid = -1;
                // Iterate through each line in the file
                foreach (string jsonLine in jsonLines)
                {
                    // Deserialize the JSON data into PalmArm
                    PalmArm palmArmData = JsonUtility.FromJson<PalmArm>(jsonLine);
                    if (frameid == -1)
                    {
                        frameid = palmArmData.frameId;
                    }
                    if (frameid != -1 && frameid != palmArmData.frameId)
                    {
                        float delay = (palmArmData.PalmVelocity.magnitude * Time.deltaTime) + 0.009f;
                        yield return new WaitForSeconds(delay);
                        
                        ClearCylinders();
                        ClearPalmAndWrist();
                        frameid = palmArmData.frameId;
                    }

                    float radios = 0.03f;
                    // Debug.Log("started creating");
                    DrawPalmAndWrist(palmArmData.PalmPosition, palmArmData.WristPosition, palmArmData.ElbowPosition, radios,Color.green, Color.blue, Color.grey);

                    // Iterate through each finger in the palm
                    foreach (SerializableFinger finger in palmArmData.fingers)
                    {
                        // Iterate through each bone in the finger
                        foreach (MyBone bone in finger.Bones)
                        {
                            // Call DrawCylinder function with bone data
                            DrawCylinder(bone.PrevJoint, bone.NextJoint, bone.Width,Color.yellow);
                        }
                    }
                    // Debug.Log("end creation");
                }

                // Delete the last hand
                ClearCylinders();
                ClearPalmAndWrist();
            }
            yield return null;
        }
    }

    private List<GameObject> cylinders = new List<GameObject>();
    private List<GameObject> spheres = new List<GameObject>();

    private void ClearCylinders()
    {
        foreach (var cylinder in cylinders)
        {
            Destroy(cylinder);
        }
        cylinders.Clear();
    }

    private void ClearPalmAndWrist()
    {
        foreach (var sphere in spheres)
        {
            Destroy(sphere);
        }
        spheres.Clear();
    }

    private void DrawCylinder(Vector3 start, Vector3 end, float width, Color color)
    {
        Vector3 position = (start + end) / 2f;
        Quaternion rotation = Quaternion.FromToRotation(Vector3.up, end - start);

        GameObject cylinder = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        cylinder.transform.position = position;
        cylinder.transform.rotation = rotation;
        cylinder.transform.localScale = new Vector3(width, Vector3.Distance(start, end) / 2f, width);
        cylinder.GetComponent<Renderer>().material.color = color;

        cylinders.Add(cylinder);
    }

    private void DrawPalmAndWrist(Vector3 palmPosition, Vector3 wristPosition, Vector3 elbowPosition, float ballRadius, Color palmColor, Color wristColor, Color elbowColor)
    {
        GameObject palmObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        palmObject.transform.position = palmPosition;
        palmObject.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        palmObject.GetComponent<Renderer>().material.color = palmColor;

        spheres.Add(palmObject);

        GameObject wristObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        wristObject.transform.position = wristPosition;
        wristObject.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        wristObject.GetComponent<Renderer>().material.color = wristColor;

        spheres.Add(wristObject);

        GameObject elbowObject = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        elbowObject.transform.position = elbowPosition;
        elbowObject.transform.localScale = new Vector3(ballRadius, ballRadius, ballRadius);
        elbowObject.GetComponent<Renderer>().material.color = elbowColor;

        spheres.Add(elbowObject);

        LineRenderer lineRenderer = wristObject.AddComponent<LineRenderer>();
        lineRenderer.material.color = Color.red;
        lineRenderer.startWidth = 0.02f;
        lineRenderer.endWidth = 0.02f;
        lineRenderer.positionCount = 2;
        lineRenderer.SetPosition(0, wristPosition);
        lineRenderer.SetPosition(1, elbowPosition);
    }
}
