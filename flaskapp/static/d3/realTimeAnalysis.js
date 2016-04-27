var getGraph = (function (content,key) {
    "use strict",
    data =content
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
    $(document).ready(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });

        $('#dropdown-terms').highcharts({
            chart: {
                type: 'spline',
                animation: Highcharts.svg, // don't animate in old IE
                marginRight: 10,
                events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];
			//console.log("Series:" , series)
			var dateInfo = ""
                        setInterval(function () {
			var y = "" ;
			$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/" + key , function( data1)
			{
				data1 = $.parseJSON(data1)
				y = data1[0][1]
				var x = data1[0][0]['$date']
				series.addPoint([x, y], true, true);	
			});
			},10000);
		   }
                }
            },
            title: {
                text: 'Live random data'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                        Highcharts.numberFormat(this.y, 2);
                }
            },
            legend: {
                enabled: false
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'Random data',
                data: data
            }]
        });
    });
})
