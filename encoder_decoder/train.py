import torch.optim as optim
from   torch.nn import CrossEntropyLoss
import torch
import numpy as np
from   torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from   custom_dataset import CustomDataset
from   variational_encoder_decoder import VariationalEncoderDecoder
# coding: utf-8

d = CustomDataset()

dataloader = DataLoader(d,batch_size=4,shuffle=True)
ved        = VariationalEncoderDecoder()
optimizer  = optim.Adam(ved.parameters(), lr=0.0001)
loss       = CrossEntropyLoss()

for epoch in range(100):
    for i_batch, (x,y) in enumerate(dataloader):
        print(i_batch)
        optimizer.zero_grad()
        output = ved(x)
        L = loss(output,y)
        print("Loss: %s"%L.item())
        L.backward()
        optimizer.step()