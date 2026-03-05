#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
# from collections import defaultdict

# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         ret = []
#         adj = defaultdict(set)
#         directory = dict()
#         visited = set()

#         def dfs(adj: dict[str, set[str]], email: str, visited: set, same_accounts: list):
#             if email in visited:
#                 return
            
#             visited.add(email)
#             same_accounts.append(email)

#             for next_email in adj[email]:
#                 dfs(adj, next_email, visited, same_accounts) 

#             return

#         for account in accounts:
#             name = account[0]
#             emails = account[1:]

#             for email in emails:
#                 directory[email] = name
                
#             first = emails[0]
#             for other in emails[1:]:
#                 adj[first].add(other)
#                 adj[other].add(first)
        
#         for start in adj:
#             if start in visited:
#                 continue
            
#             same_account = []
#             dfs(adj, start, visited, same_account)

#             same_account.sort()
#             ret.append([directory[same_account[0]]] + same_account)

#         return ret

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        visited = set()
        directory = dict()
        ret = []

        for a in accounts:
            name = a[0]
            emails = a[1:]

            for e in emails:
                directory[e] = name

            first = emails[0]
            graph[first].update()
            for other in emails[1:]:
                graph[first].add(other)
                graph[other].add(first)
        
        def dfs(graph: defaultdict, email: str, merged: list, visited: set):
            if email in visited:
                return
            
            visited.add(email)
            merged.append(email)

            for next_email in graph[email]:
                dfs(graph, next_email, merged, visited)

        for e in graph:
            merged = []
            dfs(graph, e, merged, visited)

            if len(merged) > 0:
                name = directory[e]
                merged.sort()
                ret.append([name] + merged)

        return ret
            
# @lc code=end

