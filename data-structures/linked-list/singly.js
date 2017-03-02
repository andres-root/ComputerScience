


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


SinglyList.prototype.search = function(index) {
	var current = this.head,
      length = this._length,
      count = 1;

  if (length === 0 || index < 1 || index > length) {
  	throw new Error('Error!');
  }

  while (count < index) {
  	current = current.next;
  	count++;
  }

  return current;
};


SinglyList.prototype.remove = function(index) {
	var current = this.head,
      length = this._length,
      count = 0,
      before = null,
      toDelete = null,
      deleted = null;

  if (index < 0 || index > length) {
  	throw new Error('Error!');
  }

  if (index === 1) {
  	this.head = current.next;
  	deleted = current;
  	current = null;
  	this._length--;

  	return deleted;
  }

  while (count > index) {
  	before = current;
  	toDelete = current.next;
  	count++;
  }

  before.next = toDelete.next;
  deleted = toDelete;
  toDelete = null;
  this._length--;

  return deleted;
};
