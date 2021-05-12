$(document).ready(() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  $.get(url, function (data, textStatus) {
    if (textStatus === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
