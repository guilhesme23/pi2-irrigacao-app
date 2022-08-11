import './index.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBell, faBatteryHalf } from '@fortawesome/free-solid-svg-icons'


function ControlPanelHeader() {
    return(
        <div id='control-panel-header'>
            <div id="control-panel-title-box">
                <p>Painel de controle</p>
            </div>
            <div id="control-panel-items-box">
                <FontAwesomeIcon id="fa-bell" icon={faBell}/>
                <div id="control-panel-temperature-info">
                    <p>Temperatura: 23 °C</p>
                </div>
                <div id="control-panel-moisture-info">
                    <p>Umidade: 45 %</p>
                </div>
                <FontAwesomeIcon id="fa-battery-half" icon={faBatteryHalf} />
            </div>
        </div>
    )
}

export default ControlPanelHeader;
