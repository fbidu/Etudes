class Errors {
    constructor() {
        this.errors = {};
    }

    get(field) {
        if (this.errors[field]) {
            return this.errors[field];
        }
    }

    record(errors) {
        this.errors = errors;
    }

    clear(field) {
        if (field) {
            delete this.errors[field];
            return;
        }

        this.errors = {};
    }

    has(field) {;
        return this.errors.hasOwnProperty(field)
    }

    any() {
        return Object.keys(this.errors).length > 0;
    }
}

class Form {
    constructor(data) {
        this.originalData = data;

        for (let field in data) {
            this[field] = data[field];
        }

        this.errors = new Errors();
    }

    data() {
        let data = Object.assign({}, this);

        delete data.originalData;
        delete data.errors;

        return data;

    }

    update(data) {
        for (let field in data) {
            this[field + 'Result'] = data[field]
        }

    }

    submit(requestType, url) {
        return new Promise((resolve, reject) => {
            axios[requestType](url, this.data())
                .then(response => {
                    this.onSuccess(response.data);
                    resolve(response.data);
                })
                .catch(error => {
                    this.onFail(error.response.data)
                });
        })
    }

    onSuccess(data) {
        console.log(data)
        this.update(data)
        this.errors.clear();
        this.reset();
    }

    onFail(errorData) {
        console.log(errorData)
        this.errors.record(errorData);
    }

    reset() {
        for (let field in this.originalData) {
            this[field] = '';
        }
    }
}

new Vue({
    el: "#root",

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