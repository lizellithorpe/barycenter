#/usr/bin/env python3
import numpy as np
import sys
sys.path.append('/Users/lizellithorpe/desktop/research')
from orbital_xyz import *

class CelestialBody(object):
	def __init__(self, obj='none'):
		self.obj='none'
		
	def ArrayUnpack(self, obj):	
		filename=obj+".aei"
		t,x,y,z,xv,yv,zv,m = np.loadtxt(filename,skiprows=4, unpack=True)
		self.x=x
		self.y=y
		self.z=z
		self.t=t
		self.xv=xv
		self.yv=yv
		self.zv=zv
		self.mass=m
		cart_data={"time":t,
						  "x":x,
						  "y":y,
						  "z":z,
						  "xv":xv,
						  "yv":yv,
						  "zv":zv,
						  "mass":m
			}
						
		
			
		return(cart_data)
		
	def OrbitalCalc(self,otherbodies):
		if not isinstance(otherbodies,list):
			raise TypeError("Please submit a list of strings.")
			
		if not isinstance(otherbodies[0],str):
			raise TypeError("Please submit a list of strings.")
		
		
		time_of_run=165.25e7
		data_dump_time=365250
		timesteps=np.floor(time_of_run/data_dump_time)
		timesteps=int(timesteps)+2
		
		num_bodies=len(otherbodies)
		weights=np.empty(num_bodies)
		cm=np.zeros((3,timesteps))
		print(cm.shape)
		vcm=np.zeros((3,timesteps))
		for i in range(num_bodies):
			tb,xb,yb,zb,xvb,yvb,zvb,mb = np.loadtxt(otherbodies[i],skiprows=4, unpack=True)
			print(mb.shape)
			if tb.size < timesteps:
				append_zeros=timesteps-tb.size
				xb=np.append(xb,np.zeros(append_zeros))
				yb=np.append(yb,np.zeros(append_zeros))
				zb=np.append(zb,np.zeros(append_zeros))
				mb=np.append(mb,np.zeros(append_zeros))
				print(mb.shape,otherbodies[i])
				
				xvb=np.append(xvb,np.zeros(append_zeros))
				yvb=np.append(yvb,np.zeros(append_zeros))
				zvb=np.append(zvb,np.zeros(append_zeros))
			#weight coords
			cart_pos=[[xb],[yb],[zb]]
			cart_vel=[[xvb],[yvb],[zvb]]
			
			
			weights[i]=mb[0]
			print('finished!')
			cm=cm+mb*cart_pos
			vcm=vcm+mb*cart_vel
			
		return(cart_pos)
			
			
		
	
				


binarydat=CelestialBody(obj="BINARY")
binarydat.obj="BINARY"
print(binarydat.obj)
otherbodies= ["PLANET1.aei","PLANET2.aei"]



print(binarydat.OrbitalCalc(otherbodies))
					
				
				
		