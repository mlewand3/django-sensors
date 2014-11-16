
function serverStatus(ok) {
  var status_div = $('.status.server');
  var status_message = $('.server .message');

  switch (ok) {

    case true:
      status_div.removeClass('not-ok');
      status_div.removeClass('not-pulse');
      status_message.text('Server OK');
      break;

    case false:
      if (status_div.hasClass('not-ok')) {
        status_div.removeClass('not-ok');
        status_div.addClass('not-pulse');
      } else {
        status_div.addClass('not-ok');
        status_div.removeClass('not-pulse');
      }
      status_message.text('Server NOT OK');
      break;
  }
}
