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
        if (field) delete this.errors[field];
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
        this['up'] = data['name']
    }

    submit(requestType, url) {
        axios[requestType](url, this.data())
            .then(response => {
                this.onSuccess(response)
            })
            .catch(error => {
                this.onFail(error.response.data)
            });
    }

    onSuccess(response) {
        this.update(response.data)
        this.errors.clear();
    }

    onFail(error) {
        this.errors.record(error);
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
            "name": "",
            "up": ""
        }),
    },

    methods: {
        onSubmit() {
            this.form.submit('post', 'http://localhost:5000/upper')
        }
    }
})