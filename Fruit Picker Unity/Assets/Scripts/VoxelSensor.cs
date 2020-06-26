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
    private int[] resolutions = {20, //Default
                                 20, //
                                 20, //
                                 20, //
                                 20, //
                                 20, //
                                 20, //
                                 20, //
                                 100, // wall
                                 20, // leaf
                                 20, // stem
                                 20, // peduncle
                                 20, // ripe_fruit
                                 20, // unripe_fruit
                                 20, // gripper
                                 20, // arm
                                 20};// robot
    [SerializeField] protected bool useUV;
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
        List<int> layers = new List<int>();
        Debug.Log(string.Format("{0} objects",hitColliders.Length));
        for (int i=0;i < hitColliders.Length;i++)
        {
            int layer = hitColliders[i].gameObject.layer;
            if(hitColliders[i].tag == "robot" || layer < 8)
                continue;
            // Debug.Log(hitColliders[i].name);
            Mesh mesh = hitColliders[i].GetComponent<MeshFilter>().sharedMesh;
            var scale = hitColliders[i].transform.lossyScale.magnitude;
            // int res = (int)(resolution*scale);
            int res = resolutions[layer];
            var data = GPUVoxelizer.Voxelize(voxelizer, mesh, res, (type == MeshType.Volume));
            // voxel
            Voxel_t[] voxels = data.GetData();
            for(int j=0;j<voxels.Length;j++)
            {
                voxels[j].position = hitColliders[i].transform.TransformPoint(voxels[j].position);
                voxels[j].position = transform.InverseTransformPoint(voxels[j].position);
                layers.Add(layer);
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
                    int layer = layers[i];
                    float U = v.uv.x;
                    float V = v.uv.y;
                    if(!v.IsEmpty()){
                        file.WriteLine(string.Format("{0},{1},{2},{3},{4},{5}",x,y,z,layer,U,V));
                    }
                }
            }
        
    
    frame++;
    }
}