/*d3.json("data.js", function(data) 
	{*/
	//	alert("Hello")
//	});
//
/*
d3.json("",function(data)
{
	//var content = {{content|tojson}}
	console.log(keysOutput);
	console.log(valuesOutput);
})
*/
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

var chart = c3.generate({
    data: {
        columns: content
    }
});

