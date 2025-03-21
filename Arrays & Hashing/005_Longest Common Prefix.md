# Longest Common Prefix

## 📝 Problem Statement

### 🔗 Problem Link

> *[LeetCode Problem](https://leetcode.com/problems/longest-common-prefix/description/)*

> Write a function to find the longest common prefix string amongst an array of strings.
>
> If there is no common prefix, return an empty string "".
>
> **Example 1:**
>
> **Input:** strs = ["flower","flow","flight"]  
> **Output:** "fl"  
>
> **Example 2:**
>
> **Input:** strs = ["dog","racecar","car"]  
> **Output:** ""  
> **Explanation:** There is no common prefix among the input strings.
>
> **Constraints:**
>
> - 1 <= strs.length <= 200  
> - 0 <= strs[i].length <= 200  
> - strs[i] consists of only lowercase English letters if it is non-empty.  

---

## 🛩️ Approach 1: Vertical Scanning

### 🔍 Idea

- Compare characters column by column across all strings.
- If a mismatch is found, return the prefix found so far.

### 🚀 Implementation

```java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        int n = strs.length;

        for (int i = 0; i < strs[0].length(); i++) {
            for (int j = 0; j < n; j++) {
                if (i == strs[j].length() || strs[j].charAt(i) != strs[0].charAt(i)) {
                    return strs[j].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n * m)`
- **Space Complexity:** `O(1)` (no extra space used)

### 📸 LeetCode Screenshot
![Accepted Submission](Screenshots/5.1.png)

---

## 🛩️ Approach 2: Sorting

### 🔍 Idea

- Sort the array lexicographically so that the first and last elements are the most different.
- Compare the first and last string to determine the common prefix.

### 🚀 Implementation

```java
import java.util.Arrays;

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1)
            return strs[0];

        Arrays.sort(strs);
        int N = Math.min(strs[0].length(), strs[strs.length - 1].length());

        for (int i = 0; i < N; i++) {
            if (strs[0].charAt(i) != strs[strs.length - 1].charAt(i))
                return strs[0].substring(0, i);
        }
        return strs[0];
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n * m log m)`
- **Space Complexity:** `O(1)` or `O(m)` (depending on sorting algorithm)

### 📸 LeetCode Screenshot
![Accepted Submission](Screenshots/5.2.png)

