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
    