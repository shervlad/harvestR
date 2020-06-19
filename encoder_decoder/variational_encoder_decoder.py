from encoder import Encoder
from decoder import Decoder
from torch.distributions.normal import Normal
import torch.nn as nn
import numpy as np
import torch

class VariationalEncoderDecoder(nn.Module):
    def __init__(self):
        super(VED, self).__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()
        loc = torch.as_tensor(np.zeros((128)),dtype=torch.float32)
        scale = torch.as_tensor(np.ones((128)), dtype=torch.float32)
        self.N = Normal(loc,scale)
    

    def forward(self, x, verbose=False): 
        mu, var = self.encoder(x)
        mu = mu.view(-1,1,1,128)
        var = var.view(-1,1,1,128)
        z = mu + var*self.N.sample()
        output = self.decoder(z)
        return output