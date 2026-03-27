| Day | Title | Topic | Difficulty | Time Complexity |
|-----|-------|-------|------------|----------------|
| 21 | Valid Parentheses | Stack | Easy | O(n), where 'n' is the length of the input string. We iterate through the string once, and each stack operation (push, pop, peek) takes O(1) time.
| 20 | Word Pattern | Hash Map | Easy | O(L + N), where L is the total length of the string 's' (due to splitting and iterating through words) and N is the length of the 'pattern'. In the worst case, L dominates N, so it can be simplified to O(L). Hash map operations (insertion, lookup) take O(1) on average.
| 19 | Container With Most Water | Arrays, Two Pointers | Medium | O(n)
| 18 | Number of 1 Bits | Bit Manipulation | Easy | O(k), where k is the number of set bits in the input integer n. In the worst case, k can be log(n) (e.g., for n = 2^m - 1, all m bits are set). Therefore, the time complexity is O(log n).
| 17 | Subtree of Another Tree | Tree, Depth-First Search, Binary Tree | Easy | Let N be the number of nodes in the 'root' tree and M be the number of nodes in the 'subRoot' tree.

The `is_subtree` function traverses each node in the 'root' tree. For each node, it potentially calls `is_same_tree`.

The `is_same_tree` function, in the worst case, visits all M nodes of `subRoot`.

Since `is_subtree` makes a call to `is_same_tree` for each of the N nodes in the `root` tree, the total time complexity is O(N * M).
| 16 | Remove Linked List Elements | Linked List | Easy | O(N), where N is the number of nodes in the linked list. We traverse the list once.
| 15 | Valid Parentheses | Stack | Easy | O(n)
| 14 | Invert Binary Tree | Tree, Recursion | Easy | O(N)
| 13 | Merge Two Sorted Lists | Linked Lists | Easy | O(m + n)
| 12 | Invert Binary Tree | Tree, Recursion | Easy | O(N)
| 11 | Sum of Root To Leaf Binary Numbers | Binary Tree, Depth-First Search, Bit Manipulation | Medium | O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once during the Depth-First Search traversal.
| 10 | Valid Palindrome | Strings | Easy | O(N), where N is the length of the input string. In the worst case, both pointers traverse the entire string once.
| 9 | Middle of the Linked List | Linked List | Easy | O(N)
| 8 | Find the Duplicate Number | Arrays, Cycle Detection (Floyd's Tortoise and Hare) | Medium | O(N)
| 7 | Minimum Depth of Binary Tree | Tree, Breadth-First Search (BFS) | Easy | O(N), where N is the number of nodes in the binary tree. In the worst case, we visit each node exactly once.
| 6 | Best Time to Buy and Sell Stock | Arrays, Greedy | Easy | O(n)
| 5 | Delete Node in a Singly-Linked List (Given Node Only) | Linked List | Medium | O(1)
| 4 | Longest Common Prefix | String Manipulation | Easy | O(N * L_min), where N is the number of strings in the input list, and L_min is the length of the shortest string. In the worst case, we iterate through each character of the shortest string (up to L_min characters), and for each character, we compare it with the corresponding character in all N-1 other strings.
| 3 | Roman to Integer | String Manipulation, Hash Map | Easy | O(N), where N is the length of the Roman numeral string. The algorithm iterates through the string once.
| 2 | Palindrome Number | Mathematics | Easy | O(log N), where N is the input integer. The number of digits in N is approximately log10(N). In each step of the while loop, we effectively remove one digit from 'x', thus the number of iterations is proportional to the number of digits in N.
| 2 | Palindrome Number | Mathematics | Easy | O(log N), where N is the input integer. The number of digits in N is approximately log10(N). In each step of the while loop, we effectively remove one digit from 'x', thus the number of iterations is proportional to the number of digits in N.
| 1 | Two Sum | Arrays, Hash Tables | Easy | O(n)
