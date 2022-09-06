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
                        <SingleGraphBox 
                            headerText = 'Chuva + irrigação'
                            label = 'Chuva + irrigação'
                            values = {[80, 82, 90, 85, 86]}
                        />
                        <SingleGraphBox 
                            headerText = 'Deficit hídrico'
                            label = 'Deficit hídrico'
                            values = {[80, 82, 90, 85, 86]}
                        />
                        <SingleGraphBox 
                            headerText = 'Reposição'
                            label = 'Reposição'
                            values = {[75, 77, 79, 83, 86]}
                        />
                        <SingleGraphBox 
                            headerText = 'Retirada'
                            label = 'Retirada'
                            values = {[88, 90, 85, 83, 80]}    
                        />
                    </div>
                    <SensorStatusBox />
                </div>
            </div>
        </div>
    )
}

export default Reports;
