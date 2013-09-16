#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// Digit generator

var digit = function(n) {
	var output = [];
	for(i = 1; i <= n; i++) {
		output.push(i)
	}
	return output;
}

// Sum

var sum = function(as) {
	var cc = 0;
	for(ii in as) {
		cc += as[ii];
	}
	return cc;
}

// Divisor

var divisor = function(n) {
	var output =[];
	for(ii = 1; ii <= (math.floor(Math.sqrt(n)) + 1); ii++) {
		if(n % ii === 0) {
			output.push(ii)
		}
	}
	for(jj = (output.length - 1); jj > 0; jj--) {
		output.push(n / output[jj])
	}
	return output;
}

// Amicability Checker

var amicable = function(as) {
	var output = [];
	var base = 0;
	var child = 0;
	for(ii = 2; ii <= (as.length - 1); ii++) {
		child = sum(divisor(as[ii]));
		if(sum(divisor(child)) === as[ii]) {
			output.push(as[ii]);
			output.push(child);
		}
	}
	return output;
}

log(divisor(220));
log(sum(divisor(220)));
log(sum(divisor(300)));
log(amicable(digit(10)));
