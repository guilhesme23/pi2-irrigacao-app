import { useEffect, useState } from 'react';
import SingleGraphBox from '../../assets/SingleGraphBox';
import './index.css'
import api from '../../services/api';

function GraphBox() {
    const [graphsData, setGraphsData] = useState({})

    useEffect(() => {
        async function fetchApi() {
            await api.get("/sensors", {
                headers: {"Access-Control-Allow-Origin": "*"}
            }).then(response => {
                const data = response.data;
                setGraphsData(data)
            })
        }
        fetchApi()
    }, [])

    const umidade_solo = Object.values(graphsData).map(sensors => sensors.humidity_soil)
    const umidade_ar = Object.values(graphsData).map(sensors => sensors.humidity_air)
    const temperatura_ar = Object.values(graphsData).map(sensors => sensors.temp_air)
    const temperatura_solo = Object.values(graphsData).map(sensors => sensors.temp_soil)
    const data_coleta = Object.values(graphsData).map(sensors => new Date(sensors.recorded_on).toLocaleDateString())

    return(
        <div id='graph-box'>
            <div id='graph-box-title'>
                <p>Relatório dos sensores</p>
            </div>
            { graphsData && <div id='graph-box-items'>
                <SingleGraphBox 
                    headerText='Umidade do solo (%)'
                    label = 'Umidade'
                    values = {umidade_solo}
                    x_values = {data_coleta}
                />
                <SingleGraphBox 
                    headerText='Umidade do ar (%)'
                    label = 'Umidade'
                    values = {umidade_ar}
                    x_values = {data_coleta}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do ar (°C)'
                    label = 'Temperatura'
                    values = {temperatura_ar}
                    x_values = {data_coleta}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do solo (°C)'
                    label = 'Temperatura'
                    values = {temperatura_solo}
                    x_values = {data_coleta}
                />
            </div>}
        </div>
    )
}

export default GraphBox;
