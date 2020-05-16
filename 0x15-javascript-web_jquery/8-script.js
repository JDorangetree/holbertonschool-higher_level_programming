$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  for (const film of data.results) {
    $('#list_movies').append(`<li>${film.title}</li>`);
  }
});
