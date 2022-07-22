import './index.css'

function SensorStatusBox(){
    return(
        <div id="sensor-status-box">
            <div id="datetime-column">
                <div id="column-header">
                    <p id="column-header-text">Data/Hora</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">1</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">2</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">3</p>
                </div>
            </div>
            <div id="sensor-type-column">
                <div id="column-header">
                    <p id="column-header-text">Tipo</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">Umidade Solo</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">Umidade Ar</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">Temperatura Ar</p>
                </div>
            </div>
        </div>
    )
}

export default SensorStatusBox;
