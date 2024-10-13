// using System;
// using System.IO;
// using Python.Runtime;
// using UnityEngine;

// public class DWTAnalyzer : MonoBehaviour
// {
//     // Paths to your JSON files
//     public string jsonFile1 = "synced1/sync_left_hand_data.json";
//     public string jsonFile2 = "synced1/sync_right_hand_data.json";

//     void Start()
//     {
//         if (File.Exists(jsonFile1) && File.Exists(jsonFile2))
//         {
//             AnalyzeHandMovements(jsonFile1, jsonFile2);
//         }
//         else
//         {
//             Debug.LogError("JSON files not found.");
//         }
//     }

//     void AnalyzeHandMovements(string jsonFile1, string jsonFile2)
//     {
//         // Ensure the Python environment is initialized properly
//         Environment.SetEnvironmentVariable("PYTHONHOME", @"C:\Users\dovy4\AppData\Local\Programs\Python\Python312");
//         Environment.SetEnvironmentVariable("PYTHONPATH", @"C:\Users\dovy4\AppData\Local\Programs\Python\Python312\Lib");

//         // Use PythonNet to call the Python function
//         using (Py.GIL())
//         {
//             try
//             {
//                 // Import your Python script (make sure your script is in the Python environment or specify its path)
//                 dynamic pyModule = Py.Import("DWTUnity"); // No '.py' extension here
//                 dynamic result = pyModule.analyze_sync(jsonFile1, jsonFile2); // Call the analyze_sync function

//                 // Extract the results from the Python dictionary
//                 double distancePosition = result["distance_position"];
//                 double normalizedDistancePosition = result["normalized_distance_position"];
//                 double distanceVelocity = result["distance_velocity"];
//                 double normalizedDistanceVelocity = result["normalized_distance_velocity"];
//                 double distanceTipPosition = result["distance_tip_position"];
//                 double normalizedDistanceTipPosition = result["normalized_distance_tip_position"];

//                 // Log the results in Unity's console
//                 Debug.Log($"DTW Distance (Position): {distancePosition}");
//                 Debug.Log($"Normalized DTW Distance (Position): {normalizedDistancePosition}");
//                 Debug.Log($"DTW Distance (Velocity): {distanceVelocity}");
//                 Debug.Log($"Normalized DTW Distance (Velocity): {normalizedDistanceVelocity}");
//                 Debug.Log($"DTW Distance (Tip Position): {distanceTipPosition}");
//                 Debug.Log($"Normalized DTW Distance (Tip Position): {normalizedDistanceTipPosition}");
//             }
//             catch (Exception e)
//             {
//                 Debug.LogError($"Error in Python analysis: {e.Message}");
//             }
//         }
//     }
// }
using System;
using System.Diagnostics;  // Needed for running external processes
using System.IO;
using UnityEngine;  // Needed for logging in the Unity Console

public class DWTAnalyzer : MonoBehaviour
{
    // Paths to your JSON files and Python script
    public string jsonFile1 = "synced1/sync_left_hand_data.json";
    public string jsonFile2 = "synced1/sync_right_hand_data.json";
    public string pythonScript = "DWTUnity.py";  // Path to your Python script

    void Start()
    {
        if (File.Exists(jsonFile1) && File.Exists(jsonFile2))
        {
            RunPythonScript(jsonFile1, jsonFile2);
        }
        else
        {
            UnityEngine.Debug.LogError("JSON files not found.");
        }
    }

    void RunPythonScript(string jsonFile1, string jsonFile2)
    {
        // Ensure Python is available on the system PATH
        ProcessStartInfo startInfo = new ProcessStartInfo();
        startInfo.FileName = "python";  // Assumes Python is installed and available in the system PATH

        // Pass the Python script and the JSON files as arguments
        startInfo.Arguments = $"{pythonScript} {jsonFile1} {jsonFile2}";
        startInfo.UseShellExecute = false;  // Allows for redirection of output
        startInfo.RedirectStandardOutput = true;
        startInfo.RedirectStandardError = true;

        try
        {
            // Start the Python process
            using (Process process = Process.Start(startInfo))
            {
                // Capture the standard output from the Python script
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    UnityEngine.Debug.Log($"Python script output: {result}");
                }

                // Capture any errors that the Python script may have produced
                string error = process.StandardError.ReadToEnd();
                if (!string.IsNullOrEmpty(error))
                {
                    UnityEngine.Debug.LogError($"Python script error: {error}");
                }

                // Ensure the process finishes
                process.WaitForExit();
            }
        }
        catch (Exception e)
        {
            UnityEngine.Debug.LogError($"Error running Python script: {e.Message}");
        }
    }
}
