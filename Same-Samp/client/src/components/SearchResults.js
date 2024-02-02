import React, {useState} from "react";
import "./SearchResults.css";

export const SearchResults = ({songs, setResult, isResult, setIsResult}) => {
  //search result component
  //input matching
  const modifyInput = (value) => {
    console.log(value);
    setResult(value);
    setIsResult(true);
  };

  const handleChange =()=>{

  }
 

  /*style={{backgroundColor: hover ? 'gray' :'#bababa'}} 
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave} */
  

  return(
    <div className="Wrapper">
      <div  className="Results">
        {!isResult && songs.map((song, id) => 
            <div key={id} style={{cursor:"grab"}} 
            onClick={(e) => modifyInput(song)}> 
              {song} 
            </div>
        )}
      </div>
    </div>
  );
};

export default SearchResults;
