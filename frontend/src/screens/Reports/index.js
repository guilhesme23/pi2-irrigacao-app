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
    const [evapo, setEvapo] = useState(0)
    const [surplus, setSurplus] = useState(0)

    useEffect(() => {
        async function fecthWaterbalanceData() {
            await api.get('/waterbalance', {
                headers: {"Access-Control-Allow-Origin": "*"}
            }).then(response => {
                const waterbalanceData = response.data

                setGraphsDates(waterbalanceData.map(object => object.data).slice(24,31))
                setRainValue(waterbalanceData.map(object => object.precipitacao).slice(24,31))
                setDeficit(waterbalanceData.map(object => object.deficit * -1).slice(24,31))
                setEvapo(waterbalanceData.map(object => object.etr).slice(24,31))
                setSurplus(waterbalanceData.map(object => object.excesso).slice(24,31))
            })
        }

        fecthWaterbalanceData()
    }, [])

    return(
        <div id="reports">
            <Sidebar />
            <div id="reports-screen">
                <ControlPanelHeader />
                <div id="reports-info-box">
                    <div id='reports-info-box-graph-items'>
                        <SingleGraphBox 
                            headerText = 'Chuva'
                            label = 'Chuva (mm)'
                            values = {rainValue}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Deficit hídrico'
                            label = 'Deficit hídrico (mm)'
                            values = {deficit}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Evapotranspiração'
                            label = 'Evapotranspiração (mm)'
                            values = {evapo}
                            x_values = {graphDates}
                        />
                        <SingleGraphBox 
                            headerText = 'Excedente hídrico'
                            label = 'Excedente hídrico (mm)'
                            values = {surplus}
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
