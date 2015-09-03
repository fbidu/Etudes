// 1
var App = Ember.Application.create();

// 2
App.Router.map(function() {
    this.resource("index", {
        "path" : "/"
    });
});

// 3
App.Message = DS.Model.extend({
    "user" : DS.attr("string"),
    "text" : DS.attr("string")
});

// 4
App.ApplicationAdapter = DS.FixtureAdapter.extend(); 

// 5
App.Message.FIXTURES = [ 
    {
        "id"   : 1,
        "user" : "Chris",
        "text" : "Hello World."
    },
    {
        "id"   : 2,
        "user" : "Wayne",
        "text" : "Don't dig it, man."
    },
    {
        "id"   : 3,
        "user" : "Chris",
        "text" : "Meh."
    }
];