var PI = Math.PI;

var radius = 0;

function circle (radius)
{
	this.radius = radius;
	return radius * radius * PI;
}

module.exports.circle = circle;
