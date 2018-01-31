import Errors from "./Errors";

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

export default Form;