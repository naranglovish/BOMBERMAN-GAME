import Config
import os
import time
import sys
def destroy(m): 			# functions removes the enemy if enemy is bombed
	null(Config.arr[m].x,Config.arr[m].y)
	Config.arr.remove(Config.arr[m])
	Config.score+=100

def pri(mat):			# print function it print the whole board
	os.system("clear")
	if Config.flag==1:
		for i in range(Config.pp,Config.pp+2):
				for j in range(Config.ppp,Config.ppp+4):
					mat[i][j]='e'
	
	if Config.level==1:			# print the bomb phase of level 1		
		for _ in mat:
			print("\033[1;31;40m".join(_))

		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))
	
	if Config.level==2:		# print the bomb phase of level 2
		for _ in mat:
			print("\033[1;36;40m".join(_))

		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))
	if Config.level==3:     # print the bomb phase of level 3
		for _ in mat:
			print("\033[1;37;40m".join(_))

		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))


		
def null(x,y):  # it is just the part of updating thing
	for i in range(0,2):
		for j in range(0,4):
			Config.Matrix[x+i][y+j]=' '

class Bomb(object):  #it is class of bomb  
	def __init__(self,x1,y1):   	#it is the position of bomb
		self.x=x1
		self.y=y1

	def blast(self,xcord,ycord):	# it is the funtion responsible for detonation of bomb
		Config.flag=0
		Config.time=5
		if Config.Matrix[Config.pp-1][Config.ppp]=='X':      # upper y range of bomb explosion
			aa=Config.pp
		else:
			aa=Config.pp-2
			if aa<2:
				aa=2
		if Config.Matrix[Config.pp+2][Config.ppp]=='X':		# lower y range of bomb explosion
			bb=Config.pp
		else:
			bb=Config.pp+4
			if bb>Config.h-3:
				bb=Config.h-3
		if Config.Matrix[Config.pp][Config.ppp+4]=='X':   	# right x range of bomb explosion
			cc=Config.ppp
		else:
			cc=Config.ppp+8
			if cc>Config.w-4:
				cc=Config.w-4
		if Config.Matrix[Config.pp][Config.ppp-1]=='X':		# left y range of bomb explosion
			dd=Config.ppp
		else:
			dd=Config.ppp-4
			if dd<4:
				dd=4
	
		pointer=1
		des=-1
		for i in range(aa,bb):
			for k in range(Config.ppp,Config.ppp+4):		
				if Config.Matrix[i][k]=='/':				# checking the number of bricks in between and updating the score
					Config.score+=2.5
				if Config.Matrix[xcord][ycord]==Config.Matrix[Config.pp][Config.ppp]:      #checking if bomb is placed on bomber man only
					pointer=0
				if Config.Matrix[i][k]=='B':												#checking if bomberman bombs itself
					pointer=0
				if Config.Matrix[i][k]=='E':												# checking for enemies being bombed
					

					for m in range(0,len(Config.arr)):
					# 	print (Config.arr[m].x,Config.arr[m].y,i,k)
						if Config.arr[m].x==i and Config.arr[m].y==k:						# finding which enemy is bombed
							
							des=m

				Config.Matrix[i][k]='*'
		
		for j in range(dd,cc):
			for l in range(Config.pp,Config.pp+2):
				if Config.Matrix[l][j]=='/':		# checking the number of bricks in between and updating the score
					Config.score+=2.5
				if Config.Matrix[xcord][ycord]==Config.Matrix[Config.pp][Config.ppp]:		#checking if bomb is placed on bomber man only
					pointer=0
				if Config.Matrix[l][j]=='B':		#checking if bomberman bombs itself
					pointer=0
				if Config.Matrix[l][j]=='E':     	# checking for enemies being bombed
					
										
					
					for m in range(0,len(Config.arr)):
					# 	print (Config.arr[m].x,Config.arr[m].y,j,l)
					# exit(0)	
					 	if Config.arr[m].x==l and Config.arr[m].y==j:
							des=m
				Config.Matrix[l][j]='*'     
		
		if des>-1:
			destroy(des)

			
		pri(Config.Matrix)
		time.sleep(2)

		
		if pointer==0:				#pointer ==0 -> bomberman died 
			Config.lives-=1
			if Config.lives==0:
				os.system('clear')
				print('YOU LOST')
				exit(0)
			
			
				


		for i in range(aa,bb):       #updating the matrix after explosion
			for k in range(Config.ppp,Config.ppp+4):
				Config.Matrix[i][k]=' '
		for i in range(dd,cc):
			for k in range(Config.pp,Config.pp+2):
				Config.Matrix[k][i]=' '     
		return pointer               # telling if bomberman died or not if pointer ==0 then it died

		