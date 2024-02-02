#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <fstream>
#include <vector>

using namespace std;

void getFile(string &fileName) {
    if (fileName == "1")
        fileName = "/Users/ignatius/CLionProjects/SameSamp/CSVS/a_new_day_spotified.csv";
    if (fileName == "2")
        fileName = "/Users/ignatius/CLionProjects/SameSamp/CSVS/think_about_it_spotified.csv";
}

struct Vertex {
    string Artist, Song_Name, Track_ID, Genre, Instrument, Year, Popularity, Duration, Explicit, Available_Markets;
    vector<string> AM;
};

class Graph {
    unordered_map<string, Vertex> Storage;          // Contains all vertices to get score later
    unordered_map<string, vector<pair<string, int>>> Function;
    //           song_name         song_name | score
public:
    void insertVertex(string Artist, string Song_Name, string Track_ID, string Genre, string Instrument, string Year, string Popularity, string Duration, string Explicit, string Available_Markets);
    int getScore(Vertex first, Vertex second);
    void formulateGraph();
    void printGraph();
    void printNeighbors();
    void Dijkstra(string start);
};

void Graph::insertVertex(string Artist, string Song_Name, string Track_ID, string Genre, string Instrument, string Year, string Popularity, string Duration, string Explicit, string Available_Markets) {
    Storage[Song_Name].Artist = Artist;
    Storage[Song_Name].Song_Name = Song_Name;
    Storage[Song_Name].Track_ID = Track_ID;
    Storage[Song_Name].Genre = Genre;
    Storage[Song_Name].Instrument = Instrument;
    Storage[Song_Name].Year = Year;
    Storage[Song_Name].Popularity = Popularity;
    Storage[Song_Name].Duration = Duration;
    Storage[Song_Name].Explicit = Explicit;
    Storage[Song_Name].Available_Markets = Available_Markets;
}

int Graph::getScore(Vertex first, Vertex second) {
    int value = 0;
    if (first.Artist == second.Artist)
        value++;
    if (first.Popularity == second.Popularity)
        value++;
    if (first.Explicit == second.Explicit)
        value++;
    if (first.Duration == second.Duration)
        value++;
    if (first.Genre == second.Genre)
        value ++;
    if (first.Instrument == second.Instrument)
        value++;
    if (first.Year == second.Year)
        value++;
    return value;
}

void Graph::formulateGraph() {
    for(auto itr = Storage.begin(); itr != Storage.end(); ++itr) {
        for(auto itr2 = Storage.begin(); itr2 != Storage.end(); ++itr2) {
            int currScore = getScore(itr->second, itr2->second);
            if ((currScore > 4) && (itr->first != itr2->first))
                Function[itr->first].push_back({itr2->first, currScore});
        }
    }
}

void Graph::printGraph() {
    cout << "----======================================----" << endl;
    for (auto itr = Storage.begin(); itr != Storage.end(); ++itr) {
        cout << "Name: " << Storage[itr->first].Song_Name << endl;
        cout << "Artist: " << Storage[itr->first].Artist << endl;
        cout << "Track ID: " << Storage[itr->first].Track_ID << endl;
        cout << "Genre: " << Storage[itr->first].Genre << endl;
        cout << "Instrument: " << Storage[itr->first].Instrument << endl;
        cout << "Year: " << Storage[itr->first].Year << endl;
        cout << "Popularity: " << Storage[itr->first].Popularity << endl;
        cout << "Duration: " << Storage[itr->first].Duration << endl;
        cout << "Explicit: " << Storage[itr->first].Explicit << endl;
        cout << "Available Markets: " << Storage[itr->first].Available_Markets << endl;
        cout << "----======================================----" << endl;
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

void Graph::Dijkstra(string start) {
    unordered_set<string> S;            // Vertices computed
    unordered_set<string> V_S;          // Vertices that still need to be processed
    unordered_map<string, string> pv;      // Predecessor name
    unordered_map<string, int> dv;         // Distance value
    string curr = start;            // This is so the while-loop can iterate on lowest uncomputed d[v]
    S.insert(start);
    for (auto itr = Function.begin(); itr != Function.end(); ++itr) {          // Set all distances to infinity
        dv[itr->first] = 2147483647;
        pv[itr->first] = "";
        if (itr->first != start)
            V_S.insert(itr->first);
    }
    dv[start] = 0;          // Initial distance is 0
    while (!V_S.empty()) {
        for (int i = 0 ; i < Function[curr].size(); i++) {
            Relaxation(pv, dv, Function[curr][i].first, curr, Function[curr][i].second);
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

    //                                            PRINT TEST
    /*
    cout << "=================================" << endl;
    cout << "Dijkstra's for: " << start << endl;
    cout << "=================================" << endl;
    for (auto itr = Storage.begin(); itr != Storage.end(); ++itr) {          // Print Test
        if (itr->first == start)
            continue;
        if (pv[itr->first] != "")
            cout << "Vertex: " << itr->first << " | Distance: " << dv[itr->first] << " | Parent: " << pv[itr->first] << endl;
    }
     */
}

void Graph::printNeighbors() {
    for (auto itr = Function.begin(); itr != Function.end(); ++itr) {
        cout << "---------------------------------------------" << endl;
        cout << "Vertex: " << itr->first << endl;
        cout << "==================Neighbors==================" << endl;
        for (int i = 0; i < Function[itr->first].size(); i++) {
            cout << "Vertex: " << Function[itr->first][i].first << " Score: " << Function[itr->first][i].second << endl;
        }
        cout << endl;
    }
}

int main() {
    Graph System;
    fstream CSV;
    string fileName, input;

    cout << "=====================================" << endl;
    cout << "         Welcome to SameSamp!        " << endl;
    cout << "=====================================" << endl;
    cout << "Select CSV:" << endl;
    cout << "1." << endl;
    cout << "2." << endl;
    cin >> fileName;

    getFile(fileName);
    CSV.open(fileName);

    while (getline(CSV, input)) {           // Inserting values into storage
        string Artist, Song_Name, Track_ID, Genre, Instrument, Year, Popularity, Duration, Explicit, Available_Markets;
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

        Year = input.substr(0, input.find(','));
        input = input.substr(input.find(',') + 1, input.length());

        Popularity = input.substr(0, input.find(','));
        input = input.substr(input.find(',') + 1, input.length());

        Duration = input.substr(0, input.find(','));
        input = input.substr(input.find(',') + 1, input.length());

        Explicit = input.substr(0, input.find(','));
        input = input.substr(input.find(',') + 1, input.length());

        Available_Markets = input;
        System.insertVertex(Artist, Song_Name, Track_ID, Genre, Instrument, Year, Popularity, Duration, Explicit, Available_Markets);
    }

    cin.get();
    System.formulateGraph();
    cout << "Choose song to put" << endl;
    string song;
    getline(cin, song);
    System.Dijkstra(song);

    cout << endl;


    return 0;
}