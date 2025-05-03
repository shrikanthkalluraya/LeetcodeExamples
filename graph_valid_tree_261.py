# Graph-valid-tree. LeetCode: 261
class Solution(object):
    def isValidGraph(self, n, edges)
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Step 1: Check edge count
        if len(edges) != n - 1:
            return False

        # Step 2: Build the Graph
        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)  # undirected

        # Step 3: DFS Traversal (start from node 0)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False  # cycle found
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # skip the edge we came from
                if not dfs(neighbor, node):
                    return False
            return True

        # 4. Start DFS from node 0
        if not dfs(0, -1):
            return False




        # 5. Ensure all nodes are visited (i.e., graph is connected)
        return len(visited) == n
