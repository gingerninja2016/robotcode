#Robot program by Saurabh Sakpal

class Location:
    #constructor that initialises the robot
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    #function to report the robot's current location and direction
    def Report(self):
        directionReport = self.direction
        directionReport = directionReport.upper()
        print("Output X Y is:", self.x, self.y, directionReport)
    
    #functon to shift robot direction left relative to direction they are facing
    def changedirectionLeft(self):

        if self.direction == "south":
            self.direction = "east"
        elif self.direction == "north":
            self.direction = "west"
        elif self.direction == "east":
            self.direction = "north"
        elif self.direction == "west":
            self.direction = "south"
            
    #function to shift robot direction right relative to direction they are facing
    def changedirectionRight(self):
    
        if self.direction == "south":
            self.direction = "west"
        elif self.direction == "north":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "south"
        elif self.direction == "west":
            self.direction = "north"
    
    #function to move robot 1 step in direction they are facing
    def Move(self):
        self.x = int(self.x)
        self.y = int(self.y)
        
        if self.direction == "north" and self.y < 5:
            self.y = self.y + 1
        elif self.direction == "west" and self.x > 0:
            self.x = self.x -1
        elif self.direction == "south" and self.y > 0:
            self.y = self.y - 1
        elif self.direction == "east" and self.x < 5: 
            self.x = self.x + 1
        else:
            print("Robot is going out of grid cant be moved, try again")
    
    #function to give the robot a new place and direction
    def Place(self):
        print("Enter New Coordinates")
        self.x = input(f"Enter x :")
        self.y = input(f"Enter y :")
        self.x = int(self.x)
        self.y = int(self.y)
        if self.x <  0 or self.x > 5 or self.y < 0 or self.y > 5:
            print("Robot is out of grid cant be placed")
        else:
            print("Place is X Y: ", self.x, " ", self.y)


#This is the initial script that runs when program is run from command line \
#It involves initialising the robot's co-ordinates and running the respective commands \
#The commands are Place, Move, Left, Right and Report

x=input(f"Enter X : ")
y=input(f"Enter Y : ")
direction=input(f"Enter direction : ")
direction = direction.lower()
if int(x)>5 or int(x)< 0 or int(y)> 5 or int(y)<0:
    print("Robot placed out of grid start again")
elif direction!= "west" and direction!= "east" and direction!= "north" and direction!="south":
    print("Invalid Direction, Direction has to be North, South, East or West start program again")
else:
    directionUpper = direction.upper()
    print("Place is X Y: ", x, " ", y, " ", directionUpper)

#initialise the robots co ordinates via constructing the Location class and creating object robot 
robot = Location(x,y, direction)

#flag to keep prompting input at user interface/terminals
flagv= 1
while flagv!= 0:

    commandrobot = input()
    commandrobot = commandrobot.lower()
    if commandrobot == "place":
        robot.Place()
    elif commandrobot == "move":
        robot.Move()
    elif commandrobot == "left":
        robot.changedirectionLeft()
    elif commandrobot == "right":
        robot.changedirectionRight()
    elif commandrobot == "report":
        robot.Report()
    else:
        flagv=0
    






