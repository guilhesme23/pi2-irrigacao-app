import './index.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faStopwatch } from '@fortawesome/free-solid-svg-icons';

function TimeActivityBox() {
    return(
        <div id="time-activity-box">
            <div id="timer-icon-box">
                <FontAwesomeIcon id='fa-stopwatch-icon' icon={faStopwatch}/>
            </div>
            <div id="timer-status-box">
                <p id="timer-status-text">
                    Tempo de atividade
                </p>
                <p id="timer-status-value">
                    00:48:39 h
                </p>
            </div>
        </div>
    )
}

export default TimeActivityBox;
