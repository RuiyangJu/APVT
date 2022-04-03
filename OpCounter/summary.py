import torch
from thop import profile
from torchvision.models import resnet18

input = torch.randn(1, 3, 32, 32)
model = resnet18()
macs, params = profile(model, inputs=(input, ))

print('macs:')
print(macs)

print('params:')
print(params)