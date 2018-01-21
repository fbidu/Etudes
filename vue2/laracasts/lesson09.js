Vue.component('modal', {
    props: {
        visible: {default: false}
    },

    template: `
    <div class="modal is-active" v-show:visible>
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">
                    <slot name="header"></slot>
                </p>
                <button class="delete" aria-label="close"></button>
            </header>
            <section class="modal-card-body">
                <slot></slot>
            </section>
            <footer class="modal-card-foot">
                <slot name=footer>
                    <!-- That's a nice way to provida a default content -->
                    <button class="button is-success">Save changes</button>
                    <button class="button">Cancel</button>
                </slot>
            </footer>
        </div>
    </div>
    `,

    methods: {
        setVisible() {
            this.visible = true
        }
    }
})


new Vue({
    el: "#root",

    methods: {
        show(child) {
            console.log("Someone wants to see " + child)
            this.$refs[child].setVisible()
        }
    }
})