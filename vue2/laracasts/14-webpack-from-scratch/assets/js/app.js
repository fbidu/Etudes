import axios from "axios";
import Vue from "vue";
import Form from "./core/Form";

import Hello from "./components/Hello"

window.axios = axios; // This makes axios "global"

new Vue({
    el: "#root",

    components: {
        Hello
    },

    data: {
        "form": new Form({
            "name": ""
        }),
        "projectForm": new Form({
            "name": "",
            "description": ""
        })
    },

    methods: {
        onSubmit() {
            this.form.submit('post', 'http://localhost:5000/upper')
                .then(response => {
                    console.log(response);
                });
        },

        submitProject() {
            this.projectForm.submit('post', "http://localhost:5000/projects")
        }
    }
})