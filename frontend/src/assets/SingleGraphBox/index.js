import React from 'react';
import './index.css'

function SingleGraphBox(props){
    return(
        <div id='single-graph-box'>
            <p id='graph-header'>{props.headerText}</p>
            <div id='graph-position'></div>
        </div>
    )
}

export default SingleGraphBox;
