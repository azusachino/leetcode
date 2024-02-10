package tmpl

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type TrieNode struct {
	Val      rune
	Children [26]*TrieNode
	IsWord   bool
}

type ListNode struct {
	Val  int
	Next *ListNode
}

type Trie struct {
	Root *TrieNode
}

type BinaryIndexTree struct {
	Tree []int
	Cap  int
}

func NewTrie() Trie {
	return Trie{
		Root: &TrieNode{
			// root node has no value
			Val: '$',
		},
	}
}
