import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

def og_from_voxel_coords(filename, bound=0.5, scale = 128):
    """
    takes in a list of voxels and tags from 'filename'
    returns a scalexscale caoccupancy grid
    """
    span  = 2*bound
    gs = int(span*scale) #grid size

    num_layers = 8

    all_coords = [[] for i in range(num_layers)]

    f = open(filename,'r')
    for l in f:
        x,y,z,layeridx = l.replace('\n','').split(',')
        # print(tag)
        x = float(x)
        y = float(y)
        z = float(z)
        layeridx = int(layeridx)
        if 16 > layeridx > 7:
            all_coords[layeridx-8].append([x,y,z])

    og = np.zeros((gs,gs,gs))
    for classidx in range(num_layers):
        coords = np.array(all_coords[classidx])
        coords = np.array(coords).reshape(-1,3)

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
    return og


def plot_og(og, dest=None, show=False, gs=128):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0,gs)
    ax.set_ylim(0,gs)
    ax.set_zlim(0,gs)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")

    colors = ['blue','green','green','yellow','red','brown','black','black','black']
    for c,color in zip(og,colors):
        x,y,z= c.nonzero()
        ax.scatter(x, y, z, marker='s',s=1,color=color)
    if show:
        plt.show()
    if dest is not None:
        plt.savefig(dest)
    plt.close()

