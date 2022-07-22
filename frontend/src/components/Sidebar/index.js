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
                    <p>Controles</p>
                </Link>
                <Link id="sidebar-button" to='/reports'>
                    <FontAwesomeIcon id='fa-icon' icon={faFileLines}/>
                    <p>Relatórios</p>
                </Link>
            </div>
        </div>
    )
}

export default Sidebar;
