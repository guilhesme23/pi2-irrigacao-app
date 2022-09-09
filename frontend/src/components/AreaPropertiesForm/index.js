import './index.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCompass } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react'
import api from '../../services/api'

function AreaPropertiesForm(props) {
    const [fieldWidth, setFieldWidth] = useState(0)
    const [fieldLength, setFieldLength] = useState(0)

    const calculateRoute = async () => {
        await api.post("/fields", {
            "width": fieldWidth,
            "length": fieldLength
        }).then(response => {
            console.log(response);
        }).catch(err => {
            console.error(err)
        })
    }

    const setIrrigationStatus = value => {
        api.post("/commands/irrigate", {
            "irrigate": value
        }).then(response => {
            console.log(response)
        }).catch(error => {
            console.error(error)
        })
    }

    const startIrrigation = () => {
        setIrrigationStatus(true)
    }

    const stopIrrigation = () => {
        setIrrigationStatus(false)
    }

    return (
        <div id='area-properties'>
            <div id='area-properties-box'>
                <div id="area-properites-box-title">
                    <p>Grid Layout</p>
                </div>
                <div id='area-property-box'>
                    <p>Largura (m)</p>
                    <input 
                        id="area-text-box"
                        onChange={event => setFieldWidth(event.target.value)}
                    />
                </div>
                <div id='area-property-box'>
                    <p>Comprimento (m)</p>
                    <input 
                        id="area-text-box" 
                        onChange={event => setFieldLength(event.target.value)}
                    />
                </div>
                <div id='area-property-box'>
                    <p>Posição da base</p>
                    <select id="base-position-selection" 
                        onChange={(event) => {
                            props.setBasePosition(event.target.value)
                            props.setUpdateBasePosition(true)
                    }}>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
                <div id="area-property-buttons">
                    <div id="calculate-route-button">
                        <button>
                            <FontAwesomeIcon id='fa-icon-compass' icon={faCompass}/>
                            Calcular rota
                        </button>
                    </div>
                    <div id="start-stop-buttons">
                        <button onClick={startIrrigation}>
                            Iniciar rota
                        </button>
                        <button onClick={stopIrrigation}>
                            Parar rota
                        </button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default AreaPropertiesForm;
