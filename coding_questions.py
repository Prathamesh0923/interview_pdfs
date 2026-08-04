# Python coding-round questions.
# Each item: (title, problem_statement, solution_code)

CODING_QUESTIONS = [
    ("Reverse a string",
     "Write a function to reverse a string without using built-in reverse().",
     "def reverse_string(s):\n"
     "    result = ''\n"
     "    for ch in s:\n"
     "        result = ch + result\n"
     "    return result\n\n"
     "# Pythonic one-liner:\n"
     "def reverse_string(s):\n"
     "    return s[::-1]"),
    ("Check palindrome",
     "Determine whether a given string is a palindrome (ignoring case).",
     "def is_palindrome(s):\n"
     "    s = s.lower()\n"
     "    return s == s[::-1]"),
    ("Check anagram",
     "Check if two strings are anagrams of each other.",
     "def is_anagram(a, b):\n"
     "    return sorted(a.lower()) == sorted(b.lower())\n\n"
     "# O(n) with Counter:\n"
     "from collections import Counter\n"
     "def is_anagram(a, b):\n"
     "    return Counter(a) == Counter(b)"),
    ("FizzBuzz",
     "Print numbers 1..n, but 'Fizz' for multiples of 3, 'Buzz' for 5, 'FizzBuzz' for both.",
     "def fizzbuzz(n):\n"
     "    for i in range(1, n + 1):\n"
     "        if i % 15 == 0:\n"
     "            print('FizzBuzz')\n"
     "        elif i % 3 == 0:\n"
     "            print('Fizz')\n"
     "        elif i % 5 == 0:\n"
     "            print('Buzz')\n"
     "        else:\n"
     "            print(i)"),
    ("Factorial (iterative and recursive)",
     "Compute the factorial of n.",
     "def factorial_iter(n):\n"
     "    result = 1\n"
     "    for i in range(2, n + 1):\n"
     "        result *= i\n"
     "    return result\n\n"
     "def factorial_rec(n):\n"
     "    return 1 if n <= 1 else n * factorial_rec(n - 1)"),
    ("Fibonacci sequence",
     "Generate the first n Fibonacci numbers efficiently.",
     "def fibonacci(n):\n"
     "    a, b = 0, 1\n"
     "    result = []\n"
     "    for _ in range(n):\n"
     "        result.append(a)\n"
     "        a, b = b, a + b\n"
     "    return result"),
    ("Check prime number",
     "Determine whether a number is prime.",
     "def is_prime(n):\n"
     "    if n < 2:\n"
     "        return False\n"
     "    i = 2\n"
     "    while i * i <= n:\n"
     "        if n % i == 0:\n"
     "            return False\n"
     "        i += 1\n"
     "    return True"),
    ("Count vowels and consonants",
     "Count vowels and consonants in a string.",
     "def count_vc(s):\n"
     "    vowels = set('aeiou')\n"
     "    v = c = 0\n"
     "    for ch in s.lower():\n"
     "        if ch.isalpha():\n"
     "            if ch in vowels:\n"
     "                v += 1\n"
     "            else:\n"
     "                c += 1\n"
     "    return v, c"),
    ("Find the largest element in a list",
     "Return the maximum value without using max().",
     "def find_max(nums):\n"
     "    largest = nums[0]\n"
     "    for n in nums[1:]:\n"
     "        if n > largest:\n"
     "            largest = n\n"
     "    return largest"),
    ("Second largest element",
     "Find the second largest element in a list.",
     "def second_largest(nums):\n"
     "    first = second = float('-inf')\n"
     "    for n in nums:\n"
     "        if n > first:\n"
     "            first, second = n, first\n"
     "        elif first > n > second:\n"
     "            second = n\n"
     "    return second"),
    ("Remove duplicates from a list",
     "Remove duplicates while preserving order.",
     "def dedupe(nums):\n"
     "    seen = set()\n"
     "    result = []\n"
     "    for n in nums:\n"
     "        if n not in seen:\n"
     "            seen.add(n)\n"
     "            result.append(n)\n"
     "    return result"),
    ("Count word frequency",
     "Count the frequency of each word in a sentence.",
     "from collections import Counter\n"
     "def word_freq(text):\n"
     "    return dict(Counter(text.lower().split()))"),
    ("First non-repeating character",
     "Return the first character that appears only once.",
     "from collections import Counter\n"
     "def first_unique(s):\n"
     "    counts = Counter(s)\n"
     "    for ch in s:\n"
     "        if counts[ch] == 1:\n"
     "            return ch\n"
     "    return None"),
    ("Two Sum",
     "Return indices of two numbers that add up to a target.",
     "def two_sum(nums, target):\n"
     "    seen = {}\n"
     "    for i, n in enumerate(nums):\n"
     "        if target - n in seen:\n"
     "            return [seen[target - n], i]\n"
     "        seen[n] = i\n"
     "    return []"),
    ("Reverse a list in place",
     "Reverse a list without slicing or reversed().",
     "def reverse_list(lst):\n"
     "    i, j = 0, len(lst) - 1\n"
     "    while i < j:\n"
     "        lst[i], lst[j] = lst[j], lst[i]\n"
     "        i += 1\n"
     "        j -= 1\n"
     "    return lst"),
    ("Merge two sorted lists",
     "Merge two sorted lists into one sorted list.",
     "def merge(a, b):\n"
     "    i = j = 0\n"
     "    result = []\n"
     "    while i < len(a) and j < len(b):\n"
     "        if a[i] <= b[j]:\n"
     "            result.append(a[i]); i += 1\n"
     "        else:\n"
     "            result.append(b[j]); j += 1\n"
     "    result.extend(a[i:])\n"
     "    result.extend(b[j:])\n"
     "    return result"),
    ("Binary search",
     "Implement binary search on a sorted list.",
     "def binary_search(arr, target):\n"
     "    lo, hi = 0, len(arr) - 1\n"
     "    while lo <= hi:\n"
     "        mid = (lo + hi) // 2\n"
     "        if arr[mid] == target:\n"
     "            return mid\n"
     "        elif arr[mid] < target:\n"
     "            lo = mid + 1\n"
     "        else:\n"
     "            hi = mid - 1\n"
     "    return -1"),
    ("Bubble sort",
     "Sort a list using bubble sort.",
     "def bubble_sort(arr):\n"
     "    n = len(arr)\n"
     "    for i in range(n):\n"
     "        swapped = False\n"
     "        for j in range(n - i - 1):\n"
     "            if arr[j] > arr[j + 1]:\n"
     "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n"
     "                swapped = True\n"
     "        if not swapped:\n"
     "            break\n"
     "    return arr"),
    ("Quick sort",
     "Sort a list using quicksort.",
     "def quick_sort(arr):\n"
     "    if len(arr) <= 1:\n"
     "        return arr\n"
     "    pivot = arr[len(arr) // 2]\n"
     "    left = [x for x in arr if x < pivot]\n"
     "    mid = [x for x in arr if x == pivot]\n"
     "    right = [x for x in arr if x > pivot]\n"
     "    return quick_sort(left) + mid + quick_sort(right)"),
    ("Merge sort",
     "Sort a list using merge sort.",
     "def merge_sort(arr):\n"
     "    if len(arr) <= 1:\n"
     "        return arr\n"
     "    mid = len(arr) // 2\n"
     "    left = merge_sort(arr[:mid])\n"
     "    right = merge_sort(arr[mid:])\n"
     "    i = j = 0\n"
     "    out = []\n"
     "    while i < len(left) and j < len(right):\n"
     "        if left[i] <= right[j]:\n"
     "            out.append(left[i]); i += 1\n"
     "        else:\n"
     "            out.append(right[j]); j += 1\n"
     "    out.extend(left[i:]); out.extend(right[j:])\n"
     "    return out"),
    ("Sum of digits",
     "Compute the sum of digits of an integer.",
     "def digit_sum(n):\n"
     "    n = abs(n)\n"
     "    total = 0\n"
     "    while n > 0:\n"
     "        total += n % 10\n"
     "        n //= 10\n"
     "    return total"),
    ("Reverse an integer",
     "Reverse the digits of an integer.",
     "def reverse_int(n):\n"
     "    sign = -1 if n < 0 else 1\n"
     "    rev = int(str(abs(n))[::-1])\n"
     "    return sign * rev"),
    ("Check Armstrong number",
     "Check if a number equals the sum of its digits each raised to the count of digits.",
     "def is_armstrong(n):\n"
     "    digits = str(n)\n"
     "    p = len(digits)\n"
     "    return n == sum(int(d) ** p for d in digits)"),
    ("GCD and LCM",
     "Compute the GCD and LCM of two numbers.",
     "def gcd(a, b):\n"
     "    while b:\n"
     "        a, b = b, a % b\n"
     "    return a\n\n"
     "def lcm(a, b):\n"
     "    return a * b // gcd(a, b)"),
    ("Count occurrences of an element",
     "Count how many times a value appears in a list.",
     "def count_occurrences(lst, target):\n"
     "    count = 0\n"
     "    for x in lst:\n"
     "        if x == target:\n"
     "            count += 1\n"
     "    return count"),
    ("Flatten a nested list",
     "Flatten an arbitrarily nested list into a flat list.",
     "def flatten(nested):\n"
     "    result = []\n"
     "    for item in nested:\n"
     "        if isinstance(item, list):\n"
     "            result.extend(flatten(item))\n"
     "        else:\n"
     "            result.append(item)\n"
     "    return result"),
    ("Find missing number 1..n",
     "Given n-1 distinct numbers from 1..n, find the missing one.",
     "def missing_number(nums, n):\n"
     "    expected = n * (n + 1) // 2\n"
     "    return expected - sum(nums)"),
    ("Find duplicates in a list",
     "Return all elements that appear more than once.",
     "from collections import Counter\n"
     "def find_duplicates(nums):\n"
     "    return [k for k, v in Counter(nums).items() if v > 1]"),
    ("Move all zeros to end",
     "Move all zeros in a list to the end while keeping order of non-zeros.",
     "def move_zeros(nums):\n"
     "    pos = 0\n"
     "    for n in nums:\n"
     "        if n != 0:\n"
     "            nums[pos] = n\n"
     "            pos += 1\n"
     "    for i in range(pos, len(nums)):\n"
     "        nums[i] = 0\n"
     "    return nums"),
    ("Rotate a list by k",
     "Rotate a list to the right by k positions.",
     "def rotate(nums, k):\n"
     "    k %= len(nums)\n"
     "    return nums[-k:] + nums[:-k]"),
    ("Check balanced parentheses",
     "Check whether brackets ()[]{} in a string are balanced.",
     "def is_balanced(s):\n"
     "    pairs = {')': '(', ']': '[', '}': '{'}\n"
     "    stack = []\n"
     "    for ch in s:\n"
     "        if ch in '([{':\n"
     "            stack.append(ch)\n"
     "        elif ch in pairs:\n"
     "            if not stack or stack.pop() != pairs[ch]:\n"
     "                return False\n"
     "    return not stack"),
    ("Longest common prefix",
     "Find the longest common prefix among a list of strings.",
     "def longest_common_prefix(strs):\n"
     "    if not strs:\n"
     "        return ''\n"
     "    prefix = strs[0]\n"
     "    for s in strs[1:]:\n"
     "        while not s.startswith(prefix):\n"
     "            prefix = prefix[:-1]\n"
     "            if not prefix:\n"
     "                return ''\n"
     "    return prefix"),
    ("Maximum subarray sum (Kadane)",
     "Find the contiguous subarray with the largest sum.",
     "def max_subarray(nums):\n"
     "    best = current = nums[0]\n"
     "    for n in nums[1:]:\n"
     "        current = max(n, current + n)\n"
     "        best = max(best, current)\n"
     "    return best"),
    ("Count set bits",
     "Count the number of 1s in the binary representation of n.",
     "def count_bits(n):\n"
     "    count = 0\n"
     "    while n:\n"
     "        n &= n - 1\n"
     "        count += 1\n"
     "    return count"),
    ("Find pairs with given sum",
     "Find all unique pairs in a list that sum to a target.",
     "def pair_sum(nums, target):\n"
     "    seen = set()\n"
     "    pairs = set()\n"
     "    for n in nums:\n"
     "        complement = target - n\n"
     "        if complement in seen:\n"
     "            pairs.add(tuple(sorted((n, complement))))\n"
     "        seen.add(n)\n"
     "    return list(pairs)"),
    ("Title case a sentence",
     "Capitalize the first letter of each word.",
     "def title_case(text):\n"
     "    return ' '.join(w.capitalize() for w in text.split())"),
    ("Find the longest word",
     "Return the longest word in a sentence.",
     "def longest_word(text):\n"
     "    return max(text.split(), key=len)"),
    ("Sum of even numbers",
     "Return the sum of even numbers in a list.",
     "def sum_even(nums):\n"
     "    return sum(n for n in nums if n % 2 == 0)"),
    ("Transpose a matrix",
     "Transpose a 2D matrix (list of lists).",
     "def transpose(matrix):\n"
     "    return [list(row) for row in zip(*matrix)]"),
    ("Merge two dictionaries",
     "Merge two dicts; values from the second override the first.",
     "def merge_dicts(a, b):\n"
     "    return {**a, **b}"),
    ("Group anagrams",
     "Group a list of words into anagram clusters.",
     "from collections import defaultdict\n"
     "def group_anagrams(words):\n"
     "    groups = defaultdict(list)\n"
     "    for w in words:\n"
     "        groups[''.join(sorted(w))].append(w)\n"
     "    return list(groups.values())"),
    ("Decimal to binary",
     "Convert a non-negative integer to its binary string.",
     "def to_binary(n):\n"
     "    if n == 0:\n"
     "        return '0'\n"
     "    bits = ''\n"
     "    while n > 0:\n"
     "        bits = str(n % 2) + bits\n"
     "        n //= 2\n"
     "    return bits"),
    ("Check perfect number",
     "A perfect number equals the sum of its proper divisors.",
     "def is_perfect(n):\n"
     "    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n"),
    ("Find common elements in two lists",
     "Return elements present in both lists.",
     "def common_elements(a, b):\n"
     "    return list(set(a) & set(b))"),
    ("Caesar cipher",
     "Shift each letter by k positions (encrypt).",
     "def caesar(text, k):\n"
     "    result = []\n"
     "    for ch in text:\n"
     "        if ch.isalpha():\n"
     "            base = ord('A') if ch.isupper() else ord('a')\n"
     "            result.append(chr((ord(ch) - base + k) % 26 + base))\n"
     "        else:\n"
     "            result.append(ch)\n"
     "    return ''.join(result)"),
    ("Count words, chars, lines in text",
     "Return counts of lines, words, and characters in a block of text.",
     "def text_stats(text):\n"
     "    lines = text.splitlines()\n"
     "    words = text.split()\n"
     "    return {'lines': len(lines), 'words': len(words), 'chars': len(text)}"),
    ("Find intersection node count / unique counts",
     "Return how many distinct values appear in a list.",
     "def distinct_count(nums):\n"
     "    return len(set(nums))"),
    ("Implement a stack using a list",
     "Implement a basic stack with push, pop, peek.",
     "class Stack:\n"
     "    def __init__(self):\n"
     "        self._data = []\n"
     "    def push(self, x):\n"
     "        self._data.append(x)\n"
     "    def pop(self):\n"
     "        return self._data.pop()\n"
     "    def peek(self):\n"
     "        return self._data[-1]\n"
     "    def is_empty(self):\n"
     "        return not self._data"),
    ("Implement a queue using two stacks",
     "Build a FIFO queue using two stacks.",
     "class Queue:\n"
     "    def __init__(self):\n"
     "        self.inbox, self.outbox = [], []\n"
     "    def enqueue(self, x):\n"
     "        self.inbox.append(x)\n"
     "    def dequeue(self):\n"
     "        if not self.outbox:\n"
     "            while self.inbox:\n"
     "                self.outbox.append(self.inbox.pop())\n"
     "        return self.outbox.pop()"),
    ("Sum of list using recursion",
     "Compute the sum of a list recursively.",
     "def rec_sum(nums):\n"
     "    if not nums:\n"
     "        return 0\n"
     "    return nums[0] + rec_sum(nums[1:])"),
    ("Power of a number",
     "Compute a raised to b using fast exponentiation.",
     "def power(a, b):\n"
     "    result = 1\n"
     "    while b > 0:\n"
     "        if b & 1:\n"
     "            result *= a\n"
     "        a *= a\n"
     "        b >>= 1\n"
     "    return result"),
    ("Find the median of a list",
     "Return the median value of a list of numbers.",
     "def median(nums):\n"
     "    s = sorted(nums)\n"
     "    n = len(s)\n"
     "    mid = n // 2\n"
     "    if n % 2:\n"
     "        return s[mid]\n"
     "    return (s[mid - 1] + s[mid]) / 2"),
    ("Remove punctuation from text",
     "Strip all punctuation characters from a string.",
     "import string\n"
     "def remove_punctuation(text):\n"
     "    return text.translate(str.maketrans('', '', string.punctuation))"),
    ("Check if two strings are rotations",
     "Check whether one string is a rotation of another.",
     "def is_rotation(a, b):\n"
     "    return len(a) == len(b) and b in (a + a)"),
    ("Find the longest substring without repeats",
     "Length of the longest substring without repeating characters.",
     "def longest_unique(s):\n"
     "    seen = {}\n"
     "    start = best = 0\n"
     "    for i, ch in enumerate(s):\n"
     "        if ch in seen and seen[ch] >= start:\n"
     "            start = seen[ch] + 1\n"
     "        seen[ch] = i\n"
     "        best = max(best, i - start + 1)\n"
     "    return best"),
]
