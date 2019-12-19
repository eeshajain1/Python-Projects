# -*- coding: utf-8 -*-
'''
Eesha Jain
#78529929


Created on Mon Nov 11 14:58:36 2019

@author: Shima Nabiee
'''
from graphics import *
from time import *
import random
import math
import os

btamt = 0

class balloon(Circle):
	def __init__(self , win , center , radius):

		self.win = win
		Circle.__init__(self, center , radius)
		
		#self.draw_balloons()

		# speed and score generator
		self.speed_scoreGen()

		

	def draw_balloons(self):

		
		# drawing cirecle
		
		center = [(self.p1.x + self.p2.x)/2 , (self.p1.y + self.p2.y)/2]
		#radius = (self.p2.x - self.p1.x)/2
		
		R = random.randint(0,255)
		B = random.randint(0,255)
		G = random.randint(0,255)
		Circle.setFill(self,color_rgb(R, G, B))
		Circle.draw(self, self.win)
		self.balloon_line = Line(Point(self.getCenter().x, self.getCenter().y - self.getRadius()), 
			Point(self.getCenter().x, self.getCenter().y - 3*self.getRadius()))
		self.balloon_line.draw(self.win)


		#balloon_line = line(self.)
		
		# drawing line (string of the balloon)
		


	def speed_scoreGen(self):
		self.speed = 0.1 + random.random()
		self.score = round(self.speed * 100)
		

		# Randomly creating speed and score of the balloon


	def getXY(self):
		return Point((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2)

		# Getting center of the circle
		


	def move_balloons(self):
		Circle.move(self, 0, self.speed)
		self.balloon_line.move(0, self.speed)
		sleep(0.05)
	

		# Move balloon and its string
		

	def is_hit(self , pClick):
		dist_x = self.getXY().x - pClick.x
		dist_y = self.getXY().y - pClick.y
		total_dist = math.sqrt(dist_x**2 + dist_y**2)
		return total_dist <= (self.getRadius())

		# Checking if the clicked point is inside the ballooon circle

	def getScore(self):
		return self.score
		# return the score of the balloon

	def undraw_balloons(self):
		Circle.undraw(self)
		self.balloon_line.undraw()
		# Undraw balloons and strings



class bug:
	def __init__(self , win):
		self.win = win
		# Cerate a random point forthe center of the bugs
		self.bug_center = Point(random.randrange(1,30),random.randrange(1,30))
		self.BugSpeedX , self.BugSpeedY = 0.3 , 0.5

	def loadGIF(self , img ):
		self.Buggie = Image(self.bug_center, img)
		self.Buggie.draw(self.win)
	

		# load the image and draw it


	def move_bug(self):

		bug_center = self.Buggie.anchor
		
		# Checking X
		if bug_center.x <= 1:
			BspeedX = self.BugSpeedX
		elif bug_center.x >= 30:
			BspeedX = -self.BugSpeedX
		else:
			BspeedX = ( (math.ceil( 0.5 - random.random() ) * 2) - 1 ) *self.BugSpeedX

		# Add the code to check Y
		if bug_center.y <= 1:
			BspeedY = self.BugSpeedX
		elif bug_center.y >= 30:
			BspeedY = -self.BugSpeedX
		else:
			BspeedY = ( (math.ceil( 0.5 - random.random() ) * 2) - 1 ) *self.BugSpeedX

		self.Buggie.move(BspeedX, BspeedY)

		# Move the bug based on speed

	def undraw_bug(self):
		self.Buggie.undraw()
		# Undraw bug

	def bug_hit(self, pClick):

		# Checking whether the clicked point is inside the bug image
		# You can consider the bug like a circle with radius 1
		#bug_center = self.Buggie.anchor

		anchor_offset = .5
		dist_x = (self.Buggie.anchor.x - anchor_offset) - pClick.x
		dist_y = (self.Buggie.anchor.y + anchor_offset) - pClick.y
		
		total_dist = math.sqrt((dist_y*dist_y) + (dist_x*dist_x))

		if total_dist <= 1:
			return True
		else:
			return False
		
		





def draw_cloud(win, x1,x2,y1,y2):
    cloud_list = []
    for i in range(11):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        p = Point(x,y)

        cloud = Circle(p,2)
        cloud.setFill("white")
        cloud.setOutline("white")
        cloud.draw(win)
        cloud_list.append(cloud)
    return cloud_list


def backGround():
    win = GraphWin("Blue sky and green field!", 800, 600)
    win.setCoords(0, 0, 40, 30)

    # set the background color  (width is 40, height is 30)
    BackGround = Rectangle(Point(0,15), Point(40, 30))
    BackGround.setFill("light blue")
    BackGround.draw(win)

    # set the Ground color
    Ground = Rectangle(Point(0,0) , Point(40, 15))
    Ground.setFill("light Green")
    Ground.draw(win)

    # draw the sun
    sun = Circle(Point(20,25), 2)
    sun.setFill("Yellow")
    sun.setOutline("Yellow")
    sun.draw(win)

    # draw the mountain1
    Mountain1 = Polygon(Point(0,15), Point(15, 28), Point(30,15))
    Mountain1.setFill("dark green")
    Mountain1.draw(win)

    # draw the mountain2
    Mountain2 = Polygon(Point(10,15), Point(23,26), Point(40,15))
    Mountain2.setFill("dark green")
    Mountain2.draw(win)

    # === call draw_cloud function for the left side of the sky ===
    m1 = draw_cloud(win, 5,10,20,21)
  
    # === call draw_cloud function for the right side of the sky ===
    m2 = draw_cloud(win, 24,29,22,23)

    # === set text for asking user to click a point ===
    pntMsg = Point(20, 29)
    txtMsg = Text(pntMsg, "Please click on one of the balloon.")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("red")
    txtMsg.draw(win)

    return win

def buttons(win):

    button_1 = Rectangle(Point(2,3), Point(6, 5))
    button_1.setFill("yellow")
    button_1.draw(win)
    ViewMsg = Text(Point(4, 4), "Start")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)
    
    # === stop buttton ===
    button_2 = Rectangle(Point(7,3), Point(11, 5))
    button_2.setFill("yellow")
    button_2.draw(win)
    colorMsg = Text(Point(9, 4), "Exit")
    colorMsg.setStyle("bold")
    colorMsg.setTextColor("black")
    colorMsg.draw(win)
    
    # === Betamount Entry === #
    button_3 = Rectangle(Point(12,3), Point(16,5))
    button_3.setFill("white")
    button_3.draw(win)
    betMsg = Text(Point(14,6), "Bet $:")
    betMsg.setTextColor("black")
    betMsg.draw(win)
    # Add bet amount using Entry class
    btamt = Entry(Point(14,4), 2)
    btamt.setFill("grey")
    btamt.draw(win)


    return button_1, button_2, button_3 , btamt


def main():

	# creating BG and Buttons
	win = backGround()
	button_1, button_2, button_3 , btamt = buttons(win)


	# Number of times user clicked on "start" button
	count = 0
	# Checking whether the game is started yet or not
	restart = 0

	# balance and number of timesare hitted balloons
	balance = 0
	BL_click_count = 0
	balMsg = Text(Point(18,4), 'Balance $:')
	balMsg.setStyle("bold")
	balMsg.setTextColor('blue')
	balMsg.draw(win)
	bet = Text(Point(21,4), '')
	bet.setStyle("bold")
	bet.setTextColor('blue')
	bet.draw(win)
	while True:

		# waiting for user to clock on "start" button for the first time
		if restart == 0:
			p_B = win.getMouse()
		else:
			p_B = pClick

		# Checking click on exit button
		if p_B.x > button_2.p1.x and p_B.y > button_2.p1.y and p_B.x < button_2.p2.x and p_B.y < button_2.p2.y:
			break

		# Checking click on start button
		elif p_B.x > button_1.p1.x and p_B.y > button_1.p1.y and p_B.x < button_1.p2.x and p_B.y < button_1.p2.y:
			balance = 0
			bet.setText('')	
			#if count is 1, then we need to undraw everything and draw them again.
			# otherwise we just need to set count to 1 and draw from beginning.
			if count == 1:
				for BL in BL_list:
					BL.undraw_balloons()
				Buggie.undraw_bug()
				bet.undraw()
				balMsg.undraw()


				Balloons_No = random.randint(5,10)
				BL_list		= []
				for i in range(Balloons_No):
					# Generate random x,y
					x,y = random.randrange(0,40),random.randrange(0,30)
					r = random.randrange(2,5)
					# use balloon class and create BL_list which a list of balloon class objects
					BL_list.append(balloon(win, Point(x,y), r))
				for BL in BL_list:
					BL.draw_balloons()
				# Draww bug using bug class
				Buggie = bug(win)
				Buggie.loadGIF("bug.gif")

				bet.draw(win)
				balMsg.draw(win)
			
			else:
			# Randomly creating number of balloons
				Balloons_No = random.randint(5,10)
				BL_list		= []
				for i in range(Balloons_No):
					# Generate random x,y
					x,y = random.randrange(0,40),random.randrange(0,30)
					r = random.randrange(2,5)
					# use balloon class and create BL_list which a list of balloon class objects
					BL_list.append(balloon(win, Point(x,y), r))
				for BL in BL_list:
					BL.draw_balloons()
				# Draww bug using bug class
				Buggie = bug(win)
				Buggie.loadGIF("bug.gif")
	
				count = 1
		
			while True:
				for BL in BL_list:
					# Move balloon and bug
					Buggie.move_bug()
					BL.move_balloons()
					
				sleep(0.05)

				# Waiting for the click`	
				pClick = None
				while  pClick == None:
					pClick = win.checkMouse()
					for BL in BL_list:
						BL.move_balloons()
						Buggie.move_bug()
					sleep(0.05)

				# Checking if Bug is hitted
				if Buggie.bug_hit(pClick):
					
					if btamt.getText() == '':
						betAmount = 1
					else:
						betAmount = int(btamt.getText())

					balance += 5 * betAmount

					# Undraw bug
					Buggie.undraw_bug()

					# Display remaining balance
					bet.setText(balance)

				#checking if a balloon is hitted
				for BL in BL_list:
					if BL.is_hit(pClick):
						# undraw hitted balloon and use pop(i) to remove it from the list
						BL.undraw_balloons()
						BL_list.remove(BL)
						
				
					# randomly generate 1 or -1 to decide whether you lose money or win
						random01 = random.randint(0, 2)
						randomNum = 1
						if (random01 == 0):
							randomNum = -1
						elif (random01 == 1):
							randomNum = 1;
						print(randomNum)

						Balloons_No -= 1
						balloon_score = BL.getScore()*randomNum
						# Display remaining balance
						balance += (balloon_score)
						bet.setText(balance)

				# Checking start and exit button
				if pClick.x > button_2.p1.x and pClick.y > button_2.p1.y and pClick.x < button_2.p2.x and pClick.y < button_2.p2.y:
					win.close()
					os._exit(0)

				elif pClick.x > button_1.p1.x and pClick.y > button_1.p1.y and pClick.x < button_1.p2.x and pClick.y < button_1.p2.y:
					restart = 1
					break



	win.close()
	os._exit(0)



if __name__ == '__main__':
    main()