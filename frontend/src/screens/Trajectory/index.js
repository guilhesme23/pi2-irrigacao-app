import './index.css'
import Sidebar from '../../components/Sidebar'
import AreaPropertiesForm from '../../components/AreaPropertiesForm'
import AreaDisplay from '../../components/AreaDisplay'
import ControlPanelHeader from '../../components/ControlPanelHeader'

function Trajectory() {
    return (
        <div id="trajectory">
            <Sidebar />
                <div id="trajectory-screen">
                    <ControlPanelHeader />
                    <div id="area-info-box">
                        <AreaPropertiesForm />
                        <AreaDisplay />
                    </div>
                </div>
        </div>
    )
}

export default Trajectory;
