import React, {useState} from "react";
import './Search.css'


export const Search = ({setSongs, result, isResult, setIsResult}) => {
  //search bar component
  //input matching

  const [input, setInput] = useState("");

  

  const setResults = (value) => { 
    const inputSongs = ["Amen, Brother - The Winstons", "Think (About It) - Lyn Collins", "Change the Beat (Female Version) - Beside", "Funky Drummer - James Brown", "La Di Da Di - Doug E. Fresh and Slick Rick", "Funky President (People It's Bad) - James Brown", "Bring the Noise - Public Enemy", "Synthetic Substitution - Melvin Bliss", "Here We Go (Live at Funhouse) - Run-DMC", "Hot Pants (Bonus Beats) - Bobby Byrd", "Long Red - Mountain", "Impeach the President - The Honey Dripper", "The Champ - The Mohawks", "Apache - Incredible Bongo Band", "Kool is Back - Funk, Inc", "UFO - ESG", "It's a New Day - Skull Snaps", "Ashley's Roadclip - The Soul Searchers", "Sing a Simple Song - Sly & the Family Stone", "Take Me to the Mardi Gras - Bob James"];
    var results = [];
    if(value && !isResult) {
      results = inputSongs.filter(song => song.toLowerCase().includes(value.toLowerCase()));
    }
    setSongs(results);
    console.log(results);
  }
  const handleChange = (value) => {
    setInput(value);
    setResults(value);
    setIsResult("");
  }
  

  return(
    <div className="SearchBar">
      {isResult ? 
        (<input id="resultIn"
          placeholder= "Type name of sample..."
          value = {result}
          onChange={(e) => handleChange(input)}
      />) : 
        (<input 
          placeholder= "Type name of sample..."
          value = {input} 
          onChange={(e) => handleChange(e.target.value)}
      />)}
    </div> 
  );
};

export default Search;
