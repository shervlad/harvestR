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

from torch.nn.functional import softmax

class Decoder(nn.Module):

    def __init__(self):
        super(Decoder, self).__init__()
        self.layer1 = nn.Linear(128, 256)
        self.layer2 = nn.Linear(256, 512)
        self.layer3 = nn.Sequential(
            nn.ConvTranspose2d(in_channels=8,out_channels=16,kernel_size=4,
                               stride=2,padding=1),
        )
        self.layer4 = nn.Sequential( 
            nn.ConvTranspose3d(in_channels=1,out_channels=8,kernel_size=4,
                               stride=2,padding=1),
        )
        self.layer5 = nn.Sequential(
            nn.ConvTranspose3d(in_channels=8,out_channels=8,kernel_size=4,
                               stride=2,padding=1),
        )
        self.layer6 = nn.Sequential(
            nn.ConvTranspose3d(in_channels=8,out_channels=8,kernel_size=4,
                               stride=2,padding=1),
        )

    def forward(self, x,verbose=False): 
            batch_size = -1
            if(verbose):
                print("**input**", x.size())
            out = self.layer1(x)
            if(verbose):
                print("**1**",out.size())
            out = self.layer2(out)
            if(verbose):
                print("**2**",out.size())
            out = out.view(batch_size,8,8,8)
            out = self.layer3(out)
            if(verbose):
                print("**3**",out.size())
            out = out.view(batch_size,1,16,16,16)
            out = self.layer4(out)
            if(verbose):
                print("**4**",out.size())
            out = out.view(batch_size,8,32,32,32)
            out = self.layer5(out)
            if(verbose):
                print("**5**",out.size())
            out = out.view(batch_size,8,64,64,64)
            out = self.layer5(out)
            if(verbose):
                print("**5**",out.size())
            out = softmax(out,dim=1)
            return out