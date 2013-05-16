/* Gauges.js, a basic gauges display */

$(function(){
  $('.gauge').each(function(){
    min = $(this).attr('min');
    max = $(this).attr('max');
    range = (max - min) / 100;
    degrees = 90;
    needle_degrees = degrees;
    $(this).find('#needle').get(0).css('-webkit-transform', 'rotate(' + needle_degrees + ')');
  });
});