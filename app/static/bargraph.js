/*
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
          vAxis: {title: 'Week number',  gridlines:{count:0}, titleTextStyle: {color: 'black'}},
		  hAxis: {title: 'Hits on each week',  gridlines:{count:0}, titleTextStyle: {color: 'black'}},
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
 */  
//new code

    
      function drawChart() {
          // Create and populate the data table.
        var option = {title:"Hits for The Santa Clara in this month (shown per week)",
                     width:500, height:200,
                     animation: {duration: 2000, easing: 'in',},
                     vAxis: {title: "",titleTextStyle: {color: 'red'}},
                     'legend':'none',
                     hAxis: {title: "Hits on each week", minValue:0, maxValue:100,titleTextStyle: {color: 'red'},
           gridlines:{color:'transparent'}},
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
        var data = new google.visualization.DataTable();    
        data.addColumn('string', 'Week');
        data.addColumn('number', 'Hits');
        data.addRow(['Week1', 0]);
        data.addRow(['Week2', 0]);
        data.addRow(['Week3', 0]);
        data.addRow(['Week4', 0]);
        data.addColumn('number', 'Other');

        // Create and draw the visualization.
        var chart = new google.visualization.BarChart(document.getElementById('panel-304865'));
        chart.draw(data, option);
        data.setValue(0, 1, 75);
        data.setValue(1, 1, 55);
        data.setValue(2, 1, 30);
        data.setValue(3, 1, 75);
        chart.draw(data, option);
      }

      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
