#!/bin/usr/env node

var math = require('mathjs');
var big = require('big-integer');
var log = console.log;

var factorial = function(n) {
	if(n > 1) {
		n *= factorial(n-1);
	}
	return n;
}




log(factorial(100));


