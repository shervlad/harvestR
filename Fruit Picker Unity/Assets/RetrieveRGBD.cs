﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;

[RequireComponent (typeof(ImageSynthesis))]

public class RetrieveRGBD : MonoBehaviour
{
	public int width = 256;
	public int height = 256;
	private int imageCounter = 1;

	private int frame;
	void Start(){
		frame = 0;
	}
	void Update(){
		if(frame%5==0){
			var sceneName = SceneManager.GetActiveScene().name;
			// NOTE: due to per-camera / per-object motion being calculated late in the frame and after Update()
			// capturing is moved into LateUpdate (see ImageSynthesis.cs Known Issues)
			GetComponent<ImageSynthesisRGBD>().Save(sceneName + "_" + frame, width, height,"./observations/camera/");
		}
		frame++;
	}
}
