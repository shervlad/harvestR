import torch
from torch.utils.data.dataset import Dataset  # For custom data-sets
#import torchvision.transforms as transforms
from PIL import Image
import numpy as np
#import torchvision.transforms.functional
import os
from skimage import io, transform
import matplotlib.pyplot as plt
from utils import og_from_voxel_coords
    
class CustomDataset(Dataset):
    def __init__(self, image_path="../Fruit Picker Unity/observations/camera/", 
                       voxels_path='../Fruit Picker Unity/observations/voxels/'):   # initial logic happens like transform

        self.image_path = image_path
        self.voxels_path = voxels_path

    def __getitem__(self, index):

        frame = index*5
        depth_name = os.path.join(self.image_path ,  'depth',  'Trivial_%s_depth.png'%frame)
        seg_name   = os.path.join(self.image_path ,  'layer',  'Trivial_%s_layer.png'%frame)

        depth_data = io.imread(depth_name)
        seg_data   = io.imread(seg_name)

        og = og_from_voxel_coords(os.path.join(self.voxels_path,'voxels%s.txt'%frame))

        s = seg_data.shape
        onehot = np.zeros((11, *s[:2]))
        for i in range(s[0]):
            for j in range(s[1]):
                if seg_data[i,j,0] > 7:
                    onehot[seg_data[i,j,0]-7][i,j] = 1
                if seg_data[i,j,0] == 0:
                    onehot[0][i,j] = 1

                
        onehot[10] = depth_data[:,:,0]

        onehot = torch.as_tensor(onehot,dtype=torch.float32)
        og     = torch.as_tensor(og,dtype=torch.long)
        return onehot, og

    def __len__(self):  # return count of sample we have
        return len(os.listdir(os.path.join(self.image_path,'img')))