var areaCalc = require('./area');

// Here we set the module's 'radius' to 5
console.log(areaCalc.circle(5));

// We log the radius
console.log(areaCalc.radius);


// Here we require a new instance of the module
var area1 = require('./area');

// Since the "require" as default acts as a singleton, this "new"
// instance will be the same as the above and the radius will be 5
// instead of the default '0'
console.log(area1.radius);
