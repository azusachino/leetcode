package tmpl

import (
	"container/list"
	"fmt"
)

type LRUCache struct {
	Cap int
	// Fast access to cache items
	Keys map[int]*list.Element
	// Fast update
	List *list.List
}

type pair struct {
	K, V int
}

func NewLRUCache(cap int) LRUCache {
	return LRUCache{
		Cap:  cap,
		Keys: make(map[int]*list.Element),
		List: list.New(),
	}
}

func (c *LRUCache) Get(key int) (int, error) {
	if ele, ok := c.Keys[key]; ok {
		c.List.MoveToFront(ele)
		return ele.Value.(pair).V, nil
	}

	return -1, fmt.Errorf("key %d not found", key)
}

func (c *LRUCache) Put(key, value int) {
	if ele, ok := c.Keys[key]; ok {
		ele.Value = pair{key, value}
		c.List.MoveToFront(ele)
	} else {
		if c.List.Len() == c.Cap {
			// remove last
			delete(c.Keys, c.List.Back().Value.(pair).K)
			c.List.Remove(c.List.Back())
		}
		c.Keys[key] = c.List.PushFront(pair{key, value})
	}
}

type LFUCache struct {
	// key to value node
	nodes map[int]*list.Element
	// freq to list of nodes
	lists   map[int]*list.List
	cap     int
	minFreq int
}

type node struct {
	key, val, freq int
}

func NewLFUCache(cap int) LFUCache {
	return LFUCache{
		nodes:   make(map[int]*list.Element),
		lists:   make(map[int]*list.List),
		cap:     cap,
		minFreq: 0,
	}
}

func (c *LFUCache) Get(key int) (int, error) {
	value, ok := c.nodes[key]
	if !ok {
		return -1, fmt.Errorf("key %d not found", key)
	}
	currentNode := value.Value.(node)

	// remove from old list (freq)
	c.lists[currentNode.freq].Remove(value)
	currentNode.freq++

	// check if new freq list exists
	if _, ok := c.lists[currentNode.freq]; !ok {
		c.lists[currentNode.freq] = list.New()
	}
	// update hash map
	newList := c.lists[currentNode.freq]
	newNode := newList.PushFront(currentNode)
	c.nodes[key] = newNode

	// update min_freq (check boundary)
	if currentNode.freq-1 == c.minFreq && c.lists[currentNode.freq-1].Len() == 0 {
		c.minFreq++
	}

	return currentNode.val, nil
}

func (c *LFUCache) Put(key, val int) {
	if c.cap == 0 {
		return
	}

	if currentNode, ok := c.nodes[key]; ok {
		// update value
		currentNode.Value.(*node).val = val

		// update freq
		c.Get(key)
		return
	}

	// check capacity
	if len(c.nodes) == c.cap {
		// remove from min_freq list
		minList := c.lists[c.minFreq]
		delete(c.nodes, minList.Back().Value.(*node).key)
		minList.Remove(minList.Back())
	}

	c.minFreq = 1

	currentNode := &node{key, val, 1}
	if _, ok := c.lists[c.minFreq]; !ok {
		c.lists[c.minFreq] = list.New()
	}
	newList := c.lists[c.minFreq]
	newNode := newList.PushFront(currentNode)
	c.nodes[key] = newNode
}
