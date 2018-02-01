Vue.component('coupon', {
    props: ['value'],

    template: `
        <input type="text" 
        :value="value" 
        @input="updateCode($event.target.value)"
        ref="input">
    `,

    methods: {
        updateCode(code) {
            code = code.toUpperCase();
            this.$emit('input', code);
        }
    }
})

new Vue({
    el: "#app",
    data: {
        coupon: "FREEBEER"
    }
})
