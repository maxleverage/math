#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// Integer
var integer = function(max) {
	var output = [];
	var cc = 0;
	while(cc < max) {
		cc += 1;
		output.push(cc);
	}
	return output;
};


// GCD

var gcd = function(a, b) {
	while(a != b) {
		if(a > b) {
			a -= b;
		}
		else {
			b -= a;
		}
	}
	return a;
};

// LCM function

var lcm = function(a, b) {
	return ((a*b) / gcd(a,b));
}

// Iterative LCM for multiple numbers

var lcmiter = function(as, max) {
	var nval = 0;
	var oval = lcm(as[0],as[1]);
	for(ii=2; ii < max; ii++) {
		nval = lcm(as[ii],oval);
		oval = nval;
	}
	return nval;
};

log(lcmiter(integer(10),10));

log(lcmiter(integer(20),20));
