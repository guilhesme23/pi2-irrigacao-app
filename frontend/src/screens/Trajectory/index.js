import './index.css'
import Sidebar from '../../components/Sidebar'
import AreaPropertiesForm from '../../components/AreaPropertiesForm'
import AreaDisplay from '../../components/AreaDisplay'

function Trajectory() {
    return (
        <div id="trajectory">
            <Sidebar />
            <AreaPropertiesForm />
            <AreaDisplay />
        </div>
    )
}

export default Trajectory;
