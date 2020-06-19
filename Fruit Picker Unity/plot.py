import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

directory = './frames/'
for filename in os.listdir('./frames/'):
    f = open(directory + filename,'r')
    coords = []
    for l in f:
        x,y,z,tag = l.replace('\n','').split(',')
        # print(tag)
        x = float(x)
        y = float(y)
        z = float(z)
        coords.append([x,y,z])

    if(len(coords)==0):
        continue
    coords = np.array(coords).reshape(-1,3)
    min_c = np.min(coords)
    max_c = np.max(coords)
    print(coords.shape)
    # coords = np.unique(coords,axis=0)
    # print(coords.shape)
    x = coords[:,0]
    z = coords[:,1]
    y = coords[:,2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, marker='o',s=0.5)
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")
    # plt.show()
    filename = filename.replace('.txt','.png')
    plt.savefig('./plots/%s'%filename)
    plt.close()