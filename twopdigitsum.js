#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;

// Sum function for arrays
var sum = function(as) {
	var cc = 0;
	for(ii in as) {
		cc += as[ii];
	}
	return cc;
};

// Power digit sum; K denotes the Nth power of 2
var power = function(base, k) {
	var output = [base];
	var temp = [];
	var init = 1;
	var index = 0;
	while(init < k) {
		for(ii in output) {
			output[ii] *= 2;
		}
		if(output.length === 1 && output[0] >= 10) {
			output.push(1);
			output[0] = output[0] + '';
			temp = output[0].split("")[1];
			output[0] = Number(temp);
		}
		if(output.length === 2) {
			if(output[0] >= 10) {
				output[1] += 1;
				output[0] = output[0] + '';
				temp = output[0].split("")[1];
				output[0] = Number(temp);
			}
			if(output[1] >= 10) {
				output.push(1);
				output[1] = output[1] + '';
				temp = output[1].split("")[1];
				output[1] = Number(temp);
			}
		}
		if(output.length > 2) {
			for(ii=0; ii <= (output.length - 2); ii++){
				if(output[ii] >= 10) {
					output[ii+1] += 1;
					output[ii] = output[ii] + '';
					temp = output[ii].split("")[1];
					output[ii] = Number(temp);
				}
			}
			index = output.length - 1;
			if(output[index] >= 10) {
				output[index] = output[index] + '';
				temp = output[index].split("")[1];
				output[index] = Number(temp);
				output.push(1);
			}
		}
		init += 1;
	}
	return output;
}

// Digit aggregator
var agg = function(as) {
	var output = as[as.length - 1].toString();
	for(ii = (as.length - 2); ii >= 0; ii--) {
		as[ii] = as[ii].toString()
		output = output + as[ii];
	}
	return output;
};


log(agg(power(2,20000)));
log(sum(power(2,20000)));
				

