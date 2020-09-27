class Hexagon:
    def __init__(self, name):
        self.name = name
        self.neighbours = [None]*6

    def makeConnection(self, index, other):
        if self.neighbours[index]!=None:
            return


        self.neighbours[index] = other
        if index==0:
            other.neighbours[3] = self
            if self.neighbours[5]!=None:
                self.neighbours[5].makeConnection(1, other)
            if self.neighbours[1]!=None:
                self.neighbours[1].makeConnection(5, other)

        elif index==1:
            other.neighbours[4] = self
            if self.neighbours[0]!=None:
                self.neighbours[0].makeConnection(2, other)
            if self.neighbours[2]!=None:
                self.neighbours[2].makeConnection(0, other)

        elif index==2:
            other.neighbours[5] = self
            if self.neighbours[1]!=None:
                self.neighbours[1].makeConnection(3, other)
            if self.neighbours[3]!=None:
                self.neighbours[3].makeConnection(1, other)

        elif index==3:
            other.neighbours[0] = self
            if self.neighbours[2]!=None:
                self.neighbours[2].makeConnection(4, other)
            if self.neighbours[4]!=None:
                self.neighbours[4].makeConnection(2, other)


        elif index==4:
            other.neighbours[1] = self
            if self.neighbours[3]!=None:
                self.neighbours[3].makeConnection(5, other)
            if self.neighbours[5]!=None:
                self.neighbours[5].makeConnection(3, other)

        else:
            other.neighbours[2] = self
            if self.neighbours[4]!=None:
                self.neighbours[4].makeConnection(0, other)
            if self.neighbours[0]!=None:
                self.neighbours[0].makeConnection(4, other)



                
