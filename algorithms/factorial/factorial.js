

function factorial(n) {
	if (n == 0) {
		return 1;
	}
	n = n * factorial(n - 1);
	return n;
}


var n = 5;
console.log(factorial(n))
