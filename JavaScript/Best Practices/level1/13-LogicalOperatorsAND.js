// If anything is false, JS will atribute its value

var name = "" && 'felipe'; // nome = ""

var age = 0 && 10; // idade = 0

/*
 * Double trues
 */

// Returns the last true value

var title = 'king' && 'arthur'; // Gets arthur

/*
 * Double falses
 */
// Returns the first value because of short circuiting. 
var result = "" && undefined; // result = "";
