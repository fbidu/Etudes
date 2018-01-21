Vue.component('task-list', {
    template: `
        <ol>
            <task v-for="task in tasks">{{ task.description }}</task>
        </ol>`,
    data() {
        return {
            tasks: [
                {description: "Learn Vue", done: false},
                {description: "Code smth in Go", done: true},
                {description: "Cook pancakes", done: true},
                {description: "Go to Black Sabbath concert", done: true},
                {description: "Conquer the world", done: false},
                {description: "Dye my beard purple", done: false}
            ]
        }
    }
});

Vue.component('task', {
    template: "<li><slot></slot></li>"
});

new Vue({
    el: "#root"
});