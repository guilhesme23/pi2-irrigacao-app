import './index.css'
import BatteryBox from '../../assets/BatteryBox';
import TimeActivityBox from '../../assets/TimeActivityBox';
import SensorStatusBox from '../../assets/SensorStatusBox';

function DataBox() {
    return(
        <div id='data-box'>
            <BatteryBox />
            <TimeActivityBox />
            <SensorStatusBox />
        </div>
    )
}

export default DataBox;
