package tmpl

// UnionFind is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
type UnionFind struct {
	parent, rank []int
	count        int
}

// Init uf
func (uf *UnionFind) Init(n int) {
	uf.parent = make([]int, n)
	uf.rank = make([]int, n)
	uf.count = n
	for i := 0; i < n; i++ {
		uf.parent[i] = i
		uf.rank[i] = 1
	}
}

func (uf *UnionFind) Find(x int) int {
	if x == uf.parent[x] {
		return x
	}
	// compress path
	uf.parent[x] = uf.Find(uf.parent[x])
	return uf.parent[x]
}

func (uf *UnionFind) Union(x, y int) {
	rootX, rootY := uf.Find(x), uf.Find(y)
	if rootX == rootY {
		return
	}
	if uf.rank[rootX] < uf.rank[rootY] {
		rootX, rootY = rootY, rootX
	}
	uf.parent[rootY] = rootX
	uf.rank[rootX] += uf.rank[rootY]
	uf.count--
}

// Count return the number of sets
func (uf *UnionFind) Count() int {
	return uf.count
}
