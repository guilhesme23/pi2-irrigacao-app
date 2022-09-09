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
    }, [])

    return(
        <div id="sensor-status-box">
            <div id="datetime-column">
                <div id="column-header">
                    <p id="column-header-text">Data/Hora</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">
                        {reportsDates[0][0]}, {reportsDates[0][1]}
                    </p>
                </div>
            </div>
            <div id="sensor-type-column">
                <div id="column-header">
                    <p id="column-header-text">Atividade</p>
                </div>
                <div id="column-item">
                    <p id="column-item-text">
                        {
                            reportsStatus[0] === 'INIT_CYCLE' ? 
                                "O veículo iniciou o cíclo" : 
                                "Status não identificado"
                        }
                    </p>
                </div>
            </div>
        </div>
    )
}

export default SensorStatusBox;
