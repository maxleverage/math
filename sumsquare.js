#!/usr/bin/env node

var sum = function(arr){
	var cc = 0;
	for(var ii in arr){
		cc += arr[ii];
	}
	return cc;
}


var sumsquare = function(n){
	var ii = 0;
	var out = [];
	value = 0;
	while(ii < n){
		ii += 1;
		value = Math.pow(ii,2);
		out.push(value);
	}
	return sum(out);
};

var squaresum = function(n){
	var ii = 0;
	var out = [];
	while(ii < n){
		ii += 1;
		out.push(ii);
	}
	return Math.pow(sum(out),2);
};

console.log(squaresum(10) - sumsquare(10));
console.log(squaresum(100) - sumsquare(100));
		
