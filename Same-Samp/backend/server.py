from flask import Flask, jsonify, request 
from flask_cors import CORS
from Vertex import Vertex
from GraphBuild import GraphBuild
from os import listdir
import csv
import json
import copy

#this part is horribly designed please don't judge D: 

# a_new_day_graph = GraphBuild()
# amen_graph = GraphBuild()
apache_graph = GraphBuild()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/apache_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         apache_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )
      apache_graph.formulateGraph()
      ashley_graph = GraphBuild()

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         ashley_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()


app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
  return {"members" : ["member1", "Member2", "Member3"]}


@app.route('/vertex', methods=['POST'])
def post_vertex():
   
   global data 
   global sample
   data = request.get_json()
   

  
   # getting sample name and grabbing associated csv file
   sample =  data['userData'][0]
   

   # creating graph from csv data
  #  inserting userVertex into graph

   return jsonify({"message": "Vertex received and stored."}), 200

  #  inserting userVertex into graph

@app.route('/algorithm', methods=['GET'])
def get_algorithm():
    global graphCopy
    graphCopy = copy.copy(apache_graph)
    

  # running selected algorithm
    adjlist = graphCopy.getAdjList()      
    storage = graphCopy.getStorage()

    graph = {
       "songs": []
    }

    for key, value in adjlist.items():
        tempSong = {}
        tempSong["name"] = storage[key].getName()
        tempSong["neighbors"] = []
        for name, weight in adjlist[key]:
          tempSong["neighbors"].append({"name": name,"weight": weight})
        graph["songs"].append(tempSong)
        

    algo = data['userData'][4]
    if algo== "Dijkstra":
      S, dv, pv = apache_graph.dijkstra("heliosphan")
      algoDict = {}

      count = 0
      for val in S:
          while(count < 15):
            algoDict[val] = (dv[val], pv[val])
            count += 1
          

      mainJSON = algoDict

      json_main_obj = json.dumps(algoDict)   
    elif algo == "Breadth First Search":
       traversal = graphCopy.BFS("heliosphan", 15)
       mainJSON = traversal
       json_main_obj = json.dumps(mainJSON) 

       

  # creating main JSON and inserting Graph JSON

   #running algo on graph and inserting algo JSON into main JSON package

   # delete global instance of current graph so that it is not stored

   #return main JSON

    with open("C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/testjson/apache_dijkstra.json", "w") as outfile:
          outfile.write(json_main_obj)

    return json_main_obj, 200


## two types of requests. One for dijkstras and the other for BFS

# for any new post request first build a new vertex. Then grab the associated csv file
# and build new graph with csv and newly created vertex from user inputs. Build main JSON and build graph JSON representation.
# after making graph, run selected algorithm and package result with main JSON.
# send main JSON to client 



if __name__ == "__main__" :
  app.run(debug=True)
