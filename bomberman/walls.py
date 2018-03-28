import Config
class Walls(object):
	def wall(self):
		for i in range(0,Config.w):  # the  upper and lower boundry
			Config.Matrix[0][i]='X'
			Config.Matrix[1][i]='X'
			Config.Matrix[40][i]='X'
			Config.Matrix[41][i]='X'
		for i in range(0,Config.h): # the side boundries
			Config.Matrix[i][0]='X'
			Config.Matrix[i][1]='X'
			Config.Matrix[i][2]='X'
			Config.Matrix[i][3]='X'
			Config.Matrix[i][80]='X'
			Config.Matrix[i][81]='X'
			Config.Matrix[i][82]='X'
			Config.Matrix[i][83]='X'
		Config.count,Config.count1=-1,-1
	#	print (Config.count ,Config.count1)
		for i in range(4,38):# the inner walls unbreakable 
			
			if (i)%2==0:
				Config.count=Config.count+1  # to ensure they leave one block gap in y direction 
				if Config.count%2==0:     
					for j in range(8,80):
						if j%2==0:
							Config.count1=Config.count1+1
							#print(Config.count1)
							if Config.count1%4==0: # to ensure they leave one block (4 gap) 
								 
								Config.Matrix[i][j]='X'
								Config.Matrix[i+1][j]='X'
								Config.Matrix[i][j+1]='X'
								Config.Matrix[i+1][j+1]='X'
								Config.Matrix[i][j+2]='X'
								Config.Matrix[i+1][j+2]='X'
								Config.Matrix[i][j+3]='X'
								Config.Matrix[i+1][j+3]='X'

