import './index.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCompass } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react'
import api from '../../services/api'

function AreaPropertiesForm(props) {
    const [fieldWidth, setFieldWidth] = useState(0)
    const [fieldLength, setFieldLength] = useState(0)
    const [basePosX, setBasePosX] = useState(0)
    const [basePosY, setBasePosY] = useState(0)

    const calculateRoute = async () => {
        console.log("Creating field!")
        try {
            let res = await api.post('/fields', {
                width: fieldWidth,
                length: fieldLength
            }, {
                headers: {"Access-Control-Allow-Origin": "*"}
            })

            console.log(res.data.id)
            let trajectory = await api.post('/trajectory', {
                field_id: res.data.id,
                base_pos_x: basePosX,
                base_pos_y: basePosY
            }, {
                headers: {"Access-Control-Allow-Origin": "*"}
            })
            console.log(trajectory)
        } catch (error) {
            console.log(error)
        }
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

    const generateBasePosCoordinates = (value) => {
        switch (value) {
            case '1':
                setBasePosX(0)
                setBasePosY(0)
                break;

            case '2':
                setBasePosX(1)
                setBasePosY(0)
                break;
        
            case '3':
                setBasePosX(1)
                setBasePosY(1)
                break;

            case '4':
                setBasePosX(0)
                setBasePosY(1)
                break;

            default:
                break;
        }
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
                            generateBasePosCoordinates(event.target.value)
                    }}>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
                <div id="area-property-buttons">
                    <div id="calculate-route-button">
                        <button onClick={calculateRoute}>
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
