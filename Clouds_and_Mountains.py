#### ======= HW4 template ======= ####
#Eesha Jain
''' This program draws clouds and mountains and allows the user to draw a house, move the clouds
and change the views (morning, noon, and evening) as well as adjust the speed of the clouds'''
#grade on project: 100%

from graphics import *
from time import *
import math
import random


# draw cloud on the left and right side of the sky based on the points using function. this function should return alist of circles.
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

def move_cloud(Speed, cloud1, cloud2):
    for i in cloud1: 
        i.move(Speed, 0)
        sleep(.1)
    for i in cloud2:
        i.move(Speed, 0)
        sleep(.1)
    
 

# draw the trunk of the tree with two points as a rectangle, calculate the circle above the tree trunk.
def draw_house_body(win, p1, p2):
    # drawing rectangle as house body.
    house_body = Rectangle(p1,p2)
    house_body.setFill("red")
    house_body.draw(win)
    return house_body
    
def draw_house(win,p1,p2,p3):
    # finding width and height of the rectangle.
    width = (p2.x - p1.x)
    height = (p2.y - p1.y)
    
    # finding the points for the roof polygon.
    r1 = Point(p1.x, p2.y)
    r2 = Point(p1.x+width/3, p3.y)
    r3 = Point(p2.x+width/3, p3.y)
    roof = Polygon(r1,r2,r3,p2)
    roof.setFill(color_rgb(100,0,0))
    # drawing the roof
    roof.draw(win)
    # draw the front polygon
    f1 = Point(p2.x+2*(width/3),p2.y)
    f2 = Point(p2.x+2*(width/3),p1.y)
    f3 = Point(p2.x,p1.y)
    face = Polygon(p2,r3,f1,f2,f3)
    face.setFill("pink")
    face.draw(win)
    # hint : for x values of the roof, add p1.x and p2.x by (width/3)
    return roof, face
    
    
def main():

    # Initializing Speed
    Speed = 0.4

    # creating the graphic window
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
    cloud1 = draw_cloud(win, 5,10,20,21)
  
    # === call draw_cloud function for the right side of the sky ===
    cloud2 = draw_cloud(win, 24,29,22,23)

    # === set text for asking user to click a point ===
    pntMsg = Point(20, 29)
    txtMsg = Text(pntMsg, "Please click the left bottom point of the house.")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("red")
    txtMsg.draw(win)
    
    # === get the lower point from user ===
    p1 = win.getMouse()
    p1.draw(win)
    p1.setFill("brown")
    
    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the upper right point of the house.")
    
    # === get the upper point from user ===
    p2 = win.getMouse()
    p2.draw(win)
    p2.setFill("brown")
    # TODO: get point p2
    
    # === call function to draw the house body ===
    m3 = draw_house_body(win, p1, p2)

    # === change the text to ask user to click another point ===
    txtMsg.setText("Now click the roof top point of the house.")
    # === get the roof top point from user ===
    
    # TODO: get point p3
    p3 = win.getMouse()
    # === call function to draw the roof and front of the house ===
    draw_house(win, p1, p2, p3)

    # === change the text inside text box ===
    txtMsg.setText("Please click a button.")

    # === View button ===
    button_1 = Rectangle(Point(2,3), Point(6, 5))
    button_1.setFill("yellow")
    button_1.draw(win)
    ViewMsg = Text(Point(4, 4), "Views")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)

    # === Wind buttton ===
    button_2 = Rectangle(Point(7,3), Point(11, 5))
    button_2.setFill("yellow")
    button_2.draw(win)
    ViewMsg = Text(Point(9,4), "Wind")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)  

    # TODO: details of button 2

    
    # === Speed Button ===
    button_3 = Rectangle(Point(12,3), Point(16, 5))
    button_3.setFill("Yellow")
    button_3.draw(win)
    speed_string = ("Speed", '(', str(Speed), ")")
    ViewMsg = Text(Point(14,4), speed_string)
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)

    # TODO: details of button 3



    # === Exit Button ===
    button_4 = Rectangle(Point(17,3), Point(21, 5))
    button_4.setFill("grey")
    button_4.draw(win)
    ViewMsg = Text(Point(19,4), "Exit")
    ViewMsg.setStyle("bold")
    ViewMsg.setTextColor("black")
    ViewMsg.draw(win)

    click = win.getMouse()
    while True:
        count = 0
        #click = win.getMouse()
        if(click.x >= 17 and click.x <= 21 and click.y >= 3 and click.y <= 5):
            break
        
        elif(click.x >= 7 and click.x <= 11 and click.y >=3 and click.y <= 5 ):
            times = 1
            while(times <= 4):
                move_cloud(Speed, cloud1, cloud2)
                times += 1
            click = win.getMouse()

        # Check views
        if(click.x >= 2 and click.x <= 6 and click.y >= 3 and click.y <= 5 and count == 0):
            BackGround.setFill(color_rgb(3,248,252))
            for i in cloud1:
                i.setFill('grey')
                i.setOutline('grey')
            for i in cloud2:
                i.setFill('grey')
                i.setOutline('grey')
            sun.setFill(color_rgb(252, 61, 3))
            sun.setOutline(color_rgb(252, 61, 3))
            txtMsg.setText('Noon')
            count += 1 
            click = win.getMouse()
        #Evening View
        if(click.x >= 2 and click.x <= 6 and click.y >= 3 and click.y <= 5 and count == 1):
            BackGround.setFill('dark blue')
            sun.setFill('dark blue')
            sun.setOutline('dark blue')
            txtMsg.setText('Evening')
            count += 1
            click = win.getMouse()

        #Goes back to normal view
        if(click.x >= 2 and click.x <= 6 and click.y >= 3 and click.y <= 5 and count == 2):
            sun.setFill('Yellow')
            sun.setOutline('Yellow')
            BackGround.setFill('light blue')
            for i in cloud1:
                i.setFill('white')
                i.setOutline('white')
            for i in cloud2:
                i.setFill('white')
                i.setOutline('white')
            txtMsg.setText('Please click a button to change views')
            click = win.getMouse()
            count = 0
        #changes speed button
        elif(click.x >= 12 and click.x <= 16 and click.y >=3 and click.y <= 5 ):  
            Speed += 0.3   
            button_3 = Rectangle(Point(12,3), Point(16, 5))
            button_3.setFill("Yellow")
            button_3.draw(win)
            speed_string = ("Speed", '(', str(Speed), ")")
            ViewMsg = Text(Point(14,4), speed_string)
            ViewMsg.setStyle("bold")
            ViewMsg.setTextColor("black")
            ViewMsg.draw(win)
            click = win.getMouse() 
            
                
    txtMsg.setText("Good Bye!")
    win.close()
    

main()
