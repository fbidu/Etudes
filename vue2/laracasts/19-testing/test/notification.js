import Vue from 'vue/dist/vue';
import test from 'ava';

import Notification from '../src/Notification';

function notification(message) {
    let n = Vue.extend(Notification);

    let notif = new n({
        propsData: {
            message: message
        }
    }).$mount();

    return notif
}
test("That it renders a notification", t => {

    notif = notification("Hello, world!");
    let content = notif.$el.textContent;

    t.is(content, "Hello, world!");
});