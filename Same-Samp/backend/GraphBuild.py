from Vertex import Vertex
import math

class GraphBuild:
    def __init__(self):
        self.storage = {}
        self.adjlist = {}

    def insertVertex(self,artist, name, genre, instrument, year, popularity, duration, explicit, avail_marks, playCount, grossRev, age, annualRev):
        self.storage[name] = Vertex(artist,name, genre, instrument, year, popularity, duration, explicit, avail_marks,playCount, grossRev, age, annualRev)

    def euclideanDistance(self,first, second):
         popularity = math.pow(first.popularity - second.popularity, 2)
         duration = math.pow(first.duration - second.duration, 2)
        #  grossRev = math.pow(first.grossRev - second.grossRev, 2)
        #  playCount = math.pow(first.playCount  - second.playCount , 2)
         age = math.pow(first.age - second.age, 2)
         distance = math.sqrt(popularity + duration + age)
         return distance

    def getScore(self, first, second):
        value = 0
        if(first.getExplicit() == second.getExplicit()):
            value += 1
        if(first.getGenre() == second.getGenre()):
            value += 1
        if(first.getInstrument() == second.getInstrument()):
            value += 1
        return value
    
    def formulateGraph(self):
        for name1, vertex1 in self.storage.items():
            for name2, vertex2 in self.storage.items():
                if(name1 == name2): 
                    continue
                # getting score and distance to calculate weight
                score = self.getScore(vertex1,vertex2)
                dist = int(self.euclideanDistance(vertex1,vertex2))
                #checking that score and distance meet minimum for connection
                if dist < 50 and score > 1:
                    dist = dist * (1 / score)
                    if name1 in self.adjlist:
                        self.adjlist[vertex1.name].append((vertex2.name, dist))
                    elif name1 not in self.adjlist:
                        print(vertex1.name)
                        self.adjlist[vertex1.name] = []
                        self.adjlist[vertex1.name].append((vertex2.name, dist))

              
    def relaxer(self, pv, dv, v, u, weight):
        if(dv[v]> dv[u] + weight):
            dv[v] = dv[u] + weight
            pv[v] = u
        return pv,dv

    def getMin(self, S, dv):
        min_int = 2147483647
        min = ''
        for name, dist in dv.items():
            if name not in S:
                if dist < min_int:
                    min = name
                    min_int = dist
        return min

    def dijkstra(self, root):
        S = set()
        V_S = set()
        pv = {}
        dv = {}
        curr = root
        S.add(root)

        # setting the initial distance for all nodes to "infinity"
        for name,neighbors in self.adjlist.items():
            dv[name] = 2147483647
            pv[name] = ''
            if name != root:
                V_S.add(name)

        # setting root distance to zero
        dv[root] = 0

        while(len(V_S) != 0):

            if curr in self.adjlist.keys():
                for i in range(0, len(self.adjlist[curr])):
                    neighbrname = self.adjlist[curr][i][0]
                    weight = self.adjlist[curr][i][1]
                    pv, dv = self.relaxer(pv, dv, neighbrname, curr,  weight)

                if(curr != root):
                    S.add(curr)
                    V_S.remove(curr)

                curr = self.getMin(S, dv)

                if(curr == ''):
                    break
        
        return S, dv, pv

    def BFS(self,root, max):
        visited = []
        q = []
        counter = 0
        if root in self.adjlist.keys():
            visited.append((root, 0))
            q.append(root)
            while q and counter < max:
                curr  = q.pop(0)
                print(len(q))
                for nhbr,weight in self.adjlist[curr]:
                    if nhbr not in visited:
                        dist = self.euclideanDistance(self.storage[root], self.storage[nhbr])
                        visited.append({"name": nhbr,
                                        "weight": weight})
                        q.append(nhbr)
                        counter += 1
        return visited
    
    def getAdjList(self):
        return self.adjlist
    def getStorage(self):
        return self.storage

            





