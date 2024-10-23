// using System;
// using System.Diagnostics;  // Needed for running external processes
// using System.IO;
// using UnityEngine;  // Needed for logging in the Unity Console

// public class DWTAnalyzer : MonoBehaviour
// {
//     // Paths to your JSON files and Python script
//     public string jsonFile1 = "synced1/sync_left_hand_data.json";
//     public string jsonFile2 = "synced1/sync_right_hand_data.json";
//     public string pythonScript = "DWTUnity.py";  // Path to your Python script

//     void Start()
//     {
//         if (File.Exists(jsonFile1) && File.Exists(jsonFile2))
//         {
//             RunPythonScript(jsonFile1, jsonFile2);
//         }
//         else
//         {
//             UnityEngine.Debug.LogError("JSON files not found.");
//         }
//     }

//     void RunPythonScript(string jsonFile1, string jsonFile2)
//     {
//         // Ensure Python is available on the system PATH
//         ProcessStartInfo startInfo = new ProcessStartInfo();
//         startInfo.FileName = "python";  // Assumes Python is installed and available in the system PATH

//         // Pass the Python script and the JSON files as arguments
//         startInfo.Arguments = $"{pythonScript} {jsonFile1} {jsonFile2}";
//         startInfo.UseShellExecute = false;  // Allows for redirection of output
//         startInfo.RedirectStandardOutput = true;
//         startInfo.RedirectStandardError = true;

//         try
//         {
//             // Start the Python process
//             using (Process process = Process.Start(startInfo))
//             {
//                 // Capture the standard output from the Python script
//                 using (StreamReader reader = process.StandardOutput)
//                 {
//                     string result = reader.ReadToEnd();
//                     UnityEngine.Debug.Log($"Python script output: {result}");
//                 }

//                 // Capture any errors that the Python script may have produced
//                 string error = process.StandardError.ReadToEnd();
//                 if (!string.IsNullOrEmpty(error))
//                 {
//                     UnityEngine.Debug.LogError($"Python script error: {error}");
//                 }

//                 // Ensure the process finishes
//                 process.WaitForExit();
//             }
//         }
//         catch (Exception e)
//         {
//             UnityEngine.Debug.LogError($"Error running Python script: {e.Message}");
//         }
//     }
// }
