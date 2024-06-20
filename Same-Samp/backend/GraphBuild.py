import math
import heapq
from Vertex import Vertex


class GraphBuild:
    def __init__(self):
        self.storage = {}
        self.adjlist = {}
        self.root = None

    def insertVertex(self,artist, name, genre, instrument, year, popularity, duration, explicit, avail_marks, playCount, grossRev, age, annualRev):
        if self.root is None:
            self.root = Vertex(artist, name, genre, instrument, year, popularity, duration, explicit, avail_marks, playCount, grossRev, age, annualRev)
            self.storage[self.root.name] = self.root
        tempName = artist + " - " + name    
        self.storage[tempName] = Vertex(artist,name, genre, instrument, year, popularity, duration, explicit, avail_marks,playCount, grossRev, age, annualRev)

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
        if(first.getGenre() != second.getGenre()):
            value += 1
        if(first.getInstrument() == second.getInstrument()):
            value += 1
        return value
    
    def formulateGraph(self):
        count = 0
        for name1, vertex1 in self.storage.items():
            for name2, vertex2 in self.storage.items():
                if(name1 == name2): 
                    continue
                # getting score and distance to calculate weight
                score = self.getScore(vertex1,vertex2)
                dist = int(self.euclideanDistance(vertex1,vertex2))
                #checking that score and distance meet minimum for connection
                if dist < 5:
                    count += 1
                if dist < 15 and 1 < score:
                    dist = (dist * (1 / score)) * 10
                    if dist <= 0:
                        continue
                    #print(f"dist: {dist}")
                    if name1 in self.adjlist:
                        self.adjlist[vertex1.name].append((vertex2.name, dist))
                    elif name1 not in self.adjlist:
                        self.adjlist[vertex1.name] = []
                        self.adjlist[vertex1.name].append((vertex2.name, dist))
        print(f"count:", count)

              
    def relaxer(self, pv, dv, v, u, weight):
        if dv[v] > dv[u] + weight:
            dv[v] = dv[u] + weight
            pv[v] = u
        return pv, dv

    def getMin(self, S, dv):
        min_int = float('inf')
        min_node = None
        for name, dist in dv.items():
            if name not in S and dist < min_int:
                min_node = name
                min_int = dist
        return min_node

    def dijkstra(self, root, max):
        S = set()
        pv = {}
        dv = {}
        curr = root

        for name in self.adjlist.keys():
            dv[name] = float('inf')
            pv[name] = None

        dv[root] = 0

        while len(S) < len(self.adjlist):
            curr = self.getMin(S, dv)
            if curr is None:
                break

            S.add(curr)

            for neighbor, weight in self.adjlist[curr]:
                pv, dv = self.relaxer(pv, dv, neighbor, curr, weight)

        sorted_distances = sorted([(name, dv[name]) for name in dv if name != root and dv[name] != float('inf')], key=lambda x: x[1])
        result = [{"name": name, "weight": dist} for name, dist in sorted_distances[:max]]

        return result


    def BFS(self, root, max):
        visited = set()
        result = []
        queue = [(root, 0)]  # (node, cumulative_distance)

        while queue and len(result) < max:
            curr, curr_dist = queue.pop(0)

            if curr not in visited:
                visited.add(curr)
                if curr != root:
                    result.append({"name": curr, "weight": curr_dist})

                for neighbor, weight in self.adjlist[curr]:
                    if neighbor not in visited:
                        new_dist = curr_dist + weight
                        queue.append((neighbor, new_dist))

        # Sort the results to get the closest 'max' elements if necessary
        result = sorted(result, key=lambda x: x['weight'])[:max]
        return result
    
    def clear(self):
        self.adjlist = {}
        
    def getAdjList(self):
        return self.adjlist
    
    def getStorage(self):
        return self.storage

            





