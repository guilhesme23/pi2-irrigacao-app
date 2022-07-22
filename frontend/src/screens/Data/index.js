import './index.css'
import Sidebar from "../../components/Sidebar"
import DataBox from "../../components/DataBox"
import GraphBox from '../../components/GraphBox'

function Data() {
    return(
        <div id="data">
            <Sidebar />
            <DataBox />
            <GraphBox />
        </div>
    )
}

export default Data;
