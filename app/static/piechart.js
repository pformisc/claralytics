	//Visualization API for the pie chart package
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);

      var result = controller.fetch_device_type()
      console.log(result)

      function drawChart() {

        var device_items = []

        var device_data = $('#load_device_data').data('device');

        $.each(device_data, function(key, value){
          device_items.push([key, value]);
        });
        
        var options = {
      is3D: true,
          colors: ['#E5D843','#80BF34','#38A660'],
          title: 'Visitors by Device Type',
          'legend': 'right',
          animation:{
            duration: 8000,
            easing: 'in'
          },
          pieSliceText: 'percentage',
        slices: {
                    1: {offset: 0.2},
                    2: {offset: 0.1},
                    3: {offset: 0.0},
                    pieSliceTextStyle:{fontSize:'20'},
                    'pieStartAngle':'160'
          },
      };

        var pie_data = new google.visualization.DataTable();
        pie_data.addColumn('string', 'Device Type');
        pie_data.addColumn('number', 'Number of Visitors');
        pie_data.addRows(device_items);

        var row = 0;
        var col = 0;

        var chart = new google.visualization.PieChart(document.getElementById('pie'));
      chart.draw(pie_data, options);

      }