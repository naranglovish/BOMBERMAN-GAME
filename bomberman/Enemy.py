import Config
import os
import random
class Enemy(object):
	def __init__(self):
		
		C=random.randrange(4,Config.h-5)
		D=random.randrange(4,Config.w-7)	

		while(True):  
			C=random.randrange(4,Config.h-5)
			D=random.randrange(4,Config.w-7)
			if D%4==0 and C%2==0  and Config.Matrix[C][D]!='B'  and Config.Matrix[C][D]!='X' and Config.Matrix[C][D]!='/' and Config.Matrix[C][D]!='E':
				break
			# findind the random x and y empty coordinate to place the enemy
		self.x=C
		self.y=D

		for i in range(0,2): 
			for j in range(0,4):
										# placing the enemy in board
				Config.Matrix[C+i][D+j]='E'
				


	def movement(self):

		u=random.randrange(0,4) # finding the random number between 0 and 4 
		# if u==0 then enemy will move up if block is empty
		# if u==1 then enemy will move one block right if it is empty
		# if u==2 then enemy will move one block down if it is empty
		#if u==3 then enemy will move one block left if it is empty
		
		if u==0:
			if Config.Matrix[self.x-2][self.y]!='X'  and Config.Matrix[self.x-2][self.y]!='/' and Config.Matrix[self.x-2][self.y]!='E' and Config.Matrix[self.x-2][self.y]!='B' and Config.Matrix[self.x-2][self.y]!=str(3) and Config.Matrix[self.x-2][self.y]!=str(2) and Config.Matrix[self.x-2][self.y]!=str(1):
				self.x=self.x-2#checking if palce is empty
			elif Config.Matrix[self.x-2][self.y]=='B':# if enemy encounters bomberman , bomberman bomber loses its life
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				return 100
				
		elif u==1:
			if  Config.Matrix[self.x][self.y+4]!='/'  and Config.Matrix[self.x][self.y+4]!='X' and Config.Matrix[self.x][self.y+4]!='E' and Config.Matrix[self.x][self.y+4]!='B' and Config.Matrix[self.x][self.y+4]!=str(3) and Config.Matrix[self.x][self.y+4]!=str(2) and Config.Matrix[self.x][self.y+4]!=str(1):
				self.y=self.y+4#checking place 
			elif Config.Matrix[self.x][self.y+4]=='B':# # if enemy encounters bomberman , bomberman bomber loses its life
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				return 100

				
							
		elif u==2:
			if  Config.Matrix[self.x+2][self.y]!='B'  and Config.Matrix[self.x+2][self.y]!='X' and Config.Matrix[self.x+2][self.y]!='E' and Config.Matrix[self.x+2][self.y]!='/' and Config.Matrix[self.x+2][self.y]!=str(2) and Config.Matrix[self.x+2][self.y]!=str(3) and Config.Matrix[self.x+2][self.y]!=str(1) :
				self.x=self.x+2#checking place
				
			elif Config.Matrix[self.x+2][self.y]=='B':# if enemy encounters bomberman , bomberman bomber loses its life
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				return 100
			

		elif u==3:
			if Config.Matrix[self.x][self.y-4]!='B'  and Config.Matrix[self.x][self.y-4]!='X' and Config.Matrix[self.x][self.y-4]!='E' and Config.Matrix[self.x][self.y-4]!='/' and Config.Matrix[self.x][self.y-4]!=str(3) and Config.Matrix[self.x][self.y-4]!=str(2) and Config.Matrix[self.x][self.y-4]!=str(1):
				self.y=self.y-4# checking place
				
			elif Config.Matrix[self.x][self.y-4]=='B':# if enemy encounters bomberman , bomberman bomber loses its life
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				return 100
			
