using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using VoxelSystem;
public class VoxelSensor : MonoBehaviour
{

    enum MeshType {
        Volume, Surface
    };

    int frame = 0;
    [SerializeField] MeshType type = MeshType.Volume;
    [SerializeField] protected ComputeShader voxelizer;
    [SerializeField] protected int resolution = 10;
    [SerializeField] protected bool useUV = false;
    Vector3 center;
    [SerializeField] protected int radius;
    // Start is called before the first frame update
    void Start()
    {
        center = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        if(frame%5!=0){
            frame++;
            return;
        }
        Collider[] hitColliders = Physics.OverlapSphere(center, radius);
        List<Voxel_t> allVoxels = new List<Voxel_t>();
        List<string> tags = new List<string>();
        Debug.Log(string.Format("{0} objects",hitColliders.Length));
        for (int i=0;i < hitColliders.Length;i++)
        {
            if(hitColliders[i].tag == "robot")
                continue;
            if(hitColliders[i].tag == "stem")
                Debug.Log("STEM!");
            // Debug.Log(hitColliders[i].name);
            Mesh mesh = hitColliders[i].GetComponent<MeshFilter>().sharedMesh;
            var scale = hitColliders[i].transform.lossyScale.magnitude;
            // int res = (int)(resolution*scale);
            int res = resolution;
            var data = GPUVoxelizer.Voxelize(voxelizer, mesh, res, (type == MeshType.Volume));
            // voxel
            Voxel_t[] voxels = data.GetData();
            for(int j=0;j<voxels.Length;j++)
            {
                voxels[j].position = hitColliders[i].transform.TransformPoint(voxels[j].position);
                voxels[j].position = transform.InverseTransformPoint(voxels[j].position);
                tags.Add(string.Format("{0}",hitColliders[i].gameObject.layer));
            }
            allVoxels.AddRange(voxels);
            // GetComponent<MeshFilter>().sharedMesh = VoxelMesh.Build(voxels, data.UnitLength, useUV);
            data.Dispose();
        }

        // Debug.Log(string.Format("There are {0} voxels",voxels.Count));
        using (System.IO.StreamWriter file =
            new System.IO.StreamWriter(string.Format(@"./observations/voxels/voxels{0}.txt",frame)))
            {
                for(int i=0;i<allVoxels.Count;i++)
                {
                    Voxel_t v = allVoxels[i];
                    float x = v.position.x;
                    float y = v.position.y;
                    float z = v.position.z;
                    string tag = tags[i];
                    if(!v.IsEmpty()){
                        file.WriteLine(string.Format("{0},{1},{2},{3}",x,y,z,tag));
                    }
                }
            }
        
    
    frame++;
    }
}