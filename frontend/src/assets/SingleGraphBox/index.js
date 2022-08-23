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
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Exemplo'
            },
        },
    };

    const labels = ['A', 'B', 'C']

    const data = {
        labels,
        datasets: [
            {
                label: 'Dataset 1',
                data: [1, 2, 3],
                borderColor: 'rgb(255, 0, 0)',
                backgroundColor: 'rgb(123, 123, 123)',
            },
        ]
    }

    return(
        <div id='single-graph-box'>
            <p id='graph-header'>{props.headerText}</p>
            <div id='graph-position'>
                <Line options={options} data={data}/>
            </div>
        </div>
    )
}

export default SingleGraphBox;
