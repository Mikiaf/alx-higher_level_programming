
const list = $('#list_movies')
$.ajax({
    type:'GET',
    url:'https://swapi-api.alx-tools.com/api/films/?format=json',
    success:function(data){
        data.results.forEach((movie_title) => {
            list.append(`<li>${movie_title.title}</li>`)
        })
    }
})