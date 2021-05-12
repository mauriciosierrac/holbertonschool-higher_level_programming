const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data, textStatus) {
  if (textStatus === 'success') {
    const listMovies = data.results;
    listMovies.forEach(function (movie) {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
