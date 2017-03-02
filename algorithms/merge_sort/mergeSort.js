
var unsorted = [7, 3, 1, 6, 2, 8, 10, 5, 9, 4, 11, 12]


function merge(A, B) {
	var result = [];
	while (A.length && B.length) {
		if (A[0] <= B[0]) {
			result.push(A.shift());
		} else {
			result.push(B.shift());
		}
	}

	while(A.length) {
		result.push(A.shift());
	}

	while(B.length) {
		result.push(B.shift());
	}

	return result;
}


function sort(values) {
	if (values.length < 2) {
		return values;
	}

	var middle = parseInt(values.length / 2);
  var left   = values.slice(0, middle);
  var right  = values.slice(middle, values.length);

  console.log(left, right)

	return merge(sort(left), sort(right));
}

console.log(unsorted);
console.log(sort(unsorted));
