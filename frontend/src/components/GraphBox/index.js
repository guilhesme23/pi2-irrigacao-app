import { useEffect, useState } from 'react';
import SingleGraphBox from '../../assets/SingleGraphBox';
import './index.css'
import api from '../../services/api';

function GraphBox() {
    const [graphsData, setGraphsData] = useState({})

    useEffect(() => {
        api.get("/sensors", {
            headers: {"Access-Control-Allow-Origin": "*"}
        }).then(response => {
            console.log('resposta => ' + response)
            const data = response.data;
            setGraphsData(data)
        })
    }, [])

    const umidade_solo = graphsData[0] && Object.values(graphsData[0])[3]
    const umidade_ar = graphsData[0] && Object.values(graphsData[0])[2]
    const temperatura_ar = graphsData[0] && Object.values(graphsData[0])[0]
    const temperatura_solo = graphsData[0] && Object.values(graphsData[0])[1]
    const data_coleta = new Date(graphsData[0] && Object.values(graphsData[0])[4])
        .toLocaleDateString()

    return(
        <div id='graph-box'>
            <div id='graph-box-title'>
                <p>Relatório dos sensores</p>
            </div>
            { graphsData && <div id='graph-box-items'>
                <SingleGraphBox 
                    headerText='Umidade do solo (%)'
                    label = 'Umidade'
                    values = {[
                        umidade_solo
                    ]}
                    x_values = {[
                        data_coleta
                    ]}
                />
                <SingleGraphBox 
                    headerText='Umidade do ar (%)'
                    label = 'Umidade'
                    values = {[
                        umidade_ar
                    ]}
                    x_values = {[
                        data_coleta
                    ]}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do ar (°C)'
                    label = 'Temperatura'
                    values = {[
                        temperatura_ar
                    ]}
                    x_values = {[
                        data_coleta
                    ]}
                />
                <SingleGraphBox 
                    headerText = 'Temperatura do solo (°C)'
                    label = 'Temperatura'
                    values = {[
                        temperatura_solo
                    ]}
                    x_values = {[
                        data_coleta
                    ]}
                />
            </div>}
        </div>
    )
}

export default GraphBox;
