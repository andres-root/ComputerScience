

function palindrome(word) {
	if (word.length == 0 || word.length == 1) {
		return true;
	} else if (word.slice(0, 1) === word.slice(-1)) {
		return true;
	} else {
		return false;
	}

	return palindrome(word.substr(1).slice(0, -1));
}

console.log(palindrome('rotor'));
console.log(palindrome('motor'));
