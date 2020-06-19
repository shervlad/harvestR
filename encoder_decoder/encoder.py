# importing the libraries
import pandas as pd
import numpy as np

# for reading and displaying images
from skimage.io import imread
import matplotlib.pyplot as plt

# for creating validation set
from sklearn.model_selection import train_test_split

# for evaluating the model
from sklearn.metrics import accuracy_score
from tqdm import tqdm

# PyTorch libraries and modules
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import Linear, ReLU, CrossEntropyLoss, Sequential, Conv2d, Conv3d, MaxPool2d, MaxPool3d, Module, Softmax, BatchNorm3d, Dropout
from torch.optim import Adam, SGD

class Encoder(nn.Module):

    def __init__(self):
        super(Encoder, self).__init__()
        self.layer1 = nn.Sequential(
            #8x256x256   -> 32x256x256  |  4 kernels 2x5x5 each
            nn.Conv2d(11, 32, kernel_size=(5,5), stride=1, padding=2),
            nn.ReLU(),
            #32x256x256 -> 32x128x128  |
            nn.MaxPool2d(kernel_size=5, stride=2, padding=2)
        )
        self.layer2 = nn.Sequential( 
            #32x128x128   -> 32x128x128 
            nn.Conv2d(32, 32, kernel_size=(5,5), stride=1, padding=2),
            nn.ReLU(),
            #32x128x128 -> 32x64x64
            nn.MaxPool2d(kernel_size=5, stride=2, padding=2)
        )
        self.layer3 = nn.Sequential(
            #32x64x64 -> 8x64x64
            nn.Conv3d(1, 8, kernel_size=(32,5,5), stride=1, padding=(0,2,2)),
            nn.ReLU(),
            #8x64x64  -> 8x32x32
            nn.MaxPool3d(kernel_size=(1,5,5), stride=(1,2,2),padding=(0,2,2))
        )
        self.layer4 = nn.Sequential(
            #8x32x32 -> 8x32x32
            nn.Conv3d(1, 8, kernel_size=(8,5,5), stride=1, padding=(0,2,2)),
            nn.ReLU(),
            #8x32x32 -> 8x16x16
            nn.MaxPool3d(kernel_size=5, stride=(1,2,2),padding=2)
        )
        self.layer5 = nn.Sequential(
            #8x16x16 -> 8x16x16
            nn.Conv3d(1, 8, kernel_size=(8,5,5), stride=1, padding=(0,2,2)),
            nn.ReLU(),
            #8x16x16 -> 8x8x8
            nn.MaxPool3d(kernel_size=5, stride=(1,2,2),padding=2)
        )
        self.drop_out = nn.Dropout()
        self.fc1 = nn.Linear(512, 256)
        self.mu = nn.Linear(256, 128)
        self.var = nn.Linear(256, 128)

    def forward(self, x, verbose=False): 
            batch_size = -1
            if(verbose):
                print("**input**", x.size())
            out = self.layer1(x)
            if(verbose):
                print("**1**",out.size())
            out = self.layer2(out)
            if(verbose):
                print("**2**",out.size())
            out = out.view(batch_size,1,32,64,64)
            out = self.layer3(out)
            if(verbose):
                print("**3**",out.size())
            out = out.view(batch_size,1,8,32,32)
            out = self.layer4(out)
            if(verbose):
                print("**4**",out.size())
            out = out.view(batch_size,1,8,16,16)
            out = self.layer5(out)
            if(verbose):
                print("**5**",out.size())
            out = out.view(batch_size,1,512)
            out = self.drop_out(out)
            if(verbose):
                print("**drop_out**",out.size())
            out = self.fc1(out)
            if(verbose):
                print("**fc1**",out.size())
            mu = self.mu(out)
            var = self.mu(out)
            if(verbose):
                print("**mu**",mu.size())
                print("**var**",var.size())
                print(mu)
            return mu, var
    # encoder

    # def recognition(self, input_images):
    #     """ build convolutional variational encoder with pytorch"""
    #     with tf.variable_scope("recognition"):
    #         h1 = lrelu(conv3d(input_images, 1, 16, "d_h1")) # 28x28x1 -> 14x14x16
    #         h2 = lrelu(conv2d(h1, 16, 32, "d_h2")) # 14x14x16 -> 7x7x32
    #         h2_flat = tf.reshape(h2,[self.batchsize, 7*7*32])

    #         w_mean = dense(h2_flat, 7*7*32, self.n_z, "w_mean")
    #         w_stddev = dense(h2_flat, 7*7*32, self.n_z, "w_stddev")

    #     return w_mean, w_stddev

    # # decoder
    # def generation(self, z):
    #     with tf.variable_scope("generation"):
    #         z_develop = dense(z, self.n_z, 7*7*32, scope='z_matrix')
    #         z_matrix = tf.nn.relu(tf.reshape(z_develop, [self.batchsize, 7, 7, 32]))
    #         h1 = tf.nn.relu(conv_transpose(z_matrix, [self.batchsize, 14, 14, 16], "g_h1"))
    #         h2 = conv_transpose(h1, [self.batchsize, 28, 28, 1], "g_h2")
    #         h2 = tf.nn.sigmoid(h2)

    #     return h2
