import {useState, useEffect} from 'react'
import './App.css';
import sslogo from './SameSampLogo.jpg';
import Dijkstra from './components/DijkstraTable';
import Search from './components/Search.js';
import SearchResults from './components/SearchResults.js';
import DropDown from './components/DropDown.js';
import BFS from './components/BFS.js'
import Graph from "react-graph-vis";


var graph = {
}
function graphBuilder(jsonfile){
  // instantiatig graph
  var graph = {
    nodes: [

    ],
    edges: [

    ]
  }
  // turning JSON into string & reading JSON file and creating local Javascript Object
  var jsonstring = JSON.stringify(jsonfile)
  var songsObj = JSON.parse(jsonstring);
  var songs = songsObj.songs;

  var nodesCopy = [];
  var color = '#FAADE7';
  for(let i =0; i < songs.length; i++){
    let tempcid;
    switch(songs[i].genre){
      case 'Electronic / Dance':
        color = '#00ffff'; // cerulean blue
        tempcid = 1;
        break;
      case 'Hip-Hop / Rap / R&B':
        color = '#002e63'; //desaturated black
        tempcid = 2;
        break;
      case 'Rock / Pop':
        color = '#cc0099'; //medium violet
        tempcid = 3;
        break;
      case 'Jazz / Blues':
        color = '#bf94e4'; // lavender
        tempcid = 4; 
        break; 
      case 'SoundTrack / Library':
        color = '#ffffff'; //white smoke ahaha
        tempcid = 5;
        break;
      case 'Soul / Funk / Disco':
        color = '#556b2f'; // olive green
        tempcid = 6;
        break;
      case 'Reggae / Dub':
        color = '#ff7e4e'; // orange red
          tempcid = 7;
          break;
      case 'Country / Folk':
        color = '#a0785a'; //pale
          tempcid = 8;
          break;
      case 'World / Latin':
          color = '#ffa812'; // neon yellow
          tempcid = 9;
          break;
      case 'Classical':
          tempcid = 10;
          color = '#9bddff'; // light blue
          break;
      case 'Other':
          tempcid = 11;
          color = '#FAADE7'; // pink
          break;
      default:
        tempcid = 12;
        color = '#FAADE7'; // pink
    }


    var tempSong = {
      id: `${songs[i].name}`,
      label: `${songs[i].name}`,
      artist: `${songs[i].artist}`,
      genre: `${songs[i].genre}`,
      instrument: `${songs[i].instrument}`,
      cid: tempcid,
      color: color
    }
    nodesCopy.push(tempSong);
    
  }
  var set = new Set();
  var setEdge = true;
  var edgesCopy = [];
  for(let i = 0; i < songs.length; i++){
      for(let n = 0; n < songs[i].neighbors.length; n++){

        
        var tempEdge = {
          from: songs[i].name,
          to: songs[i].neighbors[n].name,
          value: songs[i].neighbors[n].weight
        }
        console.log(set);

        for(let edge of set){
          if (edge.from === tempEdge.to && edge.to == tempEdge.from){
            console.log(edge.from);
            console.log(edge.to);
            console.log(tempEdge.to);
            console.log(tempEdge.from);
            setEdge = false;
          }
        }

        if(setEdge) {
          edgesCopy.push(tempEdge);
        }
        set.add({from: songs[i].name, to: songs[i].neighbors[n].name});
        setEdge = true;
      }
  }
  graph.nodes = nodesCopy;
  graph.edges = edgesCopy;
  return graph; 
}

function App() {
  useBeforeRender(() => {
    //referenced from 
    //https://stackoverflow.com/questions/75774800/how-to-stop-resizeobserver-loop-limit-exceeded-error-from-appearing-in-react-a
      window.addEventListener("error", (e) => {
        if (e) {
          const resizeObserverErrDiv = document.getElementById(
            "webpack-dev-server-client-overlay-div",
          );
          const resizeObserverErr = document.getElementById(
            "webpack-dev-server-client-overlay",
          );
          if (resizeObserverErr)
            resizeObserverErr.className = "hide-resize-observer";
          if (resizeObserverErrDiv)
            resizeObserverErrDiv.className = "hide-resize-observer";
        }
      });
  }, []);

  const [songs, setSongs] = useState([]);
  const [result, setResult] = useState("");
  const [go, setGo] = useState(false);
  const [instrument, setInst] = useState("");
  const [genre, setGenre] = useState("");
  const [year, setYear] = useState("");
  const [algorithm, setAlg] = useState("");
  const [isResult, setIsResult] = useState(false);
  const [explicit, setExplicit] = useState("");
  const [duration, setDuration] = useState("");
  const [userData, setUserData] = useState([]);
  const [backendData, setBackendData] = useState([]); // fetch json data from backend
  const [currSong, setCurrSong] = useState('');
  const [graph_, setGraph] = useState({});


  //Dummy backend data fetch to set backendData so we can use it here in the frontend
  useEffect(()=>{
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setBackendData(data)
        console.log(data)
      }
    )
  }, []) 


  const submitVertex = async () => {
    try {
      const response = await fetch('http://localhost:5000/vertex', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ userData }),
      });

      if (!response.ok) {
        throw new Error('Failed to submit vertex');
      }

      console.log('Vertex submitted successfully');
      console.log(userData)
    } catch (error) {
      console.error(error);
    }
    try {
      const response = await fetch('http://localhost:5000/algorithm');
      if (!response.ok) {
        throw new Error('Failed to fetch algorithm');
      }
      const data = await response.json();
      setBackendData(data)
      setGraph(graphBuilder(backendData)) // builds graph once
      setGo(true);
    } catch (error) {
      console.error(error);
    }
  };

  // large network test options color
  var options = {
    improvedLayout: true,
    autoResize: true,
    width: '100%',
    height: '100%',
    configure:{ enabled: false,
      container: undefined},
    nodes: {
      shape: "dot",
      size: 25,
      scaling: {
        min: 10,
        max: 30,
      },
      font: {
        size: 20,
        strokeWidth: 2,
        strokeColor: 'white',
        color: 'black',
        bold: {
          color: 'black',
          size: 25, // px
          face: 'arial',
          vadjust: 0,
          mod: 'bold'
        },
        face: "arial",
      },
      color: {background: '#FAADE7', border: '#1A2642', highlight: '#9DF495'},
    },
    edges: {
      width: 0.05,
      color: { inherit: "from" },
      smooth: {
        type: "continuous",
      },
      arrows: {
              to: {
                enabled: false,
              },
              middle: {
                enabled: false,
              },
              from: {
                enabled: false,
              }
            }
    },
    physics: {
      stabilization: false,
      barnesHut: {
        gravitationalConstant: -80000,
        springConstant: 0.001,
        springLength: 100,
      },
    },
    interaction: {
      zoomView: true,
      tooltipDelay: 200,
      hideEdgesOnDrag: false,
    },
  };

  const handleAddVertex = () => {
    if (result && instrument && year && genre && algorithm && duration && explicit) {
      setUserData([result ,instrument ,year , genre , algorithm , duration ,explicit]);
    }else{
      alert("Fill in all inputs!");
    }
  };
  
const canSearch = () =>{
  if(result && instrument && year && genre && algorithm && duration && explicit){
    console.log(`result: ${result}`)
    console.log(`userData: ${userData}`)
    submitVertex();
    setCurrSong(result);
  }
  else{
    alert("Fill in all inputs!");
  }
};


  return (
  
    <div className="App">
      <div className="content">
        <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <img style={{width: '50%', height: '30%'}} src={sslogo} alt="logo"/>
        </div>
        <Search setSongs = {setSongs} result={result} setResult={setResult} isResult={isResult} setIsResult={setIsResult}/>
        {songs && <SearchResults songs = {songs} setResult={setResult} isResult={isResult} setIsResult={setIsResult}/>}
        <DropDown setInst = {setInst} setAlg = {setAlg} setGenre = {setGenre} setYear = {setYear} setDuration = {setDuration} setExplicit = {setExplicit}/>
        <div style={{marginTop: '3px'}}>
          <button onClick={handleAddVertex}>Add Vertex</button>
          <button onClick={ () => {canSearch()}} style={{marginLeft: '10px'}}>Search</button>
        </div>

        {go &&
        <div style={{backgroundColor: 'gray', borderRadius: '5px', marginTop: '18px'}}>
          <div style={{backgroundColor: '#070D0D', color:'white', borderRadius: '5px', fontWeight: 'bold', fontSize: '20px'}}> Songs that Sampled "{currSong}"</div>
        <div style={{display: 'flex',  marginTop: '0px'}}>
        <div id="g" style={{ margin: '0px', width: '80%', height: '95vh', backgroundColor: '#bababa', display: 'flex', borderRadius: '5px'}}> 
          <Graph
            graph={graph_}
            options={options}
            events={events}
            getNetwork={network => {}}
          />
        </div>
        <div style={{display: 'flex', borderRadius: '5px', margin: '0px', width: '50%', height: '95vh', backgroundColor: '#bababa'}}>
            {algorithm === "Dijkstra" ? 
              <div style={{display:'inline-block', alignContent: 'center', width: '100%'}}>
                 <Dijkstra backendData={backendData}/> 
               </div> : 
              <div style={{display:'inline-block', alignContent: 'center', width: '100%'}}>
                  <BFS backendData={backendData}/>
              </div>
            }
        </div>
        </div>
        </div>
        }
        
      </div>
    </div>
  );
}

export default App;
