import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

//referenced https://mui.com/material-ui/react-table/#sticky-header 

function buildRows(json) {
  // turning JSON into string & reading JSON file and creating local Javascript Object
  var songs = json;
  console.log(songs);

  var rows =[];
  var n = 1;
  var temp;
  var nameA, nameB, nameC, nameD, nameE;
  console.log(songs.length);
  var set = new Set();
  var root = songs[0].name;

  for (let i = 1; i < songs.length; i++) { //32
    temp = songs[i].name;
    set.add(temp);
  }
  
  var uni = [];
  for(let song of set){
    uni.push(song);
  }

  for(let i = 0; i < uni.length; i+=2){
    if(i === 0){
      nameA = "Root: " + root;
    }
    else{
      nameA = n.toString() + ": " + uni[i];
      n++;
    }
    
    nameB = n.toString() + ": " + uni[i +1];
    n++;
    rows.push({name: nameA, name2: nameB});
  }

  return rows;
}


export const BFS = ({backendData}) => {
  //search result component
  //input matching
  
  const rows = buildRows(backendData);
  return(
    <TableContainer style={{backgroundColor: '#bababa', maxHeight:'95vh'}}component={Paper}>
      <Table sx={{ maxWidth: 800}} aria-label="simple table">
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="center" style={{padding: '10px'}} component="th" scope="row"> {row.name} </TableCell>
              <TableCell align="center">{row.name2}</TableCell>
              
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default BFS;