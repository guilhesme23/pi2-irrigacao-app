import SingleGraphBox from '../../assets/SingleGraphBox';
import './index.css'

function GraphBox() {
    return(
        <div id='graph-box'>
            <SingleGraphBox headerText='Umidade do solo'/>
            <SingleGraphBox headerText='Umidade do ar'/>
            <SingleGraphBox headerText='Temperatura do ar'/>
        </div>
    )
}

export default GraphBox;
