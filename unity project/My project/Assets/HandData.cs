/*
this will be used for a cleaner code because we use this in multipule fiels 
*/


using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class MyBone
{
    public float Width;
    public float Length;
    public Vector3 Center;
    public Vector3 NextJoint;
    public Vector3 PrevJoint;
}

[System.Serializable]
public class SerializableFinger
{
    public Vector3 Direction;
    public Vector3 TipPosition;
    public List<MyBone> Bones = new List<MyBone>();
}
[System.Serializable]
public class PalmArm
{
    public long frameId;
    public bool isleft;
    public List<SerializableFinger> fingers = new List<SerializableFinger>();
    public Vector3 PalmPosition;//The center position of the palm.
    public Vector3 PalmVelocity;//The rate of change of the palm position.
    public Vector3 WristPosition;//The position of the wrist of this hand.
    public Vector3 ElbowPosition;
    
}