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
                        setInterval(function () {
                            /*var x = (new Date()).getTime(), // current time
                                y = Math.random();
                            series.addPoint([x, y], true, true);*/
			/*$http({
  			method: 'GET',
  			url: '/getRealSecondJSON/' +  key
			}).then(function successCallback(response) 
			{
			   //for i in response.data:
				console.log(response.data)
			}, function errorCallback(response) {
			 });
			*/
			/*
			var xhr = new XMLHttpRequest();
			xhr.open('GET', "http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/bomb", false);
			xhr.send();
			xhr.onreadystatechange = processRequest;
			function processRequest(e) {
    				if (xhr.readyState == 4 && xhr.status == 200) {
        				var response = JSON.parse(xhr.responseText);
        				//console.log(response);
    					}
			}
			*/
			$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/bomb", function( data) 
			{
				console.log(data)
			});
                        }, 1000);
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
                /*(function () {
                    // generate an array of random data
                    var data = [],
                        time = (new Date()).getTime(),
                        i;

                    for (i = -19; i <= 0; i += 1) {
                        data.push({
                            x: time + i * 1000,
                            y: Math.random()
                        });
                    }
                    return data;
                }())*/
            }]
        });
    });
})
