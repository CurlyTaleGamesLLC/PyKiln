var firingChart;

//update chart in realtime every minute, but only save logs for every 5 mins for the last fired schedule

var testdata = [{ x: 0, y: 127 }, { x: .1, y: 140 }, { x: .2, y: 135 }, { x: .5, y: 150 }];
var testdata2 = [{ x: 0, y: 200 }, { x: .1, y: 220 }, { x: .2, y: 222 }, { x: .5, y: 240 }];

export function Init(isLog) {


    let myDatasets = [];
    myDatasets.push({
            data: testdata2,
            label: "Firing Schedule",
            borderColor: "#9c27b0",
            fill: false,
            lineTension: 0.1
        }
    );

    if(isLog){
        myDatasets.push({
            data: testdata,
            label: "Actual Temperature",
            borderColor: "#ea2c6d",
            borderDash: [5, 5],
            fill: false,
            lineTension: 0.1
            }
        );
    }

    // let testDataSet = {
    //     data: testdata,
    //     label: "Actual Temperature",
    //     borderColor: "#ea2c6d",
    //     borderDash: [5, 5],
    //     fill: false,
    //     lineTension: 0.1
    // };

    firingChart = new Chart(document.getElementById("line-chart"), {
        type: 'line',
        data: {
            datasets: myDatasets
        },
        options: {
            scales: {
                xAxes: [{
                    display: true,
                    type: 'linear',
                    scaleLabel: {
                        display: true,
                        labelString: 'TIME (HOURS)'
                    },
                    ticks: {
                        stepSize: 0.5
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'TEMPERATURE °F'
                    }
                }]
            },
            // plugins: {
            //     zoom: false
            // },
            // tooltips: {
            //     mode: 'index',
            //     intersect: false,
            // },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            animation: {
                duration: 0.5
            }
        }
    });
}

// Init();

export function SetData(scheduleData) { //, actualData
    //firingChart.Chart
    console.log("TESTING!!!");

    console.log(firingChart);

    console.log(ScheduleToXY(scheduleData));

    //todo - don't display graph if 0 firing segments

    firingChart.data.datasets[0].data = ScheduleToXY(scheduleData);
    //firingChart.data.datasets[1].data = [0, 40, 10, 20, 80, 10, 200];
    //firingChart.data.labels = EveryFiveMinutes(7);
    //console.log(EveryFiveMinutes(7));
    firingChart.update();
    // firingChart.update();
    // firingChart.reset();
}

function ScheduleToXY(scheduleData) {
    let dataPoints = [{ x: 0, y: 0 }];
    let lastX = 0;
    let lastY = 0;

    for (let i = 0; i < scheduleData.length; i++) {
        lastX = lastX + (Math.abs(scheduleData[i].target - lastY) / scheduleData[i].rate);
        let newPointRamp = { x: lastX / 60, y: scheduleData[i].target };
        dataPoints.push(newPointRamp);
        lastY = scheduleData[i].target;
        lastX = lastX + scheduleData[i].hold;
        let newPointHold = { x: lastX / 60, y: scheduleData[i].target };
        dataPoints.push(newPointHold);
    }
    return dataPoints;
}

function EveryFiveMinutes(minutes) {
    let timeArray = [];
    for (let i = 0; i < minutes; i++) {
        timeArray.push(i * 5);
    }
    return timeArray;
}

function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}