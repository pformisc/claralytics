
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
	  
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Week1', 'Hits'],
          ['Week 1',  300],
          ['Week 2',  500],
          ['Week 3',  420],
          ['Week 4',  200]
        ]);
		google.visualization.ColorFormat();
		
    
        var options = {
          title: 'Hits for The Santa Clara in this month (shown per week)',
          vAxis: {title: 'Week number',  titleTextStyle: {color: 'red'}},
		  hAxis: {title: 'Hits on each week',  titleTextStyle: {color: 'red'}},
		  legend: {position:'none'},
		  series: {
				0: {
                    // set the color to change to
                    color: '009EBF',
                    // don't show this in the legend
                    visibleInLegend: false,				
					
                },
                1: {
                    // set the color to change to
                    color: 'FFA500',
                    // don't show this in the legend
                    visibleInLegend: false,			 
                }
		  }
		
		  
		  
        };

        var chart = new google.visualization.BarChart(document.getElementById('panel-304865'));
        chart.draw(data, options);
		
		
		 ; // Apply formatter to second column
      }
