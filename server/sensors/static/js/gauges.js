/* Gauges.js, a basic gauges display based on google gauges */


google.load('visualization', '1', {packages:['gauge']});

$(function(){

  var chart = new google.visualization.Gauge(document.getElementById('gauges'));

  var data = [
    ['Label', 'Value']
  ];

  options = {
    width: 500, height: 200,
    redFrom: 90, redTo: 100,
    yellowFrom:75, yellowTo: 90,
    greenFrom: 0, greenTo: 75,
    minorTicks: 20
  };

  function pollServer() {
    var request = $.ajax(window.UPDATE_URL);

    request.always(function(){
      setTimeout(function(){
          pollServer();
      }, (window.AJAX_SLEEP ? window.AJAX_SLEEP : 1000));
    });

    request.success(function(response){
      serverStatus(true);

      var gauge_data = [['Label', 'Value']];

      //Update the dashboard's gauges
      for (var i=0;i<response.length;i++){
        gauge_data.push([
          response[i]['name'] + '',
          parseFloat(response[i]['last-reading'])
        ]);
      }

      drawChart(gauge_data, chart, options);
    });

    request.fail(function(){
      serverStatus(false);
    });
  }

  pollServer();
  drawChart(data, chart, options);
});

function drawChart(data, chart, options) {

  data = google.visualization.arrayToDataTable(data);

  chart.draw(data, options);
}

