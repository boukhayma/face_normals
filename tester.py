import torch
from torch.autograd import Variable
from torchvision.transforms import Compose, ToTensor
from resnet_unet import ResNetUNet
import cv2
import numpy as np
from PIL import Image

img_transform = Compose([
  ToTensor()
])

model = ResNetUNet(n_class = 3).cuda()
model.load_state_dict(torch.load('data/model.pth'))
                                               
model.eval()
      
img = img_transform(Image.open('data/cropped/0.jpg')).unsqueeze(0)  
img = Variable(img.cuda())
  
outs = model(img)[0]  
out = np.array(outs[0].data.permute(1,2,0).cpu())  
out = out / np.expand_dims(np.sqrt(np.sum(out * out, 2)),2)
out = 127.5 * (out + 1.0)

cv2.imwrite('data/output/0.jpg', cv2.cvtColor(out, cv2.COLOR_RGB2BGR))
  




