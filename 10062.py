from collections import defaultdict

class Solution:
    def remainingMethods(self, n, k, invocations):
        # 建立调用图
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)

        # 查找可疑方法
        suspicious_methods = set()

        def dfs(method):
            if method in suspicious_methods:
                return
            suspicious_methods.add(method)
            for neighbor in graph[method]:
                dfs(neighbor)

        # 从 k 开始 DFS，标记所有可疑方法
        dfs(k)

        # 查找所有不被可疑方法调用的方法
        invoker = set()
        for a, b in invocations:
            if b in suspicious_methods:
                invoker.add(a)

        # 结果应是所有方法减去可疑方法和其调用者
        remaining_methods = set(range(n)) - suspicious_methods - invoker

        return list(remaining_methods)

# 示例使用
sol = Solution()

# 第一题
n1 = 4
k1 = 1
invocations1 = [[1, 2], [0, 1], [3, 2]]
remaining1 = sol.remainingMethods(n1, k1, invocations1)
print(remaining1)  # 应该输出 [0, 1, 2, 3]

# 第二题
n2 = 5
k2 = 0
invocations2 = [[1, 2], [0, 2], [0, 1], [3, 4]]
remaining2 = sol.remainingMethods(n2, k2, invocations2)
print(remaining2)  # 应该输出 [3, 4]
