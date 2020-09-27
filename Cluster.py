from Hexagon import Hexagon
import itertools

class Cluster:
    def __init__(self, name, hexagon):
        self.name = name
        self.hexagons = {}
        self.hexagons[hexagon.name] = hexagon

    def queryNeighbours(self, name):
        if name not in self.hexagons:
            return 'Hexagon '+name+' does not exists in cluster '+self.name

        hexagon = self.hexagons[name]
        ans = []
        for i in range(6):
            if hexagon.neighbours[i]!=None:
                ans.append((i, hexagon.neighbours[i].name))
        return str(ans)



    def addHexagon(self, name, neighbour, index):
        if name in self.hexagons:
            return 'Hexagon '+name+' already exists in cluster '+self.name

        if self.hexagons[neighbour].neighbours[index]!=None:
            return 'Could not add Hexagon '+name+' in cluster '+self.name

        newHex = Hexagon(name)
        self.hexagons[name] = newHex
        self.hexagons[neighbour].makeConnection(index, newHex)
        return 'Hexagon '+name + ' successfully added in cluster '+self.name



    def isConnected(self, hex1, hex2):

        trav = set()
        def DFS(curr):
            if curr==hex2:
                return True

            trav.add(curr.name)
            ans = False
            for i in range(6):
                if curr.neighbours[i]!=None and curr.neighbours[i].name not in trav:
                    ans = ans or DFS(curr.neighbours[i])
                    if ans:
                        return ans
            return ans

        return DFS(hex1)





    def removeHexagon(self, name):
        if name not in self.hexagons:
            return 'Hexagon '+name+' does not exists in cluster '+self.name

        hexagon = self.hexagons[name]
        connections = []
        for i in range(6):
            if hexagon.neighbours[i]!=None:
                nei = hexagon.neighbours[i]
                connections.append(nei)
                if i==0:
                    nei.neighbours[3] = None

                elif i==1:
                    nei.neighbours[4] = None

                elif i==2:
                    nei.neighbours[5] = None

                elif i==3:
                    nei.neighbours[0] = None

                elif i==4:
                    nei.neighbours[1] = None

                else:
                    nei.neighbours[2] = None
            else:
                connections.append(None)




        removable = True
        for a, b in itertools.combinations([0,1,2,3,4,5], 2):
            if hexagon.neighbours[a]!=None and hexagon.neighbours[b]!=None:
                if self.isConnected(hexagon.neighbours[a], hexagon.neighbours[b]):
                    pass
                else:
                    removable = False
                    break

        if removable:
            del self.hexagons[name]
            del hexagon
            return 'Hexagon '+name+' successfully removed from cluster '+self.name
        else:
            for i in range(6):
                hexagon.neighbours[i] = None

            for i in range(6):
                if connections[i]!=None:
                    hexagon.makeConnection(i, connections[i])

            return 'Could not remove Hexagon '+name+' from cluster '+self.name
            
