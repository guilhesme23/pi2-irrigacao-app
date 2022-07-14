import './index.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMap, faChartPie, faFileLines } from '@fortawesome/free-solid-svg-icons';

function Sidebar() {
    return (
        <div id="sidebar">
            <div id="buttons-box">
                <button id="trajectory-button">
                    <FontAwesomeIcon id='fa-icon' icon={faMap}/>
                    <p>Trajetória</p>
                </button>
                <button id="sensors-button">
                    <FontAwesomeIcon id='fa-icon' icon={faChartPie}/>
                    <p>Sensores</p>
                </button>
                <button id="reports-button">
                    <FontAwesomeIcon id='fa-icon' icon={faFileLines}/>
                    <p>Relatórios</p>
                </button>
            </div>
        </div>
    )
}

export default Sidebar;
