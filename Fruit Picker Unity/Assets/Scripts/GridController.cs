using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridController : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject prefabCell;
    private float scaleFactor = 20f;
    private float cellSize;
    private int gridSize    = 20;
    private int frames      = 0;
    public int updateRate   = 3;
    private GameObject[,,] cells;
    public List<float> labels;

    void Start()
    {
        setUp();
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        if(frames%updateRate == 0)
            updateLabels();        
        frames++;
    }


    public List<float> getLabels(){
        return labels;
    }

    private void updateLabels(){
        List<float> labelGrid = new List<float>();
        for(int k=0;k<gridSize;k++){
            for(int j=0;j<gridSize;j++){
                for(int i=0;i<gridSize;i++){
                    if(cells[i,j,k].GetComponent<CellController>().Label() == "red"){
                        labelGrid.Add(1f);
                    }
                    else if(cells[i,j,k].GetComponent<CellController>().Label() == "green"){
                        labelGrid.Add(2f);
                    }
                    else if(cells[i,j,k].GetComponent<CellController>().Label() == "robot"){
                        labelGrid.Add(3f);
                    }
                    else{
                        labelGrid.Add(0f);
                    }
                }
            }
        }
        labels = labelGrid;
    }

    void setUp(){
        cells = new GameObject[gridSize,gridSize,gridSize];
        // GameObject cell = Instantiate(prefabCell, new Vector3(0, 0, 0), Quaternion.identity);
        cellSize = prefabCell.GetComponent<CellController>().cellSize;
        float distance = cellSize*1.01f;
        // Destroy(cell);
        float x,y,z;
        for(int j=0;j<gridSize;j++){
            y = transform.localPosition.y - gridSize*distance/2 + j*distance;
            for(int k=0;k<gridSize;k++){
                z = transform.localPosition.z -gridSize*distance/8.0f + k*distance;
                for(int i=0;i<gridSize;i++){
                    x = transform.localPosition.x -gridSize*distance/2 + i*distance;
                    cells[i,j,k] = Instantiate(prefabCell, new Vector3(0, 0, 0), Quaternion.identity);
                    cells[i,j,k].transform.parent = transform;
                    cells[i,j,k].transform.localPosition = new Vector3(x,y,z);
                    cells[i,j,k].transform.localScale    = new Vector3(cellSize,cellSize,cellSize);
                    cells[i,j,k].layer = LayerMask.NameToLayer("TransparentFX");
                }
            }
        }
    }
}
