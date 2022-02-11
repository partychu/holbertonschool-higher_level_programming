$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    for (let t of data.results) {    
        $('#list_movies').append('<li>' + t.title + '</li>');
    }
});