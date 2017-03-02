


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
	var current = this.head,
      length = this._length,
      count = 0,
      before = null,
      after = null,
      toDelete = null,
      deleted = null;

  if (length === 0 || index < 1 || index > length) {
  	throw new Error('Error!');
  }

  if (index === 1) {
  	this.head = current.next;
  	
    if (this.head) {
      this.head.prev = null;
    } else {
      this.tail = null;
    }
  } else if (index === this._length) {
    this.tail = this.tail.prev;
    this.tail.next = null;
  } else {
    while (count < position) {
      current = current.next;
      count++;
    }
     
    before = current.previous;
    toDelete = current;
    after = current.next;

    before.next = after;
    after.previous = before;
    deleted = toDelete;
    toDelete = null;
  }

  this._length--;
  return this;
};
  