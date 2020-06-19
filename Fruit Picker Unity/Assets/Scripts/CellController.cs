using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CellController : MonoBehaviour
{
    public float cellSize = 0.05f;

    public string Label(){
        Collider[] hitColliders = Physics.OverlapSphere(transform.position, cellSize);
        if(hitColliders.Length == 0)
            return "";
        return hitColliders[0].tag;
    }
}
    