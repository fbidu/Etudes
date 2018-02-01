new Vue({
    el: "#alphaNotShared",
    data: {
        user: {
            name: "John"
        }
    }
})

new Vue({
    el: "#betaNotShared",
    data: {
        user: {
            name: "Jack"
        }
    }
})


// If we use a global variable, we can share

let user = {
    name: "Godiva"
}

new Vue({
    el: "#alphaShared",
    data: {
        user: user
    }
})

new Vue({
    el: "#betaShared",
    data: {
        user: user
    }
})