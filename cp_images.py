import glob
from glob import glob
import os


im_flnames = glob('/nobackupp2/gfsnyder/VELA_sunrise/Runs/VELA_v2/*_a0.350_sunrise/images/images_*_a0.350_sunrise.tar')

for fl in im_flnames:
    print fl


