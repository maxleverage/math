#!usr/bin/env node

var fibonacci = function(n){
	var phi = (1+Math.sqrt(5))/2;
	return Math.round((Math.pow(phi,n+1) - Math.pow(1-phi, n+1))/Math.sqrt(5));
};

var iseven = function(n){
	return n % 2 === 0;
};

var sum = function(arr){
	var cc = 0;
	for(var ii in arr){
		cc += arr[ii];
	}
	return cc;
};

var fibsum = function(max){
	var value = 0;
	var ii = 1;
	var out = [];
	var flag = false;
	while(value < max) {
		value = fibonacci(ii);
		flag = iseven(value);
		ii += 1
		if(flag && value < max){
			out.push(value);
		}
	}
	return sum(out);
};

console.log(fibsum(4e6));


