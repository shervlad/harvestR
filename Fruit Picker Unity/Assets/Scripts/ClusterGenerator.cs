using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ClusterGenerator : MonoBehaviour
{

    // public prefab plant;
    // Start is called before the first frame update
    void Start()
    {
        for(int j=-1;j<=1;j++){
            float y = 1.5f * j;
            for(int i=-1;i<=1;i++){
                float x = i*1.0f;
                float angle_y =  Random.Range(-20, 20);
            }
        }

    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
