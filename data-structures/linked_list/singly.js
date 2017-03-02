



var Node = function(data) {
	this.data = data;
	this.next = null;	
};

var SinglyList = function() {
	this._length = 0;
	this.head = null;
};

SinglyList.prototype.add = function(value) {
	var	node = new Node(value),
			current = this.head;

	if (!current) {
		this.head = node;
		this._length++;

		return node;
	}

	while (current.next) {
		current = current.next;
	}

	current.next = node;
	this._length++;

	return node;
};