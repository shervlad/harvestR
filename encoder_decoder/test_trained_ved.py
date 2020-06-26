from variational_encoder_decoder import VariationalEncoderDecoder
import torch
from custom_dataset import CustomDataset
from   torch.utils.data import DataLoader
from utils import plot_og
import numpy as np

dataset = CustomDataset()
x,y = dataset[4]
x = x.view(1,*x.size())
y = y.detach().numpy()
ved = VariationalEncoderDecoder()
ved.load_state_dict(torch.load('ved.pt'))
ved.eval()

predicted_og = ved(x).detach().numpy()


print(predicted_og.shape)
predicted_og = np.argmax(predicted_og,axis=1)
print(predicted_og.shape)

print(y.shape)

plot_og(y,show=True)