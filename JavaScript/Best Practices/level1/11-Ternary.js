// One thing I find interesting to notice about is the precedence of the ? operator.
// Inside a string concatenation, the + operator has a higher priority.

var isArthur = false;
var weapon;

console.log("Current weapon: " + isArthur ? "Excalibur" : "Longsword");
// Interestingly, this code will log ONLY "Excalibur

// As usual, it is possible to just elevate the priority using parentheses:
console.log("Current weapon: " + (isArthur ? "Excalibur" : "Longsword"));
// This code prints "Current weapon: Longsword";


/*
 * Multiple statements
 */

var isKing = false;
var helmet;

// Just group the statements and use a comma.
isArthur && isKing ? (weapon = "Excalibur", helmet = "Goosewhite") : (weapon = "Longsword", helmet = "Iron Helm");

/*
 * Nesting
 */

// As usual, you can nest ternaries but you should be careful
// because it can easily mess with your code's legibility.
// Identation is obligatory.

var isArcher = true;
isArthur && isKing ? (weapon = "Excalibur", helmet = "Goosewhite")
                   :
                   isArcher ? (weapon = "Longbow", helmet = "Mail Helm") 
                            : (weapon = "Longsword", helmet = "Iron Helm");
// The above statement will assign longbow and mail helm to the variables.
// 2015-07-31
