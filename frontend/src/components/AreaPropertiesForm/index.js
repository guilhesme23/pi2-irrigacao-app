import './index.css'

function AreaPropertiesForm(props) {

    return (
        <div id='area-properties'>
            <div id='area-properties-box'>
                <div id="area-properites-box-title">
                    <p>Grid Layout</p>
                </div>
                <div id='area-property-box'>
                    <p>Largura (m)</p>
                    <input id="area-text-box"></input>
                </div>
                <div id='area-property-box'>
                    <p>Comprimento (m)</p>
                    <input id="area-text-box"></input>
                </div>
                <div id='area-property-box'>
                    <p>Posição da base</p>
                    <select id="base-position-selection" 
                        onChange={(event) => {
                            props.setBasePosition(event.target.value)
                            props.setUpdateBasePosition(true)
                    }}>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                    </select>
                </div>
            </div>
        </div>
    )
}

export default AreaPropertiesForm;
