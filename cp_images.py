import glob
from glob import glob
import os

a = '0.350'
im_flnames = glob('/nobackupp2/gfsnyder/VELA_sunrise/Runs/VELA_v2/VELA*/*_a%s_sunrise/images/images_*_a%s_sunrise.tar'%(a,a))

for n, fl in enumerate(im_flnames):
    print n, fl


