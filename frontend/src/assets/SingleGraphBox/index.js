import React from 'react';
import './index.css'
import {
    Chart,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

function SingleGraphBox(props){

    Chart.register(
        CategoryScale,
        LinearScale,
        PointElement,
        LineElement,
        Title,
        Tooltip,
        Legend
    )

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: false,
                text: 'Exemplo'
            },
        },
    };

    const labels = props.x_values

    const data = {
        labels,
        datasets: [
            {
                label: props.label,
                data: props.values,
                borderColor: 'rgb(255, 0, 0)',
                backgroundColor: 'rgb(123, 123, 123)',
            },
        ]
    }

    return(
        <div id='single-graph-box'>
            <p id='graph-header'>{props.headerText}</p>
            <div id='graph-position'>
                <Line id='graph-chart-js' options={options} data={data}/>
            </div>
        </div>
    )
}

export default SingleGraphBox;
