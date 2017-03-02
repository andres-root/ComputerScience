

function power(x, n) {
	if (n === 0) {
		return 1;
	} else if (n % 2 === 0){
		var y = power(x, n/2);
		return y * y;
	} else if (n < 0) {
		var neg = power(x, n*-1)
		return 1/neg;
	} else {
		var e = power(x, n-1);
		return e * x;
	}
}

console.log(power(3, -1));
