import ControlPanelHeader from '../../components/ControlPanelHeader';
import Sidebar from '../../components/Sidebar';
import SingleGraphBox from '../../assets/SingleGraphBox';
import SensorStatusBox from '../../assets/SensorStatusBox';
import './index.css'
import { useEffect, useState } from 'react';
import api from '../../services/api';

function Reports(){

    const [graphDates, setGraphsDates] = useState(0)
    const [rainValue, setRainValue] = useState(0)
    const [deficit, setDeficit] = useState(0)

    useEffect(() => {
        async function fecthWaterbalanceData() {
            await api.get('/waterbalance', {
                headers: {"Access-Control-Allow-Origin": "*"}
            }).then(response => {
                const waterbalanceData = response.data

                setGraphsDates(waterbalanceData.map(object => object.data).slice(24,31))
                setRainValue(waterbalanceData.map(object => object.precipitacao).slice(24,31))
                setDeficit(waterbalanceData.map(object => object.deficit).slice(24,31))
            })
        }

        fecthWaterbalanceData()
    }, [])

    console.log(graphDates)

    return(
        <div id="reports">
            <Sidebar />
            <div id="reports-screen">
                <ControlPanelHeader />
                <div id="reports-info-box">
                    <div id='reports-info-box-graph-items'>
                        <SingleGraphBox 
                            headerText = 'Chuva'
                            label = 'Chuva'
                            values = {rainValue}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Deficit hídrico'
                            label = 'Deficit hídrico'
                            values = {deficit}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Reposição'
                            label = 'Reposição'
                            values = {[]}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Retirada'
                            label = 'Retirada'
                            values = {[]}
                            x_values = {graphDates}
                        />
                    </div>
                    <SensorStatusBox />
                </div>
            </div>
        </div>
    )
}

export default Reports;
