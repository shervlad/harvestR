from dataset import CustomDataset
import numpy as np
import matplotlib.pyplot as plt
import pickle
import imageio
import os
from array2gif import write_gif
d = CustomDataset()

rgb_data, depth_data, seg_data, seg_data_gray = d[0]
image_array = seg_data
# image_array = image_array[:,:,0]
s = image_array.shape
gifs = [[np.zeros(s) for j in range(len(d))] for i in range(17)]

for sample_no in range(len(d)):
    # sample_no = 10
    print(sample_no)
    rgb_data, depth_data, seg_data, seg_data_gray = d[sample_no]
    image_array = seg_data

    image_array = image_array[:,:,0]
    s = image_array.shape

    num_layers = np.unique(image_array).shape[0]
    for i in range(s[0]):
        for j in range(s[1]):
            gifs[image_array[i,j]][sample_no][i,j]=np.array([255,255,255])

for i in range(len(gifs)):
    write_gif(gifs[i], '%s.gif'%i, fps=5)