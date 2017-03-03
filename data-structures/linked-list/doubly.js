


var Node = function(data) {
	this.data = data;
	this.prev = null;
  this.next = null;
};

var DoublyList = function() {
	this._length = 0;
  this.head = null;
	this.tail = null;
};

DoublyList.prototype.add = function(value) {
	var	node = new Node(value),
			current = this.head;

	if (this._length) {
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = node;
  } else {
    this.head = node;
    this.tail = node;
  }

  this._length++;
  return node;
};


DoublyList.prototype.search = function(index) {
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

DoublyList.prototype.remove = function(index) {
  var toDelete = this.search(index);

  if (this._length === 0 || index < 1 || index > this._length) {
    throw new Error('Index out of range');
  }

  if (toDelete.next) {
    toDelete.next.prev = toDelete.prev;
  } else {
    this.tail = toDelete.prev;
  }

  if (toDelete.prev) {
    toDelete.prev.next = toDelete.next;
  } else {
    this.head = toDelete.next;
  }

  this._length--;

  return this;
};
  