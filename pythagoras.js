#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// Integer list generator

var integer = function(max) {
	var output = [];
	for(i = 1; i <= max; i++) {
		output.push(i);
	}
	return output;
};

// Pythagorean triples

var pytriple = function(max) {
	var a = integer(max);
	var b = integer(max);
	var c = 0;
	var output = [];
	for(ii in a) {
		for(jj in b) {
			if(a[ii] < b[jj]) {
				c = math.sqrt(math.pow(a[ii],2) + math.pow(b[jj],2))
				output.push(a[ii],b[jj],c);
			}
		}
	}
	return output;
};

// Pythagorean search

var pysearch = function(as, max) {
	var output = [];
	for(ii = 2; ii <= (as.length - 1); ii+=3) {
		if(as[ii] + as[ii-1] + as[ii-2] === max) {
			output.push(as[ii], as[ii-1], as[ii-2]);
			break;
		}
	}
	return output;
};


log(pysearch(pytriple(1e3), 1e3));
var result = pysearch(pytriple(1e3), 1e3);

log(result[0] * result[1] * result[2]);
