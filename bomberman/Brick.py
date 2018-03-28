import random
import Config
class Bricks(object):
	def bricks(self):
		count=0
		if Config.level==1:
			total=35
		elif Config.level==2: #these are the number of bricks per level
			total=45
		elif Config.level==3:
			total=55
		
		while(True):
			if count==total:
				break
			x=random.randrange(6,Config.w-5)
			y=random.randrange(6,Config.h-5) # randomly selecting a coordinate
			
			if x%4==0 and y%2==0 and Config.Matrix[y][x]!='/' and Config.Matrix[y][x]!='E' and Config.Matrix[y][x]!='X':#checking the conditions if the postion is available
				count+=1	
				for i in range(0,2):
					for j in range(0,4):
		
						Config.Matrix[y+i][x+j]='/'
					