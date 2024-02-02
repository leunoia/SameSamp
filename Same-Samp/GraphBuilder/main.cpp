#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include "dist/json/json.h"

using namespace std;

void getFile(string &fileName) {
    if (fileName == "1")
        fileName = "../CSVS/amenbrothercleansed.csv";
    if (fileName == "2")
        fileName = "../CSVS/changed_the_beat_spotified.csv";
    if (fileName == "3")
        fileName = "../CSVS/apache_spotified.csv";
}

struct Vertex {
    string Name, Artist, Genre, Instrument, Year;
    bool ExplicitVal;
    vector<string> AvailableMarkets;
    double Popularity;
    int Playcount;
    double Duration;
    double GrossRev;
    double AnnualRev;
    int Age;
};

class Graph {
    unordered_map<string, Vertex> Storage;          // Contains all vertices to get score later
    unordered_map<string, vector<pair<string, int>>> AdjList;
    //           song_name         song_name | score
public:
    void insertVertex(string Artist, string Song_Name, string Track_ID, string Genre, string Instrument, int Year, double Popularity, double Duration, bool Explicit, vector<std::string> Available_Markets);
    int euclideanDistance(Vertex first, Vertex second);
    int getScore(Vertex first, Vertex second);
    void formulateGraph();
    void printGraph();
    Json::Value JSONStringGenerator();
    void Dijkstra(string start);
};

void Graph::insertVertex(string Artist, string Song_Name, string Track_ID, string Genre, string Instrument, int Year, double Popularity, double Duration, bool Explicit, vector<std::string> Available_Markets) {
    Storage[Song_Name].Artist = Artist;
    Storage[Song_Name].Name = Song_Name;
//    Storage[Song_Name].Track_ID = Track_ID;
    Storage[Song_Name].Genre = Genre;
    Storage[Song_Name].Instrument = Instrument;
    Storage[Song_Name].Year = Year;
    Storage[Song_Name].AvailableMarkets = Available_Markets;
    Storage[Song_Name].ExplicitVal = Explicit;
    Storage[Song_Name].Popularity = Popularity;
    Storage[Song_Name].Duration = Duration / 1000;
    Storage[Song_Name].Age = (2022 - Year);
    Storage[Song_Name].GrossRev = 0;
    Storage[Song_Name].AnnualRev = 0;
}

int Graph::euclideanDistance(Vertex first, Vertex second){
    double popularity = pow(first.Popularity - second.Popularity , 2);
    double duration = pow(first.Duration - second.Duration, 2);
//    double grossRev = pow(first.GrossRev - second.GrossRev, 2);
//    double annualRev = pow(first.AnnualRev - second.AnnualRev, 2);
    double age = pow(first.Age - second.Age, 2);
    int distance = sqrt(popularity + duration + age);

    return distance;
}
int Graph::getScore(Vertex first, Vertex second) {
    int value = 0;

    if (first.ExplicitVal == second.ExplicitVal)
        value++;
    if (first.Genre == second.Genre)
        value ++;
    if (first.Instrument == second.Instrument)
        value++;

    return value;
}

void Graph::formulateGraph() {
    for(auto itr = Storage.begin(); itr != Storage.end(); ++itr) {
        for(auto itr2 = Storage.begin(); itr2 != Storage.end(); ++itr2) {
            cout << "vertex 1: "<< itr->second.Name << endl;
            cout << "vertex 2: " << itr2->second.Name << endl;
            int currScore = getScore(itr->second, itr2->second);
            int currDist = euclideanDistance(itr->second, itr2->second);
            if ((currDist  < 80) && (itr->first != itr2->first) && (currScore > 1))
                AdjList[itr->first].push_back({itr2->first, currDist});
        }
    }
}

void Relaxation (unordered_map<string, string> &pv , unordered_map<string, int> &dv, string v, string u, int weight) {
    if (dv[v] > dv[u] + weight) {
        dv[v] = dv[u] + weight;         // Changes distance because it's shorter
        pv[v] = u;          // Makes v's new parent u
    }
}

string getMin(unordered_set<string> S, unordered_map<string, int> dv) {
    int min_int = 2147483647;
    string min;
    for (auto itr = dv.begin(); itr != dv.end(); ++itr) {
        if (S.count(itr->first) == 0) {
            if (itr->second < min_int) {
                min = itr->first;
                min_int = itr->second;
            }
        }
    }
    return min;
}

 Graph::Dijkstra(string start) {
    unordered_set<string> S;            // Vertices computed
    unordered_set<string> V_S;          // Vertices that still need to be processed
    unordered_map<string, string> pv;      // Predecessor name
    unordered_map<string, int> dv;         // Distance value
    string curr = start;            // This is so the while-loop can iterate on lowest uncomputed d[v]
    S.insert(start);
    for (auto itr = AdjList.begin(); itr != AdjList.end(); ++itr) {          // Set all distances to infinity
        dv[itr->first] = 2147483647;
        pv[itr->first] = "";
        if (itr->first != start)
            V_S.insert(itr->first);
    }
    dv[start] = 0;          // Initial distance is 0
    while (!V_S.empty()) {
        for (int i = 0 ; i < AdjList[curr].size(); i++) {
            Relaxation(pv, dv, AdjList[curr][i].first, curr, AdjList[curr][i].second);
        }
        if (curr != start) {
            S.insert(curr);
            V_S.erase(curr);
        }
        curr = getMin(S, dv);
        if (curr == "")
            break;
    }



    int total_vertices = 0;
    cout << "=================================" << endl;
    cout << "Dijkstra's for: " << start << endl;
    cout << "=================================" << endl;
    for (auto itr = Storage.begin(); itr != Storage.end(); ++itr) {          // Print Test
        if (itr->first == start)
            continue;
        if (pv[itr->first] != "") {
            cout << "Vertex: " << itr->first << " | Distance: " << dv[itr->first] << " | Parent: " << pv[itr->first]<< endl;
            total_vertices++;
        }
    }
    cout << "=================================" << endl;
    cout << "Total vertices connected: " << total_vertices << endl;

}

void Graph::printGraph() {
    for(auto itr = Storage.begin(); itr != Storage.end(); ++itr) {
        cout << "Vertex: " << itr->first << endl;
        cout << "----==============Neighbors===============----" << endl;
        for (int i = 0; i < AdjList[itr->first].size(); i++) {
            cout << AdjList[itr->first].at(i).first << " Score: " << AdjList[itr->first].at(i).second << endl;
        }
        cout << "----======================================----" << endl << endl;
    }
}

Json::Value Graph::JSONStringGenerator(){

    Json::Value AdjList;
    Json::Value songsvec(Json::arrayValue);
    int id = 0;
    for(auto itr = Storage.begin(); itr != Storage.end(); ++itr) {
        if(id == 50)
            break;
        Json::Value song;
        song["name"] = itr->second.Name;
        song["artist"] = itr->second.Artist;
        song["genre"] = itr->second.Genre;
        song["instrument"] = itr->second.Instrument;

        Json::Value neighbors(Json::arrayValue);

        for (int i = 0; i < this->AdjList[itr->first].size(); i++) {
            Json::Value neighborsong;
            neighborsong["name"] =  this->AdjList[itr->first].at(i).first;
            neighborsong["weight"] = to_string(this->AdjList[itr->first].at(i).second);
            neighbors.append(neighborsong);
        }
        song["neighbors"] = neighbors;
        songsvec.append(song);
        id++;
    }
    AdjList["songs"] = songsvec;
    return AdjList;
}

int main() {

    Graph System;
    fstream CSV;
    string fileName, input;

    cout << "=====================================" << endl;
    cout << "  Welcome to SameSamp Graph Builder! " << endl;
    cout << "=====================================" << endl;
    cout << "Select CSV:" << endl;
    cout << "1. BIG " << endl;
    cout << "2. MEDIUM " << endl;
    cout << "3. SMALL" << endl;
    cin >> fileName;


    getFile(fileName);
    CSV.open(fileName);


    while (getline(CSV, input)) {           // Inserting values into storage
        string Artist, Song_Name, Track_ID, Genre, Instrument, tempYear, tempPop, tempDur, tempExp;
        int Year;
        double Popularity, Duration;
        bool Explicit = 0;
        vector<std::string> Available_Markets;

        input = input.substr(input.find(',') + 1, input.length());
        Artist = input.substr(0, input.find(','));

        input = input.substr(input.find(',') + 1, input.length());
        Song_Name = input.substr(0, input.find(','));

        input = input.substr(input.find(',') + 1, input.length());
        Track_ID = input.substr(0, input.find(','));

        input = input.substr(input.find(',') + 1, input.length());
        Genre = input.substr(0, input.find(','));

        input = input.substr(input.find(',') + 1, input.length());
        Instrument = input.substr(0, input.find(','));

        input = input.substr(input.find(',') + 1, input.length());
        tempYear = input.substr(0, input.find(','));
        Year = stoi(tempYear);

        input = input.substr(input.find(',') + 1, input.length());
        tempPop = input.substr(0, input.find(','));
        Popularity = stod(tempPop);

        input = input.substr(input.find(',') + 1, input.length());
        tempDur = input.substr(0, input.find(','));
        Duration = stod(tempDur);

        input = input.substr(input.find(',') + 1, input.length());
        tempExp = input.substr(0, input.find(','));
        if(tempExp == "TRUE")
            Explicit = 1;
        else if(tempExp == "FALSE")
            Explicit = 0;
//        input = input.substr(input.find(',') + 1, input.length());
//        Available_Markets = input;

        System.insertVertex(Artist, Song_Name, Track_ID, Genre, Instrument, Year, Popularity, Duration, Explicit, Available_Markets);
    }


    cin.get();
    System.formulateGraph();
    cout << "Choose song to put" << endl;
    string song;
    getline(cin, song);
    System.Dijkstra(song);


    //creating Adjacency List
    Json::Value AdjList = System.JSONStringGenerator();

    cout<< "Example JSON Conversion Test:" << endl;

// deprecated way to build JSON file with jsonCPP
    std::ofstream file_id;
    file_id.open("../JSON/apache_test.json");


    Json::FastWriter fastWriter;
    file_id << fastWriter.write(AdjList);

    file_id.close();



// newer way to build JSON file with jsonCPP
//    Json::StreamWriterBuilder builder;
//    builder["commentStyle"] = "None";
//    builder["indentation"] = "   ";
//
//    std::unique_ptr<Json::StreamWriter> writer(builder.newStreamWriter());
//    std::ofstream outputFileStream("../JSON/test50.json");
//    writer -> write(AdjList, &outputFileStream);


    return 0;
}