import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

//referenced https://mui.com/material-ui/react-table/#sticky-header 

function buildRows(json) {
  // turning JSON into string & reading JSON file and creating local Javascript Object
  var jsonstring = JSON.stringify(json)
  var songsObj = JSON.parse(jsonstring);
  var songs = songsObj;
  var rows = [];

  for(var key in songs){
    if(rows.length > 30){
      break;
    }
    else{
      rows.push({name: key, distance: songs[key][0]})
    }
    
  }
  
  return rows;
}


export const Dijkstra = ({backendData}) => {
  //search result component
  //input matching
  const rows = buildRows(backendData);

  return(
    <TableContainer style={{backgroundColor: '#bababa', maxHeight:'95vh'}}component={Paper}>
      <Table sx={{ maxWidth: 500}} aria-label="simple table">
        <TableHead>
          <TableRow style={{backgroundColor: 'gray'}}>
            <TableCell style={{fontWeight: 'bold'}}>Song Name</TableCell>
            <TableCell style={{fontWeight: 'bold'}} align="right">Distance From Most Similar Song</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row"> {row.name} </TableCell>
              <TableCell align="right">{row.distance}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default Dijkstra;