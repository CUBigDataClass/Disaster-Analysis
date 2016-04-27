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
				console.log("Inside loop: y:" , data1 )
				console.log("Inside loop: y:" , data1[0])
				console.log("Inside loop: y:" , data1[0][1])
				console.log(typeof(data1[0][1]))
				var x = (new Date()).getTime()
				series.addPoint([x, y], true, true);	
			});
			    //sleep(2)
                            //var x = (new Date()).getTime() // current time
                                //y = Math.random();
                               // console.log("Y:", y);
                            //series.addPoint([x, y], true, true);
			/*$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/" + key , function( data1) 
			{
				//console.log(data);
				data1 = $.parseJSON(data1)
				//console.log(data[0][0],data[0][1]);
				for ( var key in data1[0][0])
				{
					//console.log(key[0]);
					dateInfo = data1[0][0][key]
				}
				console.log([new Date(dateInfo),data1[0][1]])
				series.addPoint([new Date(dateInfo),data1[0][1]],true,true);
			});
			series.addPoint([new Date(dateInfo),data[0][1]],true,true);
			console.log(series)*/
			console.log(series)
                        }, 10000);
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
                    var data = [];

			$.get("http://ec2-52-39-134-88.us-west-2.compute.amazonaws.com/getRealSecondJSON/" + key , function( data1)
                        {
                                //console.log(data);
                                data1 = $.parseJSON(data1)
                                //console.log(data[0][0],data[0][1]);
                                for ( var key in data1[0][0])
                                {
                                        //console.log(key[0]);
                                        dateInfo = data1[0][0][key]
                                }
                                console.log([new Date(dateInfo),data1[0][1]])
				data.push( [new Date(dateInfo),data1[0][1]]);
                                //series.addPoint([new Date(dateInfo),data1[0][1]],true,true);
                        }); 
			
                    return data;
                }())*/
            }]
        });
    });
})
