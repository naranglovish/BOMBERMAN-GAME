
import os
import random
import time
import signal
import termios
import Config
import Brick
import Bomberman
from Bomberman import Bomberman
import Enemy
from Enemy import Enemy
from walls import Walls
from Brick import Bricks
from Bomb import Bomb
Config.level=1
Config.power=1

Config.arr=[]

class GetchUnix:		# it is used to take input from user 
	def __init__(self):
		import tty 

	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
getch = GetchUnix()



class AlarmException(Exception):
	pass

def alarmHandler(signum, frame):
	raise AlarmException

def nonBlockingRawInput(timeout=1):			# it is asking the input and moving the  enemy after the timeout
	if Config.flag==1:
		Config.time-=1
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.alarm(timeout)
	try:    
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
		for i in range(0,len(Config.arr)):				# in exception it moves the enemy
			null(Config.arr[i].x,Config.arr[i].y)
			pp=Config.arr[i].movement()
			if pp==100:
				null(man.x,man.y)
				man.x=2
				man.y=4
				position(2,4,'B')
			position(Config.arr[i].x,Config.arr[i].y,'E')
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''



Config.w,Config.h=84,42;
Config.flag=0
Config.time=5						# assigning the global variable
Config.score=0
Config.lives=3
Config.enemy=2
Config.power=1



def null(x,y):
	for i in range(0,2):
		for j in range(0,4):
			Config.Matrix[x+i][y+j]=' '
		


def position(x,y,typ):			# updating the position of bomberman and enemy
	for i in range(0,2):
		for j in range(0,4):
			Config.Matrix[x+i][y+j]=typ
	


def pri(mat):					# print the complete board
	os.system("clear")
	if Config.flag==1:							
		for i in range(Config.pp,Config.pp+2):
				for j in range(Config.ppp,Config.ppp+4):
					mat[i][j]=str(Config.time)
	if Config.level==1:			# printing the matrix at differint levels with different colours

		for _ in mat:
			print("\033[1;32;40m".join(_))
		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))

	if Config.level==2:			# printing the matrix at differint levels with different colours

		for _ in mat:
			print("\033[1;33;40m".join(_))
		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))
	if Config.level==3:			# printing the matrix at differint levels with different colours

		for _ in mat:
			print("\033[1;38;40m".join(_))
		print('SCORE==' + str(Config.score)   + '   &  '  + ' lives=='  +str(Config.lives))

man=Bomberman()
def intial():
##framing the initial board walls bricks Bomberman and creating the enemy	     
	L=Walls()
	L.wall()
	LL=Bricks()
	LL.bricks()	


	for i in range(0,Config.enemy):	# creating the enemy
		Config.arr.append(Enemy()) 	

	os.system('clear')
	print("\033[1;32;40mlevel")
	print(Config.level)
	time.sleep(2)
	pri(Config.Matrix)

intial()

while(True):

	if Config.time==0 and Config.flag==1:   #bomb blast call the blast function
		p=B.blast(man.x,man.y)
		if p==0:
			null(man.x,man.y)
			man.x=2
			man.y=4
			position(man.x,man.y,'B')
		for i in range(Config.pp,Config.pp+2):
			for k in range(Config.ppp,Config.ppp+4):
				Config.Matrix[i][k]=' '
		pri(Config.Matrix)
			
	t=nonBlockingRawInput() 				#asking the input
	if (len(Config.arr)==0):
		if Config.level==3:
			os.system('clear')
			print('You Won')
			exit(0)
		else:
			man=Bomberman()
			Config.power+=1
			Config.level+=1
			Config.enemy+=3
			intial()
			
	
	if t=='b' and Config.flag==0:   # if bomb is placed  bomb flag is on
		Config.time=3 
		Config.flag=1
		Config.pp=man.x
		Config.ppp=man.y	
		for i in range(Config.pp,Config.pp+2):
			for k in range(Config.ppp,Config.ppp+4):
				Config.Matrix[i][k]='e'
		B=Bomb(man.x,man.y)
					
	elif t=='q':   # exit from game
		exit(0)


	elif t!='b':	
		null(man.x,man.y)
		man.bombermanmove(t)
		position(man.x,man.y,'B')
		for i in range(0,len(Config.arr)):
			null(Config.arr[i].x,Config.arr[i].y)
			pp=Config.arr[i].movement()
			if pp==100:
				null(man.x,man.y)
				man.x=2
				man.y=4
				position(2,4,'B')

			position(Config.arr[i].x,Config.arr[i].y,'E')
		
		pri(Config.Matrix)

	

	pri(Config.Matrix)

