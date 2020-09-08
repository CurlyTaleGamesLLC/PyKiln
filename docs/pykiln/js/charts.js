////GRAPH DATA

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