

var Node = function (data) {
	this.parent = null;
	this.children = [];
	this.data = data;
};

var Tree = function(data) {
	this.node = new Node(data);
	this._root = this.node;
};

Tree.prototype.traverse = function(callback) {
	(function dfs(node) {
		for (var i = 0; i < node.children.length; i++) {
			dfs(node.children[i]);
		}

		callback(node);
	})(this._root);
};

