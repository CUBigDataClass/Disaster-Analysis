/*d3.json("data.js", function(data) 
	{*/
	//	alert("Hello")
//	});
//

d3.json("",function(data)
{
//	console.log(data);
	console.log(keysOutput);
	console.log(valuesOutput);
  $('#container').highcharts({
            chart: {
                zoomType: 'x'
            },
            title: {
                text: 'Frequency of Disaster Related Terms'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
            },
            xAxis: {
		categories: keysOutput 
            },
            yAxis: {
                title: {
                    text: 'Frequency of Terms'
                },
		min:0
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },

            series: [{
                type: 'area',
                name: 'number of times term was tweeted in the last 10 minutes!',
                data: valuesOutput
            }]
        });
    });
	//var content = {{content|tojson}}
//	console.log(keysOutput);
//	console.log(valuesOutput);
//})


//y
/*
var chart = c3.generate({
    bindto: '#chart',
    data: {
      columns: [
        ['data1', 30, 200, 100, 400, 150, 250],
        ['data2', 50, 20, 10, 40, 15, 25]
      ]
    }
});
*/

