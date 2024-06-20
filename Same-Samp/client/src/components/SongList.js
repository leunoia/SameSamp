// src/components/SongList.js
import React from 'react';

const SongList = ({ songs }) => {
  return (
    <div className="song-list">
      <h3 className="SongTitle">Most Similar Songs</h3>
      <ul>
        {songs.map((song, index) => (
          <li key={index}>
            <strong>{song.name}</strong>: {song.weight.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SongList;
