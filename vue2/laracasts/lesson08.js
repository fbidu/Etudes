window.Event = new Vue();

Vue.component('coupon', {
    props: ['value'],

    template: "<input v-bind:value=value placeholder=\"Enter your coupon code!\" @blur=\"apply($event.target.value)\">",

    methods: {
        apply(value) {
            Event.$emit('applied-listener', value);
        }
    }
})

Vue.component('coupon-direct-event', {
    props: ['value'],

    template: "<input v-bind:value=value placeholder=\"Enter your coupon code!\" @blur=\"applyDirect($event.target.value)\">",

    methods: {
        applyDirect(value) {
            this.$emit('applied', value);
        }
    }
})

Vue.component('message', {
    data() {
        return {
            visible: false
        };
    },

    template: `
        <article class="message is-success" v-show=visible>
            <div class="message-header">
                <p>Success</p>
                <button class="delete" aria-label="delete"></button>
            </div>
            <div class="message-body">
                <slot></slot>
            </div>
        </article>
    `,

    created() {
        Event.$on('applied-listener', (payload) => {
            this.visible = (payload > 10)
        })
    },
})

new Vue({
    el: "#root",

    data: {
        couponApplied: false,
        secondVisible: false
    },

    methods: {
        appliedDirect(value) {
            this.couponApplied = (value > 10)
        }
    },

    created() {
        Event.$on('applied-listener', () => alert("Root got the event!"))
    }
})