using System;
using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;

using UnityEngine;
using UnityEngine.Rendering;
using Random = UnityEngine.Random;

namespace VoxelSystem.Demo
{

    public class GPUVoxelParticleSystem : MonoBehaviour {

        [SerializeField] protected Mesh mesh;
        [SerializeField] protected ComputeShader voxelizer;
        [SerializeField] protected int count = 64;

        protected GPUVoxelData data;

        void Start () {
            mesh = GetComponent<MeshFilter>().mesh;
			// data = GPUVoxelizer.Voxelize(voxelizer, mesh, count);

            // int[] indices;
            // var pointMesh = BuildPoints(data, out indices);
        }

        void Update(){
            mesh = GetComponent<MeshFilter>().mesh;
            GetComponent<MeshCollider>().sharedMesh = mesh;
        }

        void getParticles () {
            mesh = GetComponent<MeshFilter>().mesh;
			data = GPUVoxelizer.Voxelize(voxelizer, mesh, count);
            int[] indices;
            List<Vector3> vertices = BuildPoints(data, out indices);
            // Debug.Log(string.Format("There are {0} voxels",vertices.Count));
        }

        void OnDestroy ()
        {
            if(data != null)
            {
                data.Dispose();
                data = null;
            }
        }


        List<Vector3> BuildPoints(GPUVoxelData data, out int[] vIndices)
        {
			var voxels = data.GetData();
			var vertices = new List<Vector3>();
            var indices = new List<int>();
            var vIndicesTmp = new List<int>();

            var count = 0;
			for(int i = 0, n = voxels.Length; i < n; i++) {
				var v = voxels[i];
                if (v.fill > 0)
                {
                    vertices.Add(v.position);
                    indices.Add(count++);
                    vIndicesTmp.Add(i);
                }
            }
            vIndices = vIndicesTmp.ToArray();
            return vertices;
        }
    }
}