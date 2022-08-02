import './index.css'
import Sidebar from '../../components/Sidebar'
import AreaPropertiesForm from '../../components/AreaPropertiesForm'
import AreaDisplay from '../../components/AreaDisplay'
import ControlPanelHeader from '../../components/ControlPanelHeader'
import { useState } from 'react'

function Trajectory() {
    const [basePosition, setBasePosition] = useState(1)
    const [updateBasePosition, setUpdateBasePosition] = useState(false)

    return (
        <div id="trajectory">
            <Sidebar />
                <div id="trajectory-screen">
                    <ControlPanelHeader />
                    <div id="area-info-box">
                        <AreaPropertiesForm 
                            setBasePosition={setBasePosition}
                            setUpdateBasePosition={setUpdateBasePosition}
                        />
                        <AreaDisplay basePosition={basePosition} 
                            updateBasePosition={updateBasePosition}
                            setUpdateBasePosition={setUpdateBasePosition}
                        />
                    </div>
                </div>
        </div>
    )
}

export default Trajectory;
