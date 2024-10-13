using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using Leap;
using Leap.Unity;

public class SwitchHands : MonoBehaviour
{

    private int selectedHand;

    [Header("HANDS")]
    [SerializeField] private Transform[] hands;

    [Header("KEYS")]
    [SerializeField] private KeyCode[] keys;

    private void SetHands()
    {
        hands = new Transform[transform.childCount];
        for(int i = 0; i < transform.childCount; i++)
        {
            hands[i] = transform.GetChild(i);
        }
        if(keys == null) keys = new KeyCode[hands.Length];
    }
    private void SetHand(int handIndex)
    {
        for(int i = 0; i < hands.Length; i++)
        {
            hands[i].gameObject.SetActive(i == handIndex);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        SetHands();
        SetHand(0);
    }

    void Update()
    {
        int prevHand = selectedHand;
        for(int i = 0; i < keys.Length;i++)
        {
            if(Input.GetKeyDown(keys[i]))
            {
                selectedHand = i;
            }
        }
        if(prevHand != selectedHand) SetHand(selectedHand);
    }
}
