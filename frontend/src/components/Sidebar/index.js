import './index.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMap, faChartPie, faFileLines } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';

function Sidebar() {
    return (
        <div id="sidebar">
            <div id="buttons-box">
                <Link id="sidebar-button" to='/'>
                    <FontAwesomeIcon id='fa-icon' icon={faMap}/>
                    <p>Trajetória</p>
                </Link>
                <Link id="sidebar-button" to='/data'>
                    <FontAwesomeIcon id='fa-icon' icon={faChartPie}/>
                    <p>Sensores</p>
                </Link>
                <button id="sidebar-button">
                    <FontAwesomeIcon id='fa-icon' icon={faFileLines}/>
                    <p>Relatórios</p>
                </button>
            </div>
        </div>
    )
}

export default Sidebar;
