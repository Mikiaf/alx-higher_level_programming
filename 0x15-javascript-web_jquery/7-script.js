const character = $('#character')

$.ajax({
    type: 'GET',
    url:'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success:function(json){
        const name = json['name']
        character,text(name)
    }
})