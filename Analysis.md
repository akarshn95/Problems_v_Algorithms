### 1) Square root of Integer

Using the concept of binary search, divide and conquer the numbers less than the given number. Since we need to find the floor of the square root, assign the latest lowest integer to be square root. 

Time Complexity - The set of integers are halved on every iteration; O(log n)
Space Complexity - O(1); 3 variables are used and they take constant space with increase in input size.


### 2) Rotated Array Search

The pivot is found out by comparing two consecutive numbers in the array, if the number at i+1 position in lesser than that in i position, i+1 is the pivot. This is found by divide and conquer by eliminating half of the array on every iteration. Once the pivot is found, if the number is less than pivot, it is not in the array. If it is more than pivot but less than last element of array, it is in the second half of the array. If the number is between first element of the array and the position before the pivot, we can eliminate the second half of the array after the pivot.

Time Complexity - The array is halved in every iteration of the search. O(log n)
Space Complexity - O(1); Constant Space

### 3) Rearrange Array Digits

Merge sort is implemented to sort the array since it has good efficiency of O(nlog n). From the sorted array (descending order), each elements is alternatively picked and append to the string of digits which is output as integers.

Time Complexity - O(nlog n) Merge Sort + O(n) -> O(nlog n)
Space Complexity - O(n); We store the sorted input list into strings whose length is proportional to the input list.

Merge sort has recursive call stack with space complexity -> O(n), O(n/2), O(n/4) .... 
Time Complexity - O(n long n)
Space Complexity - O(n)

### 4) Dutch National Flag 

Using two pointers at the start and end of the array to swap 0 and 2 when found. When 2 is found and swapped, stall the iteration to check the element swapped by 2. 

Time Complexity - O(n); One-Pass
Space Complexity - O(1); In-place sorted, constant time

### 5) Auto-complete with Tries
 
Trie data structures are used to implement. Words are inserted to tree nodes to form the trie structure for each of the words inserted with is.word=False when the character is the last of the word. For each prefix present in the word list, the suffixes are displayed accordinly. 

Time Complexity - O(n) Linear time
Space Complexity - O(n), we store the list of words that are suffixes which has worst space complexity proportional to input words

### 6) Min, Max of Unsorted Array

Using two variables to keep track of min and max, the min and max values can be found in one single pass of the array. 

Time Complexity - O(n); One-Pass
Space Complexity - O(1); Constant time, only variables used to output max and min.

### 7) HTTP Router

Tries are used to implement HTTP routing, the trie nodes and trie class is very similar to the trie classes used in Auto-complete problem. The route class is used to use these nodes to perform HTTP routing. 

add_handler has time complexity O(n); space complexity O(n)
lookup has time complexity of O(n^2); space complexity O(1)
