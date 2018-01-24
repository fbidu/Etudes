Vue.component('starship', {
    template: `
        <div class="card">
            <header class="card-header">
                <p class="card-header-title">
                    {{data.name}}
                </p>
                <a href="#" class="card-header-icon" aria-label="more options">
                    <span class="icon">
                        <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                </a>
            </header>
        <div class="card-content">
            <div class="content">
                <table class="table">
                    <tbody>
                        <tr>
                          <td>Model</td>
                          <td>{{data.model}}</td>
                        </tr>
                    </tbody>
                </table>
                            
                {{data}}
            </div>
        </div>
        <footer class="card-footer">
            <a href="#" class="card-footer-item">Save</a>
            <a href="#" class="card-footer-item">Edit</a>
            <a href="#" class="card-footer-item">Delete</a>
        </footer>
    </div>`,

    props: {
        code: {required: true}
    },

    data() {
        return {
            data: {}
        };
    },

    mounted() {
        console.log("Looking for ship with code " + this.code)
        axios.get("https://swapi.co/api/vehicles/" + this.code + "/")
            .then(response => this.data = response.data);
    }
})

new Vue({
    el: "#root"
})