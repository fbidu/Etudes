/**
<template>
  <div class="container">
    <div class="box">
      <article class="media">
        <div class="media-content">
          <div class="content">
            <p>
              <strong>Luke Skywalker</strong>
              <small> &mdash; From
                <strong>Tatooine</strong> &mdash; </small>
              <small>19BBY</small>
              <br>
              <br>
              <strong>Films</strong>
              <ol>
                <li>The Empire Strikes Back</li>
                <li>Revenge of the Sith</li>
              </ol>
            </p>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
*/

<template>
  <div class="container">
    <div class="box" v-for="person in results">
      <article class="media">
        <div class="media-content">
          <div class="content">
            <p>
              <strong> {{ person.name }}</strong>
              <small> &mdash; From
                <strong>{{person.planet}}</strong> &mdash; </small>
              <small>{{person.birth_year}}</small>
              <br>
              <br>
              <strong>Films</strong>
              <ol>
                <li v-for="movie in person.movies">{{movie}}</li>
              </ol>
            </p>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>
<script>

  import Person from '../models';

  export default {
    data() {
      return {
        results: []
      }
    },

    created() {
      axios.get("https://swapi.co/api/people/?format=json")
        .then(response => {
          let results = response.data.results;

          for (let result in results) {
            this.results.push(new Person(results[result]));
          }
        });
    }
  }
</script>