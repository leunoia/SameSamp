import os
import csv
import json
import copy
from flask import Flask, jsonify, request 
from flask_cors import CORS
from Vertex import Vertex
from GraphBuild import GraphBuild


file_path = os.path.abspath(os.path.dirname(__file__)) 

a_new_day_graph = GraphBuild()
apache_graph = GraphBuild()
amen_graph = GraphBuild()
ashley_graph = GraphBuild()
bring_the_noise_graph = GraphBuild()
changed_the_beat_graph = GraphBuild()
funk_drummer_graph = GraphBuild()
funk_pres_graph = GraphBuild()
here_we_go_graph = GraphBuild()
hot_pants_graph = GraphBuild()
impeach_the_president_graph = GraphBuild()
kool_is_back_graph = GraphBuild()
la_di_da_graph = GraphBuild()
long_red_graph = GraphBuild()
sing_simple_graph = GraphBuild()
synthetic_graph = GraphBuild()
take_me_mardi_gra_graph = GraphBuild()
the_champ_graph = GraphBuild()
think_about_it_graph = GraphBuild()
ufo_graph = GraphBuild()

graph_paths = {
    'a_new_day_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/amen_brother_spotified.csv',
    'apache_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/apache_spotified.csv',
    'amen_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/amen_brother_spotified.csv',
    'ashley_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/ashley_roachclip_spotified.csv',
    'bring_the_noise_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/bring_the_noise_spotified.csv',
    'changed_the_beat_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/changed_the_beat_spotified.csv',
    'funk_drummer_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/funk_drummer_spotified.csv',
    'funk_pres_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/funky_president_spotified.csv',
    'here_we_go_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/here_we_go_spotified.csv',
    'hot_pants_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/hot_pants_spotified.csv',
    'impeach_the_president_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/impeach_the_president_spotified.csv',
    'kool_is_back_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/kool_is_back_spotified.csv',
    'la_di_da_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/la_di_da_di_spotified.csv',
    'long_red_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/long_red_spotified.csv',
    'sing_simple_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/sing_a_simple_spotified.csv',
    'synthetic_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/synthetic_substitution_spotified.csv',
    'take_me_mardi_gra_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/take_me_mardi_gra_spotified.csv',
    'the_champ_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/the_champ_spotified.csv',
    'think_about_it_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/think_about_it_spotified.csv',
    'ufo_graph': 'C:/Users/Preston Barney/Desktop/Coding_Projects/SameSamp/Same-Samp/backend/CSVs/ufo_spotified.csv'
}

for graph_name, file_path in graph_paths.items():
    with open(file_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            market = []
            for country in csv.reader(row[10], delimiter=','):
                market.append(country)
            globals()[graph_name].insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]))
        infile.close()


def select_graph(sample):
    graph_map = {
    'Amen, Brother - The Winstons': amen_graph,
    'Think (About It) - Lyn Collins': think_about_it_graph,
    'Change the Beat (Female Version) - Beside': changed_the_beat_graph,
    'Funky Drummer - James Brown': funk_drummer_graph,
    'La Di Da Di - Doug E. Fresh and Slick Rick': la_di_da_graph,
    'Funky President (People It\'s Bad) - James Brown': funk_pres_graph,
    'Bring the Noise - Public Enemy': bring_the_noise_graph,
    'Synthetic Substitution - Melvin Bliss': synthetic_graph,
    'Here We Go (Live at Funhouse) - Run-DMC': here_we_go_graph,
    'Hot Pants (Bonus Beats) - Bobby Byrd': hot_pants_graph,
    'Long Red - Mountain': long_red_graph,
    'Impeach the President - The Honey Dripper': impeach_the_president_graph,
    'The Champ - The Mohawks': the_champ_graph,
    'Apache - Incredible Bongo Band': apache_graph, 
    'Kool is Back - Funk, Inc': kool_is_back_graph,
    'UFO - ESG': ufo_graph,
    'It\'s a New Day - Skull Snaps': a_new_day_graph,
    'Ashley\'s Roadclip - The Soul Searchers': ashley_graph,
    'Sing a Simple Song - Sly & the Family Stone': sing_simple_graph,
    'Take Me to the Mardi Gras - Bob James': take_me_mardi_gra_graph
}
    return graph_map.get(sample, None)

def build_graph_response(graph_copy):
    adjlist = graph_copy.getAdjList()
    storage = graph_copy.getStorage()
    graph = {"songs": []}
    for key, value in adjlist.items():
        tempSong = {"name": storage[key].getName(), "genre": storage[key].getGenre() , "neighbors": [{"name": name, "genre":storage[name].getGenre(), "weight": weight} for name, weight in adjlist[key]]}
        graph["songs"].append(tempSong)
    return graph

def run_algorithm(graph_copy, algo):
    if algo == "Dijkstra":
        return graph_copy.dijkstra("user - song", 15)
    elif algo == "Breadth First Search":
        return graph_copy.BFS("user - song", 15)

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
  return {"members" : ["member1", "Member2", "Member3"]}


@app.route('/algorithm', methods=['GET'])
def get_algorithm():
    user_data = request.args.get('userData')

    if user_data:
        data = json.loads(user_data)
        sample = data[0]
        graph_copy = select_graph(sample)  # Helper function to select graph
        graph_copy.clear()
        graph_copy.insertVertex("user", "song", data[3], data[1], 2024, 50, int(data[5])*1000, data[6], "US", 50000, (50000 * 0.002), 1, (50000 * 0.002))
        graph_copy.formulateGraph()
        
        graph = build_graph_response(graph_copy)
        algo_response = run_algorithm(graph_copy, data[4])
        
        mainJSON = {"graph": graph, "algo": algo_response}
        return jsonify(mainJSON), 200
    return jsonify({"error": "Invalid request"}), 400

## two types of requests. One for dijkstras and the other for BFS

# for any new post request first build a new vertex. Then grab the associated csv file
# and build new graph with csv and newly created vertex from user inputs. Build main JSON and build graph JSON representation.
# after making graph, run selected algorithm and package result with main JSON.
# send main JSON to client 


if __name__ == "__main__" :
  app.run(debug=True)