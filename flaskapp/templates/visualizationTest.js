var w = 600;
var h = 250;

var dataset = [ 
	{ key: 0, value: 5 },
	{ key: 1, value: 10 },
	{ key: 2, value: 13 },
	{ key: 3, value: 19 },
	{ key: 4, value: 21 },
	{ key: 5, value: 25 },
	{ key: 6, value: 22 },
	{ key: 7, value: 18 },
	{ key: 8, value: 15 },
	{ key: 9, value: 13 },
	{ key: 10, value: 11 },
	{ key: 11, value: 12 },
	{ key: 12, value: 15 },
	{ key: 13, value: 20 },
	{ key: 14, value: 18 },
	{ key: 15, value: 17 },
	{ key: 16, value: 16 },
	{ key: 17, value: 18 },
	{ key: 18, value: 23 },
	{ key: 19, value: 25 } ];

var xScale = d3.scale.ordinal()
				.domain(d3.range(dataset.length))
				.rangeRoundBands([0, w], 0.05); 

var yScale = d3.scale.linear()
				.domain([0, d3.max(dataset, function(d) {return d.value;})])
				.range([0, h]);

var key = function(d) {
	return d.key;
};

var svg = d3.select("body")
			.append("svg")
			.attr("width", w)
			.attr("height", h);

svg.selectAll("rect")
   .data(dataset, key)
   .enter()
   .append("rect")
   .attr("x", function(d, i) {
		return xScale(i);
   })
   .attr("y", function(d) {
		return h - yScale(d.value);
   })
   .attr("width", xScale.rangeBand())
   .attr("height", function(d) {
		return yScale(d.value);
   })
   .attr("fill", function(d) {
		return "rgb(0, 0, " + (d.value * 10) + ")";
   })

	.on("mouseover", function(d) {
  
		var xPosition = parseFloat(d3.select(this).attr("x")) + xScale.rangeBand() / 2;
		var yPosition = parseFloat(d3.select(this).attr("y")) + 14;
		

		d3.select("#tooltip")
			.style("left", xPosition + "px")
			.style("top", yPosition + "px")
			.select("#value")
			.text(d.value);
		d3.select("#tooltip").classed("hidden", false)
	})
	.on("mouseout", function() {
		d3.select("#tooltip").classed("hidden", true);
	})	;

svg.selectAll("text")
   .data(dataset, key)
   .enter()
   .append("text")
   .text(function(d) {
		return d.value;
   })
   .attr("text-anchor", "middle")
   .attr("x", function(d, i) {
		return xScale(i) + xScale.rangeBand() / 2;
   })
   .attr("y", function(d) {
		return h - yScale(d.value) + 14;
   })
   .attr("font-family", "sans-serif") 
   .attr("font-size", "11px")
   .attr("fill", "white");
   
var sortOrder = false;
var sortBars = function () {
    sortOrder = !sortOrder;
    
    sortItems = function (a, b) {
        if (sortOrder) {
            return a.value - b.value;
        }
        return b.value - a.value;
    };

    svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.value;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
};

d3.select("#sort").on("click", sortBars);
d3.select("#reset").on("click", reset);
function randomSort() {

	
	svg.selectAll("rect")
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
    });

    svg.selectAll('text')
        .sort(sortItems)
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.value;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
}
function reset() {
	svg.selectAll("rect")
		.sort(function(a, b){
			return a.key - b.key;
		})
		.transition()
        .delay(function (d, i) {
        return i * 50;
		})
        .duration(1000)
        .attr("x", function (d, i) {
        return xScale(i);
		});
		
	svg.selectAll('text')
        .sort(function(a, b){
			return a.key - b.key;
		})
        .transition()
        .delay(function (d, i) {
        return i * 50;
    })
        .duration(1000)
        .text(function (d) {
        return d.value;
    })
        .attr("text-anchor", "middle")
        .attr("x", function (d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
        .attr("y", function (d) {
        return h - yScale(d.value) + 14;
    });
};
