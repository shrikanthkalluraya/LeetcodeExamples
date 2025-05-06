# cheet sheet

 Start
│
├── Is the data sorted or needs order?
│   ├── Yes → Try Two Pointers or Binary Search
│   │   ├── Need to find elements with sum? → Two Pointers
│   │   └── Search for a value or position? → Binary Search
│   └── No
│
├── Are you working with a tree or graph?
│   ├── Yes
│   │   ├── Want to visit all nodes? → BFS or DFS
│   │   ├── Shortest path? → BFS (unweighted) or Dijkstra (weighted)
│   │   └── Detect cycles or components? → DFS or Union-Find
│   └── No
│
├── Is the data a sequence (array/string/list)?
│   ├── Yes
│   │   ├── Need max/min of contiguous subarray/substring?
│   │   │   ├── Fixed size? → Sliding Window
│   │   │   └── Varying size or condition-based? → Variable Sliding Window
│   │   ├── Looking for pairs/triplets? → Two Pointers or Hash Map
│   │   ├── Need frequency counts or lookups? → Hash Map/Set
│   │   └── Need all combinations/permutations? → Backtracking
│   └── No
│
├── Is there recursion or overlapping subproblems?
│   ├── Yes → Dynamic Programming
│   │   ├── Want to know count/ways? → DP
│   │   └── Want to maximize/minimize value? → DP
│   └── No
│
├── Are you asked for all valid options/paths?
│   └── Yes → Backtracking (maybe with pruning)
│
└── Are local greedy choices optimal?
    └── Yes → Try Greedy




---

## 🔍 Quick Pattern Hints

| Pattern             | Clues in Problem                              | Typical Use Cases                        |
|---------------------|-----------------------------------------------|------------------------------------------|
| **Sliding Window**  | "Contiguous", "subarray", fixed window size   | Max sum subarray, Longest substring      |
| **Two Pointers**    | Sorted arrays, pair/triplet problems          | Two sum II, 3Sum                         |
| **Fast/Slow Pointers** | Linked lists, cycle detection               | Linked list cycle, palindrome check     |
| **Hash Map/Set**    | Frequency, uniqueness, quick lookup           | Anagrams, Subarray sum                   |
| **Binary Search**   | Search in sorted data                         | Rotated array, Binary search             |
| **DFS/BFS**         | Tree/graph traversal, "connected", "shortest" | Word ladder, Level order traversal       |
| **Dynamic Programming** | Optimal substructure, overlapping subproblems | House robber, LIS                    |
| **Greedy**          | “Minimum”, “maximum”, optimal local choices   | Jump game, Activity selection            |
| **Backtracking**    | Generate all possibilities, "all combinations"| N-Queens, Word search                    |
| **Union-Find (DSU)**| Disjoint sets, graph connectivity             | Number of islands, Redundant connection  |

---

## 💡 Tips

- Think out loud in interviews to show your reasoning.
- Always clarify constraints before choosing a pattern.
- Start with brute force → optimize using known patterns.

---

> Created for interview practice and pattern recognition. Feel free to fork and customize!
