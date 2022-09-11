import { useEffect, useState } from 'react';
import api from '../../services/api';
import './index.css'

function SensorStatusBox(){

    const [reportsDates, setReportsDates] = useState([])
    const [reportsStatus, setReportsStatus] = useState([])

    useEffect(() => {
        const fetchReportsData = async () => {
            await api.get('/reports', {
                headers: {"Access-Control-Allow-Origin": "*"}
            }).then(response => {
                const reportsData = response.data

                setReportsDates(reportsData.map(
                    object => [
                        new Date(object.recorded_on).toLocaleDateString(),
                        new Date(object.recorded_on).toLocaleTimeString()
                    ]
                ))

                setReportsStatus(reportsData.map(object => object.status_report))
            })
        }

        fetchReportsData()
    }, [reportsDates])

    const generateReportString = (status_report) => {
        switch (status_report) {
            case 'INIT_CYCLE':
                return "O veículo iniciou o ciclo"

            case 'END_CYCLE':
                return "O veículo finalizou o ciclo"

            case 'LOW_BATERY':
                return "O veículo está com pouca bateria"

            default:
                return 'Status não identificado'
        }
    }

    return(
        <div id="sensor-status-box">
            <div id="datetime-column">
                <div id="column-header">
                    <p id="column-header-text">Data/Hora</p>
                </div>
                {
                    reportsDates.map(object => (
                        <div id="column-item">
                            <p id="column-item-text">
                                {
                                    object !== undefined ? 
                                    `${object[0]}, ${object[1]}` :
                                    null
                                }
                            </p>
                        </div>
                    ))
                }
            </div>
            <div id="sensor-type-column">
                <div id="column-header">
                    <p id="column-header-text">Atividade</p>
                </div>
                {
                    reportsStatus.map(object => (
                        <div id="column-item">
                            <p id="column-item-text">
                                {generateReportString(object)}
                            </p>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}

export default SensorStatusBox;
