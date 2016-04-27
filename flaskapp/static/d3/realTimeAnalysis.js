var getGraph = (function (content,content1, key) {
    "use strict",
    data20 = content
    data10 = content1
    function logArrayElements(element, index, array) {
        objects = element[0]
        for(var key in objects) {
           var value = objects[key];
        } 
                element[0] = value
       }   
        
    data20.forEach(logArrayElements)
    data10.forEach(logArrayElements)
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
			var series1 = this.series[1];
	
                        setInterval(function () {
			$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/" + key , function( data1)
			{
				data1 = $.parseJSON(data1)
				y = data1[0][1]
				var x = data1[0][0]['$date']
				//series.addPoint([x, y], true, true);	
			
			$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSONML/" + key , function( data2)
			{
				data2 = $.parseJSON(data2)
				y1 = data2[0][1]
				var x1 = data2[0][0]['$date']
				series.addPoint([x, y], true, true);
				series1.addPoint([x1, y1], true, true);
			});
			})
			},10000);
		   }
                }
            },
            title: {
                text: 'Real Time Keyword Count'
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
                name: 'Keyword count without ML',
                data: data20
            },{
		name: 'Keyword count with ML', 
		data: data10
	    }]
        });
    });
})
