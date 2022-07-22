import './index.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCarBattery } from '@fortawesome/free-solid-svg-icons';

function BatteryBox(){
    return(
        <div id="battery-box">
            <div id="battery-icon-box">
                <FontAwesomeIcon id='fa-battery-icon' icon={faCarBattery}/>
            </div>
            <div id="battery-status-box">
                <p id='battery-status-text'>
                    Estado da bateria
                </p>
                <p id='battery-status-value'>
                    70%
                </p>
            </div>
        </div>
    )
}

export default BatteryBox;
