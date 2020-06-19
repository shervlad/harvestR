from encoder import Encoder
from decoder import Decoder
import numpy as np
import torch

e = Encoder()
d = Decoder()
x = torch.rand((1,8,256,256))
print("ENCODING...")
output = e(x)
output = output.view(1,1,1,128)
print(output.size())
print("DECODING...")
output = d(output)