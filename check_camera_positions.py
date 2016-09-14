import numpy as np
import glob

rundir = '/nobackupp2/gfsnyder/VELA_sunrise/Runs/VELA_v2/VELA28'


cam_files = glob.glob(rundir+'/*/input/*cameras')

for i, name in enumerate(cam_files):
	print name