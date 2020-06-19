import torch.optim as optim
from torch.nn import CrossEntropyLoss as CEL
import torch
import numpy as np
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from dataset import CustomDataset
from ved import VED
# coding: utf-8

d = CustomDataset()

dataloader = DataLoader(d,batch_size=4,shuffle=True)
ved = VED()
optimizer = optim.Adam(ved.parameters(), lr=0.0001)
loss = CEL()
for i_batch, sample_batched in enumerate(dataloader):
    print(i_batch)
    optimizer.zero_grad()
    x = sample_batched[0]
    y = sample_batched[1]
    output = ved(x)
    L = loss(output,y)
    print("Loss: %s"%L.item())
    L.backward()
    optimizer.step()

