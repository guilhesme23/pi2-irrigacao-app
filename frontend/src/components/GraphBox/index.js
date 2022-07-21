import './index.css'

function GraphBox() {
    return(
        <div id='graph-box'>
            <div id='single-graph-box'>
                <p id='graph-header'>Umidade do solo</p>
                <div id='graph-position'></div>
            </div>
            <div id='single-graph-box'>
                <p id='graph-header'>Umidade do ar</p>
                <div id='graph-position'></div>
            </div>
            <div id='single-graph-box'>
                <p id='graph-header'>Temperatura do ar</p>
                <div id='graph-position'></div>
            </div>
        </div>
    )
}

export default GraphBox;
