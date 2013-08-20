#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// N digit series generation
// n specifies the number of digits in the real integer series to be generated

var digit = function(n) {
	var series = [];
	var cc = 0;
	while(cc < (math.pow(10,n) - 1)) {
		cc += 1;
		series.push(cc);
	}
	return series;
};

// Digit series product & string conversion

var product = function(as){
	var products = [];
	for(ii in as){
		for(jj in as){
			products.push((as[ii] * as[jj])+'');
		}
	}
	return products;
};

// Comparer function for string split

var palindrome = function(as) {
	var output = [];
	for(i = (as.length - 1); i >= 0; i--) {
		var str = as[i].split("");
		if(str[0] === str[(str.length - 1)]) {
			if(str[1] === str[(str.length - 2)]) {
				if(str[2] === str[(str.length - 3)]) {
					output.push(Number(as[i]));
				}
			}
		}
	}
	return output;
};

var result = product(digit(3));
log(math.max(palindrome(result)));



