#!/usr/bin/env node

var math = require('mathjs');
var log = console.log;
var max = 600851475143;

// Prime factor finder

var pfactor = function(n){
	var largestfactor = 0;
	if(math.mod(n,2) === 0){
		largestfactor = 2;
		while(math.mod(n,2) === 0){
			n /= 2;
		}
	}
	if(math.mod(n,3) === 0){
		largestfactor = 3;
		while(math.mod(n,3) === 0){
			n /= 3;
		}
	}
	var msix = 6;
	while((msix - 1) < n){
		if(math.mod(n,(msix-1)) === 0){
			largestfactor = msix - 1;
			while(math.mod(n,largestfactor) === 0){
				n /= largestfactor;
			}
		}
		if(math.mod(n,(msix+1)) === 0){
			largestfactor = msix + 1;
			while(math.mod(n,largestfactor) === 0){
				n /= largestfactor;
			}
		}
		msix += 6;
	}
	return largestfactor;
}

log(pfactor(100));
log(pfactor(max));

			
			




