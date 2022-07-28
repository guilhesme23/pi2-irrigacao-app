import './index.css'
import Sidebar from "../../components/Sidebar"
import GraphBox from '../../components/GraphBox'
import ControlPanelHeader from '../../components/ControlPanelHeader'

function Data() {
    return(
        <div id="data">
            <Sidebar />
            <div id="data-screen">
                <ControlPanelHeader />
                <div id="data-info-box">
                    <GraphBox />
                </div>
            </div>
        </div>
    )
}

export default Data;
