#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// Integer generation

var integer = function(n) {
	var output = [];
	for(ii = 1; ii <= n; ii++) {
		output.push(ii);
	}
	return output;
};

// Sum function
var sum = function(arr) {
        var cc = 0;
        for(var ii in arr) {
                cc += arr[ii];
        }
        return cc;
};

// Triangle number

var triangle = function(n) {
	var as = integer(n);
	var output = sum(as);
	return output;
}

// Factor search. Search up to sqrt(n)

var fsearch = function(n) {
	var output = [];
	for(ii = 1; ii <= (math.sqrt(n) + 1); ii++) {
		if(n % ii === 0) {
			output.push(ii);
		}
	}
	for(jj = (output.length - 1); jj >= 0; jj--) {
		output.push(n / output[jj]);
	} 
	return output.length;
};

// Triangle number search; k denotes the number of characters
var tsearch = function(k) {
	var init = 1;
	var output = 0;
	while(fsearch(triangle(init)) < k) {
		init += 1;
	}	
	output = triangle(init);
	return output;
};

log(tsearch(500));
