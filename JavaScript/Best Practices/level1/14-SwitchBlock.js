// C-like syntax, conditions are stackable and they fall through
// if you don't use a break. Includes a 'default' statement as well.

var code = 4;
var message;

switch(code)
{
    case 1:
        message = "Hello!";
    case 2:
        message = "Hi";
    case 3:
        message = "Good morning";
    case 4:
        message = "Good afternoon";
    case 5:
        message = "Good night";
}
// Without the break, message will become 'Good Night'


switch(code)
{
    case 1:
        message = "Hello!";
        break;
    case 2:
        message = "Hi";
        break;
    case 3:
        message = "Good morning";
        break;
    case 4:
        message = "Good afternoon";
        break;
    case 5:
        message = "Good night";
        break;
}
// Now message will be 'good afternoon'


switch(code)
{
    case 1:
        message = "Hello!";
        break;
    case 2:
        message = "Hi";
        break;
    case 3:
    case 4:
    case 5:
        message = "Good night";
        break;
    default:
        message = "Code not found"
}
// By stacking, codes 3, 4 and 5 will render a 'good night' message


/*
 * Switch strings
 */
//Works fine!

var country = 'Brazil';
var area;

switch(country)
{
    case 'USA':
        area = 1;
        break;
    case 'Brazil':
        area = 55;
        break;
    default:
        area = 00;
}

/*
 * Fall through
 */

// That sometimes annoying property of the switch statement that makes it run
// through all the subsequent lines may be useful if your logic requires
// some incremental variable that may be stacked.
// This is a silly example but works fine.
function medal_case(name, rank)
{
    this.owner = name;
    switch(rank)
    {
        case: "Imperator": this.add_medal("THE MOST AWESOME MEDAL");
        case: "General": this.add_medal("The BIG GREAT MEDAL");
        case: "Captain": this.add_medal("The very good medal");
        case: "Soldier": this.add_medal("The medal");
    }
}
// The result is simple - the imperator gets a medal case with its unique medal and all of the medals of the lower ranks
// The general gets his nice big great medal and all of the medals bellow but not the imperator's most awesome medal
