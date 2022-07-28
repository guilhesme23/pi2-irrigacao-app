import SingleGraphBox from '../../assets/SingleGraphBox';
import './index.css'

function GraphBox() {
    return(
        <div id='graph-box'>
            <div id='graph-box-title'>
                <p>Relatório dos sensores</p>
            </div>
            <div id='graph-box-items'>
                <SingleGraphBox headerText='Umidade do solo'/>
                <SingleGraphBox headerText='Umidade do ar'/>
                <SingleGraphBox headerText='Temperatura do ar'/>
                <SingleGraphBox headerText='Temperatura do solo'/>
            </div>
        </div>
    )
}

export default GraphBox;
