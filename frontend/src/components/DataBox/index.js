import './index.css'
import BatteryBox from '../../assets/BatteryBox';
import TimeActivityBox from '../../assets/TimeActivityBox';

function DataBox() {
    return(
        <div id='data-box'>
            <BatteryBox />
            <TimeActivityBox />
            <div id="sensor-status-box"></div>
        </div>
    )
}

export default DataBox;
