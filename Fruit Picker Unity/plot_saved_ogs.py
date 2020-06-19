import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os


bound = 0.5
scale = 100
span  = 2*bound
gs = int(span*scale) #grid size

tags = ['stem','gripper','fruit']
colors = ['white','green','green','red','green','black','blue','brown']


directory = './ogs/'
for filename in os.listdir(directory):
    print(filename)
    global_og = np.load(directory + filename)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(0,gs)
    ax.set_ylim(0,gs)
    ax.set_zlim(0,gs)
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")
    ax.set_zlabel("z axis")


    for og,color in zip(global_og,colors):
        x,y,z= og.nonzero()
        ax.scatter(x, y, z, marker='s',s=1,color=color)
        filename = filename.replace('.npy','png')
    # plt.show()
    plt.savefig('./plots_og/%s'%filename)
    plt.close()