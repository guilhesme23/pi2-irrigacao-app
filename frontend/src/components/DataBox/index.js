import './index.css'
import BatteryBox from '../../assets/BatteryBox';

function DataBox() {
    return(
        <div id='data-box'>
            <BatteryBox />
            <div id="time-activity-box"></div>
            <div id="sensor-status-box"></div>
        </div>
    )
}

export default DataBox;
