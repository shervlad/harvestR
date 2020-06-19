using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IgnoreStemCollisions : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void OnCollisionStay(Collision collision){
        Debug.Log("Colliding with " + collision.gameObject.tag);
        if (collision.gameObject.tag == "stem"){
            Debug.Log("Avoiding Collision...");
            Physics.IgnoreCollision(collision.gameObject.GetComponent<Collider>(), GetComponent<Collider>());
        }
    }
    void OnCollisionEnter(Collision collision){
        Debug.Log("Colliding with " + collision.gameObject.tag);
        if (collision.gameObject.tag == "stem"){
            Debug.Log("Avoiding Collision...");
            Physics.IgnoreCollision(collision.gameObject.GetComponent<Collider>(), GetComponent<Collider>());
        }
    }
}
