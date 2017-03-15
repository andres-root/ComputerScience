

var EventBus = function() {
  this.topics = {};
};

EventBus.prototype.subscribe = function(topic, listener) {
  if(!this.topics[topic]) {
    this.topics[topic] = [];
  }

  this.topic[topic].push(listener);
};

EventBus.prototype.publish = function(topic, data) {
  if (!this.topics[topic] || this.topics[topic].length < 1) {
    return false;
  }

  this.topics[topic].forEach(function(listener) {
    listener(data || {});
  });
};

EventBus.prototype.execute = function(topic, data) {
  if (!this.topics[topic] || this.topics[topic].length < 1) {
    return false;
  }

  this.topics[topic].forEach(function(listener) {
    listener[topic](data || {});
  });
};
