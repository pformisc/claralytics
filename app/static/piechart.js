	//Visualization API for the pie chart package
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Usage','Number'],
		  ['Mobile',300],
		  ['PC',700],
		  ['Tablets',200]
        ]);
        

        var options = {
         		
          is3D: true,
		  colors: ['#E5D843','#80BF34','#38A660'],
		   'legend': 'right',
		    pieSliceText: 'percentage',
         	 slices: {  1: {offset: 0.2},
                    2: {offset: 0.1},
                    3: {offset: 0.0},
			pieSliceTextStyle:
			{
				fontSize:'20'
			},
			'pieStartAngle':'160'
                    
          },
		  
        };


        var chart = new google.visualization.PieChart(document.getElementById('pie'));
        chart.draw(data, options);
      }
 