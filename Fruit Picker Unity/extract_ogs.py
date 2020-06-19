import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

directory = './frames/'

bound = 0.5
scale = 100
span  = 2*bound
gs = int(span*scale) #grid size

layers = [ "Default", "TransparentFX", "Ignore Raycast", "_", "Water", "UI", "_", "_", "wall", "leaf", "stem", "peduncle", "ripe_fruit", "unripe_fruit", "gripper"]
tags = ['default','stem','leaf','ripe_fruit','unripe_fruit','wall','gripper','peduncle']


for filename in os.listdir(directory):
    frame = 0
    frame = int(filename.replace('voxels','')[:-4])
    all_coords = {'other':[]}
    global_og = np.zeros((gs,gs,gs))

    for tag in tags:
        all_coords[tag] = []

    f = open(directory + filename,'r')
    for l in f:
        x,y,z,layeridx = l.replace('\n','').split(',')
        # print(tag)
        x = float(x)
        y = float(y)
        z = float(z)
        layeridx = int(layeridx)
        tag = layers[layeridx]
        if tag in tags:
            all_coords[tag].append([x,y,z])
        else:
            all_coords['other'].append([x,y,z])

    result = []
    for classidx,tag in enumerate(tags):
        coords = np.array(all_coords[tag])
        coords = np.array(coords).reshape(-1,3)
        og = np.zeros((gs,gs,gs))
        # print(coords.shape)
        # coords = np.unique(coords,axis=0)
        # print(coords.shape)


        x = coords[:,0]
        z = coords[:,1]
        y = coords[:,2]
        indices = []

        for i in range(x.size):
            if x[i]  < -bound or x[i] > bound:
                indices.append(i)
                continue
            if y[i]  < -bound or y[i] > bound:
                indices.append(i)
                continue
            if z[i]  < -bound or z[i] > bound:
                indices.append(i)
                continue

        x = np.delete(x,indices)
        y = np.delete(y,indices)
        z = np.delete(z,indices)

        x = (x + bound)*scale
        y = (y + bound)*scale
        z = (z + bound)*scale

        x = x.astype(int)
        y = y.astype(int)
        z = z.astype(int)

        for i,j,k in zip(x,y,z):
            if i==0 and j==0 and k==0:
                continue
            og[i,j,k] = classidx
        result.append(og)
    result = np.array(result)
    filename = './ogs/og_%s'%frame
    np.save(filename,result)
