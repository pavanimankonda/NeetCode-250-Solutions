# Remove Element

## 📝 Problem Statement

### 🔗 Problem Link

> *<a href="https://leetcode.com/problems/remove-element/description/" target="_blank">LeetCode Problem</a>*

> Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
>
> **Example 1:**
>
> **Input:** nums = [3,2,2,3], val = 3  
> **Output:** 2, nums = [2,2,_,_]  
>
> **Example 2:**
>
> **Input:** nums = [0,1,2,2,3,0,4,2], val = 2  
> **Output:** 5, nums = [0,1,4,0,3,_,_,_]  
>
> **Constraints:**
>
> - 0 <= nums.length <= 100  
> - 0 <= nums[i] <= 50  
> - 0 <= val <= 100  

---

## 🛩️ Approach 1: Brute Force

### 🔍 Idea

- Create a new array to store elements not equal to `val`.
- Copy the filtered elements back to `nums`.

### 🚀 Implementation

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int k = 0;
        int res[] = new int[n];

        for (int i = 0; i < n; i++) {
            if (nums[i] != val)
                res[k++] = nums[i];
        }
        for (int i = 0; i < k; i++) {
            nums[i] = res[i];
        }
        return k;
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### 📸 LeetCode Screenshot
![Accepted Submission](Screenshots/7.1.png)

---

## 🛩️ Approach 2: Two Pointers

### 🔍 Idea

- Use two pointers: one for iterating and another for storing valid elements.
- Modify the array in-place.

### 🚀 Implementation

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length;
        int k = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != val)
                nums[k++] = nums[i];
        }

        return k;
    }
}
```

### ⏳ Complexity Analysis

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### 📸 LeetCode Screenshot
![Accepted Submission](Screenshots/7.2.png)

