import './index.css'

function SensorStatusBox(){
    return(
        <div id="sensor-status-box">
            <div id="datetime-column">
                <div id="column-header">
                    <p id="column-header-text">Data/Hora</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">13/07/2022 17:43:42</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">13/07/2022 17:36:04</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">13/07/2022 17:28:09</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">02/07/2022 16:50:12</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">02/07/2022 16:42:02</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">02/07/2022 16:34:33</p>
                </div>
            </div>
            <div id="sensor-type-column">
                <div id="column-header">
                    <p id="column-header-text">Atividade</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô finalizou o ciclo</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô voltou para abastecer o tanque de água</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô iniciou um novo ciclo</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô finalizou o ciclo</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô voltou para abastecer o tanque de água</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">O robô iniciou um novo ciclo</p>
                </div>
            </div>
        </div>
    )
}

export default SensorStatusBox;
