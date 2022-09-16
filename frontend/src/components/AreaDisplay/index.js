import './index.css'

function AreaDisplay(props) {
    const handleBasePositionDisplayStyle = (position) => {
        const allPositions = [1,2,3,4]

        const el = document.getElementById('base-position-'+position)
        el.style.color = '#ff0000'

        const positionsToReset = allPositions.filter(
            data => data !== parseInt(position)
        )
        for(let pos of positionsToReset){
            const e = document.getElementById('base-position-'+pos)
            e.style.color = '#000000'
        }
    }

    return (
        <div id="area-display">
            {props.updateBasePosition && handleBasePositionDisplayStyle(props.basePosition)}
            <div id="grid-block">
                <div id="top-numbers">
                    <p id="base-position-4">4</p>
                    <p id="base-position-3">3</p>
                </div>
                <div id="grid">
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                    <div id="grid-item">.</div>
                </div>
                <div id="bottom-numbers">
                    <p id="base-position-1">1</p>
                    <p id="base-position-2">2</p>
                </div>
            </div>
            <p id="sprinkler-range-text">
                Área de alcance do aspersor = 3m
            </p>
        </div>
    )
}

export default AreaDisplay;
