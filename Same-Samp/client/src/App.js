import React, { useState, useEffect } from 'react';
import './App.css';
import sslogo from './samesamplogo222.png';
import Search from './components/Search.js';
import SearchResults from './components/SearchResults.js';
import DropDown from './components/DropDown.js';
import Graph from 'vis-react';
import SongList from './components/SongList'; // Import the new component

const genres = {
  "Electronic / Dance": 0,
  "Hip-Hop / Rap / R&B": 1,
  "Rock / Pop": 2,
  "Other": 3,
  "SoundTrack / Library": 4,
  "Soul / Funk / Disco": 5,
  "Jazz / Blues": 6,
  "Reggae / Dub": 7,
  "Country / Folk": 8,
  "World / Latin": 9,
  "Classical": 10,
};

function convertGraphFormat(graphData) {
  const nodes = [];
  const links = [];
  const nodeIdMap = {};
  let currentId = 1;

  // Add all unique nodes
  graphData.songs.forEach(song => {
    if (!nodeIdMap[song.name]) {
      nodeIdMap[song.name] = currentId;
      nodes.push({ id: currentId, label: song.name, group: genres[song.genre], genre: song.genre });
      currentId += 1;
    }
    song.neighbors.forEach(neighbor => {
      if (!nodeIdMap[neighbor.name]) {
        nodeIdMap[neighbor.name] = currentId;
        nodes.push({ id: currentId, label: neighbor.name, group: genres[neighbor.genre], genre: neighbor.genre });
        currentId += 1;
      }
      // Add link
      links.push({
        from: nodeIdMap[song.name],
        to: nodeIdMap[neighbor.name],
        value: neighbor.weight,
      });
    });
  });

  return { nodes, edges: links };
}

function App() {
  useEffect(() => {
    // Referenced from
    // https://stackoverflow.com/questions/75774800/how-to-stop-resizeobserver-loop-limit-exceeded-error-from-appearing-in-react-a
    window.addEventListener('error', (e) => {
      if (e) {
        const resizeObserverErrDiv = document.getElementById('webpack-dev-server-client-overlay-div');
        const resizeObserverErr = document.getElementById('webpack-dev-server-client-overlay');
        if (resizeObserverErr) resizeObserverErr.className = 'hide-resize-observer';
        if (resizeObserverErrDiv) resizeObserverErrDiv.className = 'hide-resize-observer';
      }
    });
  }, []);

  const [songs, setSongs] = useState([]);
  const [result, setResult] = useState('');
  const [instrument, setInst] = useState('');
  const [genre, setGenre] = useState('');
  const [year, setYear] = useState('');
  const [algorithm, setAlg] = useState('');
  const [isResult, setIsResult] = useState(false);
  const [explicit, setExplicit] = useState('');
  const [duration, setDuration] = useState('');
  const [graph, setGraph] = useState({ nodes: [], edges: [] });
  const [graphReady, setGraphReady] = useState(false); // State to track if the graph data is ready
  const [algoResults, setAlgoResults] = useState([]); // State to store algorithm results

  var options = {
    nodes: {
      shape: 'dot',
      scaling: {
        min: 10,
        max: 30,
      },
      font: {
        size: 30,
        face: 'Tahoma',
      },
    },
    edges: {
      arrows: {
        to: false,
      },
      width: 0.15,
      color: { inherit: 'from' },
    },
    physics: {
      stabilization: false,
      barnesHut: {
        gravitationalConstant: -2000,
        springConstant: 0.01,
        springLength: 300,
      },
    },
    interaction: {
      tooltipDelay: 200,
      hideEdgesOnDrag: true,
    },
  };

  const events = {
    select: function (event) {
      var { nodes, edges } = event;
    },
  };

  const submitVertex = async (userData) => {
    try {
      const queryParams = new URLSearchParams({ userData: JSON.stringify(userData) }).toString();
      const response = await fetch(`http://localhost:5000/algorithm?${queryParams}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch algorithm');
      }

      const data = await response.json();
      console.log('Data: ', data);
      const convertedGraph = convertGraphFormat(data.graph);
      console.log('Converted Graph: ', convertedGraph);
      setGraph(convertedGraph); 
      setGraphReady(true); 
      setAlgoResults(data.algo); 
    } catch (error) {
      console.error(error);
    }
  };

  const canSearch = () => {
    if (result && instrument && genre && algorithm && duration && explicit) {
      const userData = [result, instrument, 2024, genre, algorithm, duration, explicit];
      console.log(`userData: ${userData}`);
      submitVertex(userData);
      setGraphReady(false);
    } else {
      alert('Fill in all inputs!');
    }
  };

  return (
    <div className="App">
      <div className="content">
        <div className="landing">
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <img style={{ width: '30%', height: 'auto' }} src={sslogo} alt="logo" />
          </div>
          <div>
            <Search setSongs={setSongs} result={result} setResult={setResult} isResult={isResult} setIsResult={setIsResult} />
            {songs && <SearchResults songs={songs} setResult={setResult} isResult={isResult} setIsResult={setIsResult} />}
            <DropDown setInst={setInst} setAlg={setAlg} setGenre={setGenre} setYear={setYear} setDuration={setDuration} setExplicit={setExplicit} />
          </div>
          <div style={{ marginTop: '3px' }}>
            <button onClick={canSearch} style={{ marginLeft: '10px' }}>Search</button>
          </div>
        </div>
        {graphReady && (
          <div className="results-container">
            <div className="graph">
              <Graph
                graph={graph}
                options={options}
                events={events}
                getNetwork={Graph.getNetwork}
              />
            </div>
            <div className="song-list-container">
              <SongList songs={algoResults} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
