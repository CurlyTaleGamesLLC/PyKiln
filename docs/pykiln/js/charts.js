
// var timeFormat = 'MM/DD/YYYY HH:mm';

// function newDate(days) {
//     return moment().add(days, 'd').toDate();
// }

// function newDateString(days) {
//     return moment().add(days, 'd').format(timeFormat);
// }

// var color = Chart.helpers.color;
// var config = {
//     type: 'line',
//     data: {
//         labels: [ // Date Objects
//             newDate(0),
//             newDate(1),
//             newDate(2),
//             newDate(3),
//             newDate(4),
//             newDate(5),
//             newDate(6)
//         ],
//         datasets: [{
//             label: 'My First dataset',
//             backgroundColor: color(window.chartColors.red).alpha(0.5).rgbString(),
//             borderColor: window.chartColors.red,
//             fill: false,
//             data: [
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor()
//             ],
//         }, {
//             label: 'My Second dataset',
//             backgroundColor: color(window.chartColors.blue).alpha(0.5).rgbString(),
//             borderColor: window.chartColors.blue,
//             fill: false,
//             data: [
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor(),
//                 randomScalingFactor()
//             ],
//         }, {
//             label: 'Dataset with point data',
//             backgroundColor: color(window.chartColors.green).alpha(0.5).rgbString(),
//             borderColor: window.chartColors.green,
//             fill: false,
//             data: [{
//                 x: newDateString(0),
//                 y: randomScalingFactor()
//             }, {
//                 x: newDateString(5),
//                 y: randomScalingFactor()
//             }, {
//                 x: newDateString(7),
//                 y: randomScalingFactor()
//             }, {
//                 x: newDateString(15),
//                 y: randomScalingFactor()
//             }],
//         }]
//     },
//     options: {
//         title: {
//             text: 'Chart.js Time Scale'
//         },
//         scales: {
//             xAxes: [{
//                 type: 'time',
//                 time: {
//                     parser: timeFormat,
//                     // round: 'day'
//                     tooltipFormat: 'll HH:mm'
//                 },
//                 scaleLabel: {
//                     display: true,
//                     labelString: 'Date'
//                 }
//             }],
//             yAxes: [{
//                 scaleLabel: {
//                     display: true,
//                     labelString: 'value'
//                 }
//             }]
//         },
//     }
// };



// document.getElementById('randomizeData').addEventListener('click', function () {
//     config.data.datasets.forEach(function (dataset) {
//         dataset.data.forEach(function (dataObj, j) {
//             if (typeof dataObj === 'object') {
//                 dataObj.y = randomScalingFactor();
//             } else {
//                 dataset.data[j] = randomScalingFactor();
//             }
//         });
//     });

//     window.myLine.update();
// });

// var colorNames = Object.keys(window.chartColors);
// document.getElementById('addDataset').addEventListener('click', function () {
//     var colorName = colorNames[config.data.datasets.length % colorNames.length];
//     var newColor = window.chartColors[colorName];
//     var newDataset = {
//         label: 'Dataset ' + config.data.datasets.length,
//         borderColor: newColor,
//         backgroundColor: color(newColor).alpha(0.5).rgbString(),
//         data: [],
//     };

//     for (var index = 0; index < config.data.labels.length; ++index) {
//         newDataset.data.push(randomScalingFactor());
//     }

//     config.data.datasets.push(newDataset);
//     window.myLine.update();
// });

// document.getElementById('addData').addEventListener('click', function () {
//     if (config.data.datasets.length > 0) {
//         config.data.labels.push(newDate(config.data.labels.length));

//         for (var index = 0; index < config.data.datasets.length; ++index) {
//             if (typeof config.data.datasets[index].data[0] === 'object') {
//                 config.data.datasets[index].data.push({
//                     x: newDate(config.data.datasets[index].data.length),
//                     y: randomScalingFactor(),
//                 });
//             } else {
//                 config.data.datasets[index].data.push(randomScalingFactor());
//             }
//         }

//         window.myLine.update();
//     }
// });

// document.getElementById('removeDataset').addEventListener('click', function () {
//     config.data.datasets.splice(0, 1);
//     window.myLine.update();
// });

// document.getElementById('removeData').addEventListener('click', function () {
//     config.data.labels.splice(-1, 1); // remove the label first

//     config.data.datasets.forEach(function (dataset) {
//         dataset.data.pop();
//     });

//     window.myLine.update();
// });


////GRAPH DATA
window.onload = function () {
    LoadChart();
};

function LoadChart() {
    $.getJSON("api/get-chart", function (result) {
      console.log(result);
      LoadLineGraph(result['start-time'], result['temp-log'], result['schedule-log']);
    });
}

function newDate(mins) {
    return moment().add(mins, 'm').toDate();
}

function TimeRange(startTime, values){
    var startValue = moment(startTime, 'YYYY/MM/DD HH:mm:ss');
    var range = [];
    for(var i = 0; i < values; i++){
        range.push(startValue.add(1, 'm').toDate());
    }
    return range;
}


function LoadLineGraph(startTime, actual, scheduled) {
    var ctx = document.getElementById('canvas').getContext('2d');
    var pointSize = 5;
    var jsonData = {};

    jsonData['time'] = TimeRange(startTime, actual.length);
    console.log(jsonData['time'][0]);
    jsonData['scheduled'] = scheduled;
    jsonData['actual'] = actual;

    //jsonData['scheduled'] = [0,1,2,3,4,5,6,7,8,9];
    //jsonData['actual'] = [0,3,2,5,3,2,1,2,5,8];

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: jsonData['time'],
            datasets: [{
                label: 'Scheduled',
                fill: false,
                borderColor: 'rgb(0, 105, 217)',
                borderDash: [5, 5],
                pointBorderWidth: pointSize,
                pointHitRadius: pointSize * 2,
                data: jsonData['scheduled']
            }, {
                label: 'Actual',
                fill: false,
                borderColor: 'rgb(220, 53, 69)',
                pointBorderWidth: pointSize,
                pointHitRadius: pointSize * 2,
                data: jsonData['actual']
            }
            ]
        },

        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }],
                yAxes: [{
                  scaleLabel: {
                    display: true,
                    labelString: 'Temperature'
                  }
                }]
              }     
        }
    });
}