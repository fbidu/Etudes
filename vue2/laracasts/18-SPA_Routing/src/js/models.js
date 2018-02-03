class Person {
    constructor(data) {
        for (let field in data) {
            this[field] = data[field];
        }
        
        axios.get(this.homeworld)
            .then(response => this.planet = response.data.name)
            .catch(this.planet = "Unknown")

        this.movies = [];
        for (let filmId in this.films) {
            console.log(this.films[filmId]);
            axios.get(this.films[filmId])
                .then(response => this.movies.push(response.data.title));
        }
    }
}

export default Person;