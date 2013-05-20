/* Gauges.js, a basic gauges display based on google gauges */


google.load('visualization', '1', {packages:['gauge']});

$(function(){

  var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

  var data = [
    ['Label', 'Value']
  ];

  $('.sensor').each(function(){
    var label = $(this).attr('title');
    var value = $(this).find('.reading').attr('value');
    value = value / 1000;
    data.push([label, value]);
  });

  options = {
    width: 500, height: 200,
    redFrom: 90, redTo: 100,
    yellowFrom:75, yellowTo: 90,
    minorTicks: 10
  };

  drawChart(data, chart, options);

  setInterval(function(){
    var gauge_data = [
      ['Label', 'Value']
    ];
    $.ajax({ url: "/ajax-gauge-update", success: function(response){
        //Update the dashboard's gauges
        for (var i=0;i<response.length;i++){
          gauge_data.push([
            response[i]['name'] + '',
            parseFloat(response[i]['last-reading'])
          ]);
        }
        console.log(gauge_data);
        drawChart(gauge_data, chart, options);
    }, dataType: "json"});
  }, 1200);
});

function drawChart(data, chart, options) {

  data = google.visualization.arrayToDataTable(data);

  chart.draw(data, options);
}

