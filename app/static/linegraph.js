     /*
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
		var data = new google.visualization.DataTable();
        data.addColumn('date', 'Date');
    	data.addColumn('number', 'Hits');
    	data.addRow([new Date(2013, 0, 1), 10])
    	data.addRow([new Date(2013, 0, 2), 15])
    	data.addRow([new Date(2013, 0, 3), 40])
    	data.addRow([new Date(2013, 0, 4), 50])
		data.addRow([new Date(2013, 0, 5), 60])
		data.addRow([new Date(2013, 0, 6), 80])
		data.addRow([new Date(2013, 0, 7), 50])

        var options = {
         // title: 'Hits per day',
		  'legend':'none',
		  colors:['#80BF34'],
		  hAxis:
		  {
			 format:'EEE , d',
			 title:'Days in a week',
			  gridlines:{color:'transparent'},
			 slantedText:true,
			 slantedTextAngle:30,
			 textStyle:{
				 bold:true},
			 titleTextStyle: {color: 'black'}
			
		  },
		  vAxis:
		  {
			 title:'Number of Hits',
			 gridlines:{color:'transparent'},
			  textStyle:{
				 bold:true},
			 titleTextStyle: {color: 'black'}
		  },
		  pointSize:4
        };

        var chart = new google.visualization.LineChart(document.getElementById('panel-465099'));
        chart.draw(data, options);
      }

      */
    
    //new code with animation
    google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
		var data = new google.visualization.DataTable();
        data.addColumn('date', 'Date');
    	data.addColumn('number', 'Hits');
    	data.addRow([new Date(2013, 0, 1), 0])
    	data.addRow([new Date(2013, 0, 2), 0])
    	data.addRow([new Date(2013, 0, 3), 0])
    	data.addRow([new Date(2013, 0, 4), 0])
		data.addRow([new Date(2013, 0, 5), 0])
		data.addRow([new Date(2013, 0, 6), 0])
		data.addRow([new Date(2013, 0, 7), 0])

        var options = {
          title: 'Hits per day',
		  'legend':'none',
		  colors:['#004411'],
		  animation: {duration: 1000, easing: 'out',},
		  hAxis:
		  {
			 format:'E,d',
			 title:'Days in a week',
			 gridlines:{ color: 'transparent'},
			 slantedText:true,
			 slantedTextAngle:30,
			 textStyle:{
				 bold:true},
			 titleTextStyle: {color: 'red'},
			
			
		  },
		  vAxis:
		  {
			 title:'Number of Hits'	 ,
			  minValue:0, maxValue:100,
			 gridlines:{count:5,color:'transparent'} ,
			  textStyle:{
				 bold:true},
			 titleTextStyle: {color: 'red'}
		  },
		  pointSize:4
        };

        var chart = new google.visualization.LineChart(document.getElementById('panel-465099'));
        chart.draw(data, options);
		data.setValue(0,1,80);
    	data.setValue(1,1,20);
    	data.setValue(2,1,50);
    	data.setValue(3,1,20);
		data.setValue(4,1,65);
		data.setValue(5,1,40);
		data.setValue(6,1,90);
		chart.draw(data, options);
      }