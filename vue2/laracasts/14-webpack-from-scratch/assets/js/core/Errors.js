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

export default Errors;