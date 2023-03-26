class Bullet:

    #I was getting attribute errors.
    posX = 0
    posY = 0
    orientation = 0

    #Creates a new instance of Bullet
    def __init__(self, posX, posY, orientation):
        self.orientation = orientation
        if orientation == 0:
            self.posY = posY + 1
        elif orientation == 1:
            self.posX = posX + 1
        elif orientation == 2:
            self.posY = posY - 1
        elif orientation == 3:
            self.posX = posX - 1
        print("pow") #debug code
    
    #Bullet travels per frame. Use in the main while loop
    def bulletTravel(self):
        if self.orientation == 0:
            self.posY += 1
        elif self.orientation == 1:
            self.posX += 1
        elif self.orientation == 2:
            self.posY -= 1
        elif self.orientation == 3:
            self.posX -= 1

    def getPosX(self):
        return self.posX
    
    def getPosY(self):
        return self.posY
    
    def getOrientation(self):
        return self.orientation
