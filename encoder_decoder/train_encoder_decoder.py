from dataset import CustomDataset
import numpy as np
import matplotlib.pyplot as plt
import pickle
import imageio
import os
d = CustomDataset()
gifs = [[] for i in range(19)]

f = open('channel_dict.pickle','rb')
channel_dict = pickle.load(f) #dictionary that maps colors to channels
f.close()

for sample_no in range(len(d)):
    print(sample_no)
    rgb_data, depth_data, seg_data, seg_data_gray = d[sample_no]
    image_array = seg_data

    channels = []

    for i in range(len(channel_dict)):
        channels.append(np.zeros(image_array.shape[:2]))

    s = image_array.shape

    for i in range(s[0]):
        for j in range(s[1]):
            t = tuple(image_array[i,j])
            if t in channel_dict:
                channels[channel_dict[t]][i,j] = 1

    # print(channels[8]))

    channel_indices = {
        'stem'         : [0,1],
        'leaf'         : [2,4],
        'wall'         : [6,15],
        'peduncle'     : [20],
        'gripper'      : [8,18],
        'ripe_fruit'   : [16],
    }

    channels_to_display = [
        # 0,   #stem
        # 1,   #stem
        # 2,   #leaf
        # 3,   
        # 4,   #leaf
        # 5,   #arm
        # 6,   #wall
        # 7,   
        # 8,   #gripper
        # 9,   
        # 10,  
        # 11,  
        # 12,
        # 13,  #arm
        # 14,
        # 15,  #wall
        # 16,  #ripe fruit
        # 17,  
        # 18,  #gripper
        # 19,  
        # 20   #peduncle
    ]

    # images = []
    # for label in channel_indices:
    #     img = np.zeros(channels[0].shape)
    #     for c in channel_indices[label]:
    #         img += channels[c]
    #     plt.imshow(img, cmap='gray')
    #     plt.title(label)
    #     plt.show()

    # for filename in filenames:
    #     images.append(imageio.imread(filename))

    # img = np.zeros(channels[0].shape)
    # for i in channels_to_display:
    #     img+=channels[i]

    # plt.imshow(img, cmap='gray')
    # plt.show()
    for i in range(len(channels)):
        if(str(i) not in os.listdir("./images_by_channel/")):
            os.mkdir("./images_by_channel/%s"%i)
            
        plt.imshow(channels[i],cmap='gray')
        plt.savefig('./images_by_channel/%s/%s.png'%(i,sample_no))
    # print(np.unique(image_array,axis=1))
    # print(np.unique(image_array[:,:,2]))

