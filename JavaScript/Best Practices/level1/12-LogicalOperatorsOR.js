// Very neat trick. The object bellow was refactored until the third step
// It's important to note that JS uses the 'short circuiting' method for logical evaluation
// Meaning that an OR operator, by example, returns true at the first true value instead of passing through all the subsequent steps

var armory = {
    addSword: function(sword)
    {
        if (!this.swords)
        {
            this.swords = [];
        }
        this.swords.push(sword);
    }
};

var armory = {
    addSword: function(sword)
    {
        this.swords = this.swords ?  this.swords : [];
        this.swords.push(sword);
    }
};

var armory = {
    addSword: function(sword)
    {
        this.swords = this.swords || [ ]; // The OR operator will select the first true value.
        this.swords.push(sword);
    }
};

/*
 * Double trues
 */
// Evaluates the first and short circuits.
var n = 2 || 4; // n = 2
var m = "Felipe" || "Brazil"; // m = Felipe

/*
 * DOUBLE FALSES!!
 */
// Interestingly, it returns the last value

var res0 = false || 0;  // res = 0;
var res1 = 0 || false; // res1 = false;
var res2 = "" || undefined; // res2 = undefined
