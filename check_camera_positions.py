import numpy as np
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.close('all')


rundir = '/nobackupp2/gfsnyder/VELA_sunrise/Runs/VELA_v2/VELA28'


cam_files = glob.glob(rundir+'/*/input/*cameras')


fig = figure(figsize = (30,5))


for i, name in enumerate(cam_files[0:10]):
	print name
	ax = fig.add_subplot(1,10,i+1, projection='3d')

	data = np.loadtxt(name)
	for j in arange(len(data[:,0]))
		ax.plot([0,0,0], [data[j, 0], data[j,1],data[j,2]],'k-')


savefig('test.png', dpi = 200)

plt.close('all')
