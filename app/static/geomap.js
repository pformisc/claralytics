 var minZoomLevel = 4;
	   var maxZoomLevel=6;
      var myOptions = { 
	  mapTypeId: google.maps.MapTypeId.ROADMAP, 
	  center: new google.maps.LatLng(38.55547456,-95.664999),
	  zoom:minZoomLevel,
	  scaleControl:false,
	   panControl: false,
	   zoomControl:true,
	   zoomControlOptions: {
		   style: google.maps.ZoomControlStyle.DEFAULT},
	   overviewMapControl:false
	   };
	   
	  
      var map = new google.maps.Map(document.getElementById('Geomap'), myOptions);
	  
	   var strictBounds = new google.maps.LatLngBounds(
     new google.maps.LatLng(28.70, -127.50), 
     new google.maps.LatLng(48.85, -55.90)
   );
	  
	  google.maps.event.addListener(map, 'dragend', function() {
     if (strictBounds.contains(map.getCenter())) return;

     // We're out of bounds - Move the map back within the bounds

     var c = map.getCenter(),
         x = c.lng(),
         y = c.lat(),
         maxX = strictBounds.getNorthEast().lng(),
         maxY = strictBounds.getNorthEast().lat(),
         minX = strictBounds.getSouthWest().lng(),
         minY = strictBounds.getSouthWest().lat();

     if (x < minX) x = minX;
     if (x > maxX) x = maxX;
     if (y < minY) y = minY;
     if (y > maxY) y = maxY;

     map.setCenter(new google.maps.LatLng(y, x));
   });

   // Limit the zoom level
   google.maps.event.addListener(map, 'zoom_changed', function() {
     if (map.getZoom() < minZoomLevel) map.setZoom(minZoomLevel);
	 if(map.getZoom()> maxZoomLevel)map.setZoom(maxZoomLevel);
   });  
   
    var image = 'icon.png';
      $(document).ready(function() {
        $.getJSON("MapCoordinates.json", function(info) {
         for (var i = 0; i <= info.Values.length-1; i++) {
			 
            var latLng = new google.maps.LatLng(info.Values[i]['LATITUDE'],info.Values[i]['LONGITUDE']); 
            var marker=createMarker(latLng,info.Values[i]['STATE']);
			
		 }
		  marker.setMap(map);
        });
		});
		
		function createMarker(pos,t)
		{
			
				var marker = new google.maps.Marker({
                position:pos,
				map:map,
				draggable:false,
				animation: google.maps.Animation.DROP,
                title:t,
				icon: image
				 });
				 google.maps.event.addListener(marker, 'click',function()
				 {
					 if (marker.getAnimation() != null) 
					 {
    					marker.setAnimation(null);
  			 		} 
			 		else 
			 		{
    					marker.setAnimation(google.maps.Animation.BOUNCE);
 			  		}
					 
				 });
				return marker;
		}
		