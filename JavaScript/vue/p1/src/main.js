import Vue from 'vue'

Vue.config.debug = process.env.NODE_ENV !== 'production'
const App = new Vue(require('./app.vue'))
