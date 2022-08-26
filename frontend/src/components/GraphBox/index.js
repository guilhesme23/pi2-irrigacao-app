import SingleGraphBox from '../../assets/SingleGraphBox';
import './index.css'

function GraphBox() {
    return(
        <div id='graph-box'>
            <div id='graph-box-title'>
                <p>Relatório dos sensores</p>
            </div>
            <div id='graph-box-items'>
                <SingleGraphBox 
                    headerText='Umidade do solo (%)'
                    label = 'Umidade'
                    values = {[20, 18, 19, 20, 20]}
                />
                <SingleGraphBox 
                    headerText='Umidade do ar (%)'
                    label = 'Umidade'
                    values = {[35, 33.5, 35, 34, 35]}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do ar (°C)'
                    label = 'Temperatura'
                    values = {[28.5, 29, 27.5, 26, 27]}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do solo (°C)'
                    label = 'Temperatura'
                    values = {[22, 22.5, 22, 21, 21]}
                />
            </div>
        </div>
    )
}

export default GraphBox;
