import React, { Component, useState } from 'react'

import { Selectable } from "@robertz65/lyte";

import { SimpleDropdown } from 'react-js-dropdavn'
import 'react-js-dropdavn/dist/index.css'
import './DropDown.css'


const genre = [
  {label: 'Genre', value: 1},
  {label: 'Electronic / Dance', value: 2},
  {label: 'HipHop / Rap / R&B', value: 3},
  {label: 'Rock / Pop', value: 4},
  {label: 'Other', value: 5},
  {label: 'SoundTrack / Library', value: 6},
  {label: 'Soul / Funk / Disco', value: 7},
  {label: 'Jazz / Blues', value: 8},
  {label: 'Reggae / Dub', value: 9},
  {label: 'Country / Folk', value: 10},
  {label: 'World / Latin', value: 11},
  {label: 'Classical', value: 12}
]

const instrument = [
  {label: 'Instrument', value: 1},
  {label: 'Drums', value: 2},
  {label: 'Hook / Riff', value: 3},
  {label: 'Multi-Element', value: 4},
  {label: 'Vocals / Lyrics', value: 5},
  {label: 'Score', value: 6},
  {label: 'Base', value: 7},
  {label: 'Sound Effect / Other', value: 8}
]
var year = [];
var val = 1;
year.push({content: 'Year', label: val})
val++;
const years = "190019011902190319041905190619071908190919101911191219131914191519161917191819191920192119221923192419251926192719281929193019311932193319341935193619371938193919401941194219431944194519461947194819491950195119521953195419551956195719581959196019611962196319641965196619671968196919701971197219731974197519761977197819791980198119821983198419851986198719881989199019911992199319941995199619971998199920002001200220032004200520062007200820092010201120122013201420152016201720182019202020212022";
for (let i = years.length; i >= 0; i -= 4) {
  var temp = years.substring(i, i - 4);
  year.push({content: temp, label: val})
  val++;
}

export const DropDown=({setInst, setAlg, setGenre, setYear, setDuration, setExplicit}) =>{
  const [input1, setInput1] = useState("");
  const [input2, setInput2] = useState("");
  
  const getInst=(values)=>{
    setInst(values[0].label);
    console.log(values[0].label);
  };
  const getYear=(value)=>{
    //setYear(values[0].content);
    setInput2(value);
    console.log(value);
    if(value.length == 4){
      setYear(value);
    }
  };
  const getGenre=(values)=>{
    setGenre(values[0].label);
    console.log(values[0].label);
  };
  const getAlg=(values)=>{
    setAlg(values[0].content);
    console.log(values[0].content);
  };
  const getDuration =(value)=>{
    setInput1(value);
    console.log(value);
    setDuration(value);
  }
  const getExplicit=(values)=>{
    setExplicit(values[0].content);
    console.log(values);
  }

  
  return (
      <div style={{display: 'inline-block', marginTop:'25px'}}>
        <div style={{display: 'inline-block', boxShadow: '5px 10px #888888', borderRadius: '10px'}}>
          <Selectable 
            width={200}
            allowClear
            allowRefill
            defaultValue={"Genre"}
            options={genre}
            onChange={(values) => getGenre(values)}
          />
        </div>
      
        <div style={{position:'sticky', display: 'inline-block', boxShadow: '5px 10px #888888', borderRadius: '10px'}}>
           <Selectable
            width={200}
            allowClear
            allowRefill
            options={instrument}
            defaultValue={"Instrument"}
            onChange={(values) => getInst(values)}
          />
        </div>
        <div style={{position:'sticky', display: 'inline-block', boxShadow: '5px 10px #888888', borderRadius: '10px'}}>
          <Selectable
            width={200}
            allowClear
            allowRefill
            options={[{label: 1, content: "Algorithm"}, {label: 2, content: "Dijkstra"}, {label: 3, content: "Breadth First Search"}]}
            defaultValue={"Algorithm"}
            onChange={(values) => getAlg(values)}
          />
        </div>
        <div style={{position:'sticky', display: 'inline-block', boxShadow: '5px 10px #888888', borderRadius: '10px'}}>
          <Selectable
            width={200}
            allowClear
            allowRefill
            options={[{label: 1, content: "Content"}, {label: 2, content: "Non-Explicit"}, {label: 3, content: "Explicit"}]}
            defaultValue={"Content"}
            onChange={(values) => getExplicit(values)}
          />
        </div>
        <div style={{margin: '15px'}}>
          <input id='year'style = {{fontWeight: '350', 
            color: '#303030',
            fontFamily: 'arial',
            fontSize: '16px', width:'200px', backgroundColor: 'white', height: '25px', borderRadius: '5px'}} placeholder='Year'  value ={input2} onChange={(e)=> getYear(e.target.value)}/>
          <input id='duration' style = {{fontWeight: '350', 
            color: '#303030',
            fontFamily: 'arial',
            fontSize: '16px', width:'200px', backgroundColor: 'white', height: '25px', borderRadius: '5px'}} placeholder='Duration (s)' value ={input1} onChange={(e)=> getDuration(e.target.value)}/>
        </div>
      
      </div>
      );
      
  
};

export default DropDown;
/*<div style={{position:'sticky', display: 'inline-block' , boxShadow: '5px 10px #888888', borderRadius: '10px'}}>
            <Selectable 
              width={200}
              allowClear
              allowRefill
              options={year}
              defaultValue={"Year"}
              onChange={(values) => getYear(values)}
            />
        </div>*/