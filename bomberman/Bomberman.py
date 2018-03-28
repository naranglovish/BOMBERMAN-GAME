import Config
import os
import sys

class Bomberman(object):			# class bomberman
	def __init__(self):

		self.x=2
		self.y=4

		Config.Matrix = [[' ' for x in range(Config.w)] for y in range(Config.h)] #initializing the board 
		for i in range(0,2):
			for j in range(0,4):
				Config.Matrix[self.x+i][self.y+j]='B'   
	

		
	def bombermanmove(self,t):
			
			
		if t=='w':                                                                        #key input
			if Config.Matrix[self.x-1][self.y]=='E' or Config.Matrix[self.x-1][self.y]=='*': # checking for enemy and bomb
				Config.lives-=1								# lose life when you encounter bomb or enemy
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')						# exit the game if you lose all the lives
					exit(0)										
				self.x=2
				self.y=4
				

	# checking if the block above is empty  
			elif Config.Matrix[self.x-1][self.y]!='X' and Config.Matrix[self.x-1][self.y]!='E' and Config.Matrix[self.x-1][self.y]!='/' and Config.Matrix[self.x-1][self.y]!=str(3) and Config.Matrix[self.x-1][self.y]!=str(2)and Config.Matrix[self.x-1][self.y]!=str(1):  
				self.x=self.x-2 #if it is empty it will move above    			


				

		if t=='a':
			if Config.Matrix[self.x][self.y-1]=='E' or Config.Matrix[self.x][self.y-1]=='*':# checking for enemy and bomb
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				self.x=2
				self.y=4
				
			
			elif Config.Matrix[self.x][self.y-1]!='X' and Config.Matrix[self.x][self.y-1]!='E' and Config.Matrix[self.x][self.y-1]!='/' and Config.Matrix[self.x][self.y-1]!=str(3) and Config.Matrix[self.x][self.y-1]!=str(2) and Config.Matrix[self.x][self.y-1]!=str(1):  
				self.y=self.y-4 #updating if left block is empty 

		if t=='d':
			if Config.Matrix[self.x][self.y+4]=='E' or Config.Matrix[self.x][self.y+4]=='*':
				Config.lives-=1
				if Config.lives==0:
					os.system('clear')
					print('YOU LOST')
					exit(0)
				self.x=2
				self.y=4

		
			elif Config.Matrix[self.x][self.y+4]!='/' and Config.Matrix[self.x][self.y+4]!='E' and Config.Matrix[self.x][self.y+4]!='X' and Config.Matrix[self.x][self.y+4]!=str(3) and Config.Matrix[self.x][self.y+4]!=str(2) and Config.Matrix[self.x][self.y+4]!=str(1):        
				self.y=self.y+4#updating if right block is empty

		if t=='s':

			if Config.Matrix[self.x+2][self.y]=='E' or Config.Matrix[self.x+2][self.y]=='*':
				Config.lives-=1
				if Config.lives==0:
					os.system("clear")
					print('YOU LOST')
					exit(0)
				self.x=2
				self.y=4

				
			elif Config.Matrix[self.x+2][self.y]!='X' and Config.Matrix[self.x+2][self.y]!='E' and Config.Matrix[self.x+2][self.y]!='/' and Config.Matrix[self.x+2][self.y]!=str(3) and Config.Matrix[self.x+2][self.y]!=str(2) and Config.Matrix[self.x+2][self.y]!=str(1):
				self.x=self.x+2;#updating if down block is empty
				
				

								



	