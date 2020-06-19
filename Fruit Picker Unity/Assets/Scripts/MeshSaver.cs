using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System;
public class MeshSaver : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Mesh mesh = SpriteToMesh(GetComponent<SpriteRenderer>().sprite);
        AssetDatabase.CreateAsset(mesh, "Assets/Meshes/leaf_mesh.asset");
        AssetDatabase.SaveAssets();
    }

    Mesh SpriteToMesh(Sprite sprite){
        Mesh mesh = new Mesh();
        mesh.vertices = Array.ConvertAll(sprite.vertices, i => (Vector3)i);
        mesh.uv = sprite.uv;
        mesh.triangles = Array.ConvertAll(sprite.triangles, i => (int)i);
        Debug.Log("got mesh");
        return mesh;
    }        
    // Update is called once per frame
    void Update()
    {
        
    }
}
