// If anything is false, JS will atribute its value

var nome = "" && 'felipe'; // nome = ""

var idade = 0 && 10; // idade = 0

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
