import ControlPanelHeader from '../../components/ControlPanelHeader';
import Sidebar from '../../components/Sidebar';
import SingleGraphBox from '../../assets/SingleGraphBox';
import SensorStatusBox from '../../assets/SensorStatusBox';
import './index.css'

function Reports(){
    return(
        <div id="reports">
            <Sidebar />
            <div id="reports-screen">
                <ControlPanelHeader />
                <div id="reports-info-box">
                    <div id='reports-info-box-graph-items'>
                        <SingleGraphBox headerText='Chuva + irrigação'/>
                        <SingleGraphBox headerText='Deficit hídrico'/>
                        <SingleGraphBox headerText='Reposição'/>
                        <SingleGraphBox headerText='Retirada'/>
                    </div>
                    <SensorStatusBox />
                </div>
            </div>
        </div>
    )
}

export default Reports;
