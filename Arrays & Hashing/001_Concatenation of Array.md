# Concatenation of Array

## 📝 Problem Statement

### 🔗 Problem Link

> *[LeetCode Problem](https://leetcode.com/problems/concatenation-of-array/description/)*

> Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
>
> Specifically, ans is the concatenation of two nums arrays.
>
> Return the array ans.
>
> **Example 1:**
>
> **Input:** nums = [1,2,1]
> **Output:** [1,2,1,1,2,1]
> **Explanation:** The array ans is formed as follows:
>
> - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
> - ans = [1,2,1,1,2,1]
>
> **Example 2:**
>
> **Input:** nums = [1,3,2,1]
> **Output:** [1,3,2,1,1,3,2,1]
> **Explanation:** The array ans is formed as follows:
>
> - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
> - ans = [1,3,2,1,1,3,2,1]
>
> **Constraints:**
>
> - n == nums.length
> - 1 <= n <= 1000
> - 1 <= nums[i] <= 1000

## 🔹 Approach 1: Iteration (Two Pass)

### 🔍 Idea

- We iterate twice over the `nums` array to construct the `ans` array.
- We maintain an index `idx` and fill `ans` sequentially.

### 🚀 Implementation

```java
public class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2 * nums.length];
        int idx = 0;
        for (int i = 0; i < 2; i++) {
            for (int num : nums) {
                ans[idx++] = num;
            }
        }
        return ans;
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` for the output array.

### 📸 LeetCode Screenshot

![Accepted Submission](Screenshots/approach1.png)

> *Attach or link a screenshot of the accepted submission for this approach on LeetCode.*

---

## 🔹 Approach 2: Iteration (One Pass)

### 🔍 Idea

- Instead of iterating twice, we use a single loop.
- We directly assign values to `ans[i]` and `ans[i + n]` in one pass.

### 🚀 Implementation

```java
public class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) {
            ans[i] = ans[i + n] = nums[i];
        }
        return ans;
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` for the output array.

### 📸 LeetCode Screenshot

![Accepted Submission](Screenshots/approach1.png)

> *Attach or link a screenshot of the accepted submission for this approach on LeetCode.* \*
>
> ---
>
> &#x20;
