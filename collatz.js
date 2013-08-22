#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;
var fs = require('fs');

// Number sequence generator
var integer = function(n) {
	var output = [];
	for(ii = 1; ii <= n; ii++) {
		output.push(ii);
	}
	return output;
};

// Collatz sequence generator
var collatz = function(k) {
	var output = [k];
	var n = k;
	while(n > 1) {
		if(n % 2 === 0) {
			n /= 2;
			output.push(n);
		} else {
			n = (3*n + 1);
			output.push(n);
		}
	}
	return output.length;
}

// Collatz sequence length search
var colsearch = function(j) {
	var intlist = integer(j);
	var output = [];
	for(ii in intlist) {
		output.push(collatz(intlist[ii]));
	}
	return output;
}

// Index search 
var isearch = function(as) {
	var output = [];
	var max = math.max(as);
	var acc = 0;
	for(ii in as) {
		if(as[ii] === max) {
			acc = Number(ii) + 1;
			output.push(acc);
		}
	}
	return output;
};

// Testing

log(colsearch(20));
log(isearch(colsearch(1e6)));

var outfile = "collatz.csv";
var out = colsearch(1e4);

fs.writeFileSync(outfile, out);
