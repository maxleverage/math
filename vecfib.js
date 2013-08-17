#!/usr/bin/env node
var math = require('mathjs');
var log = console.log

var fibonacci = function(n){
	var fibmat = math.matrix([[1,1],[1,0]]);
	var ii = 1;
	var newmat = math.matrix([[1,1],[1,0]]);
	while(ii < n){
		ii += 1;
		newmat = math.multiply(newmat, fibmat);
	}
	return newmat;
}

log(fibonacci(10));
log(fibonacci(20));
