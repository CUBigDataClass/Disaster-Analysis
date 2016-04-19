var getGraph = (function (content) {
	"use strict",
	//console.log(content)
	data = content
	function logArrayElements(element, index, array) {
 		objects = element[0]
		for(var key in objects) {
 		   var value = objects[key];
		} 
		//console.log([new Date(value),element[1]]);
		element[0] = value
		//return [new Date(value),element[1]]
	}	
	data.forEach(logArrayElements)
	//console.log(data)
        $('#container').highcharts({
            chart: {
                zoomType: 'x'
            },
            title: {
                text: 'Disaster Analysis (keywords) against time'
            },
            subtitle: {
                text: document.ontouchstart === undefined ?
                        'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: {
                title: {
                    text: 'Number of times, the keyword occurred'
                }
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
                name: 'Disaster Analysis (Keywords against Time)',
                data: data
            }]
        
    });
});
