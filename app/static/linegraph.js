 	 function getDate(d) {
	 var dt = new Date(d.date);
	 dt.setHours(24);
	 dt.setMinutes(0);
	 dt.setSeconds(0);
	 dt.setMilliseconds(0);
	 return dt;
	 }
 
	function showData(obj, d) {
	 var coord = d3.mouse(obj);
	 var infobox = d3.select(".infobox");
	 // now we just position the infobox roughly where our mouse is
	 infobox.style("left", (coord[0] + 100) + "px" );
	 infobox.style("top", (coord[1] - 175) + "px");
	 $(".infobox").html(d);
	 $(".infobox").show();
	 }
 
	function hideData() {
	 $(".infobox").hide();
	 }
	
	 	 
	var drawChart = function(data) {
	 // define dimensions of graph
	 var m = [20, 40, 20, 100]; // margins
	 var w = 700 - m[1] - m[3]; // width
	 var h = 360 - m[0] - m[2]; // height
	 

	data.sort(function(a, b) {
	 var d1 = getDate(a);
	 var d2 = getDate(b);
	 if (d1 == d2) return 0;
	 if (d1 > d2) return 1;
	 return -1;
	 });
 
	// get max and min dates - this assumes data is sorted
	 var minDate = getDate(data[0]),
	 maxDate = getDate(data[data.length-1]);
	 var second=getDate(data[1]);
	 

	 var x = d3.time.scale().domain([minDate, maxDate]).range([0, w]);
	 
	// X scale will fit all values from data[] within pixels 0-w
	 //var x = d3.scale.linear().domain([0, data.length]).range([0, w]);
	 // Y scale will fit values from 0-10 within pixels h-0 (Note the inverted domain for the y-scale: bigger is up!)
	 var y = d3.scale.linear().domain([0, d3.max(data, function(d) { return d.trendingValue; } )]).range([h, 0]);
	 
	// create a line function that can convert data[] into x and y points
	 var line = d3.svg.line()
	 // assign the X function to plot our line as we wish
	 .x(function(d, i) {
	 // return the X coordinate where we want to plot this datapoint
	 return x(getDate(d)); //x(i);
	 })
	 .y(function(d) {
	 // return the Y coordinate where we want to plot this datapoint
	 return y(d.trendingValue);
	 });
	 
	 function xx(e) { return x(getDate(e)); };
	 function yy(e) { return y(e.trendingValue); };
	 
	$("#panel-465099").append("<p><small><em>Please move the mouse over data points to see details.</em></small></p>");
	 
	// Add an SVG element with the desired dimensions and margin.
	 var graph = d3.select("#panel-465099").append("svg:svg")
	 .attr("width", w + m[1] + m[3])
	 .attr("height", h + m[0] + m[2])
	 .append("svg:g")
	 .attr("transform", "translate(" + m[3] + "," + m[0] + ")");
	 
	// create yAxis
	 var xAxis = d3.svg.axis().scale(x).ticks(d3.time.days,1).tickSize(-h).tickSubdivide(false).tickFormat(d3.time.format('%a %d'));
	 // Add the x-axis.
	 graph.append("svg:g")
	 .attr("class", "x axis")
	 .attr("transform", "translate(0," + h + ")")
	 .call(xAxis);
	 
	// create left yAxis
	 var yAxisLeft = d3.svg.axis().scale(y).ticks(10).orient("left"); //.tickFormat(formalLabel);
	 // Add the y-axis to the left
	 graph.append("svg:g")
	 .attr("class", "y axis")
	 .attr("transform", "translate(-25,0)")
	 .call(yAxisLeft);
	 
	// Add the line by appending an svg:path element with the data line we created above
	 // do this AFTER the axes above so that the line is above the tick-lines
	 graph
	 .selectAll("circle")
	 .data(data)
	 .enter().append("circle")
	 .attr("fill", "steelblue")
	 .attr("r", 5)
	 .attr("cx", xx)
	 .attr("cy", yy)
	 .on("mouseover", function(d) { showData(this, d.trendingValue);})
	 .on("mouseout", function(){ hideData();});
	 
	 graph.append("svg:path").attr("d", line(data));
	 graph.append("svg:text")
	 .attr("x", -200)
	 .attr("y", -90)
	 .attr("dy", ".1em")
	 .attr("transform", "rotate(-90)")
	 .text("Number of Hits on each day");
	 
	 
	 $("#panel-465099").append("<div class='infobox' style='display:none;'>Test</div>");
	 }
	 
	var draw = function() {
	 var data = [ {'date': "2012-10-08", 'trendingValue': 100}, {'date': "2012-10-03", 'trendingValue': 80}, {'date': "2012-10-04", 'trendingValue': 60}, {'date': "2012-10-05", 'trendingValue': 50}, {'date': "2012-10-06", 'trendingValue': 40},{'date': "2012-10-07", 'trendingValue': 20},{'date': "2012-10-09", 'trendingValue': 50}];
	 drawChart(data);
	 }
	
	
	 
	

 