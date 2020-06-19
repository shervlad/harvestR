using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class Measure : MonoBehaviour
{
    [Header("Arrows")]
    public GameObject ArrowL;
    public GameObject ArrowR;

    [Range(0,1.0f)]
    public float arrowScale = 0.15f;

    [Range(0,90)]
    public float arrowAngle = 0;

    public Color arrowColor;

    [Header("Canvas")]
    public Color textColor;

    public Text textField;

    [Range(0,0.05f)]
    public float textScale = 0.02f;

    public GameObject canvas;

    float distance;

    void OnDrawGizmos(){
        MeasureStuff();

    }

    void MeasureStuff(){
        distance = Vector3.Distance(ArrowL.transform.position, ArrowR.transform.position);
        textField.text = distance.ToString("N3") + "m";
        canvas.transform.position = LerpByDistance(ArrowL.transform.position,ArrowR.transform.position,0.5f);

        if(ArrowL != null){
            ArrowL.GetComponent<SpriteRenderer>().color = arrowColor;
            ArrowL.transform.localScale = new Vector3(arrowScale,arrowScale,0);
            ArrowL.transform.localRotation = Quaternion.Euler(arrowAngle,0,0);
        }
        if(ArrowR != null){
            ArrowR.GetComponent<SpriteRenderer>().color = arrowColor;
            ArrowR.transform.localScale = new Vector3(arrowScale,arrowScale,0);
            ArrowR.transform.localRotation = Quaternion.Euler(arrowAngle,0,0);
        }

        if(textField != null){
            textField.color = textColor;
            textField.transform.localScale = new Vector3(textScale,textScale,0);
        }
    }

    Vector3 LerpByDistance(Vector3 A, Vector3 B, float x){
        Vector3 P = A + x*(B-A);
        return P;
    }

}
