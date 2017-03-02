
var values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


function sum(n) {
	if (n == 1) {
		return n;
	} else {
		return n + sum(n - 1);
	}
}

console.log(sum(10));
