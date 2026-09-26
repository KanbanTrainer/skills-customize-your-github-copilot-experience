# 📘 Assignment: Python Data Structures

## 🎯 Objective

Practice organizing and manipulating collections of data in Python using lists, dictionaries, and sets/tuples.

## 📝 Tasks

### 🛠️ Working with Lists

#### Description
Write a function called `top_scores()` that takes a list of numbers and returns the three highest scores in descending order.

#### Requirements
Completed program should:

- Accept a list of numbers as an argument.
- Sort the scores without modifying the original list.
- Return a list containing the top 3 scores, highest first.
- Example usage:
  ```python
  print(top_scores([55, 90, 72, 88, 64]))  # [90, 88, 72]
  ```

### 🛠️ Working with Dictionaries

#### Description
Write a function called `count_words()` that takes a string of text and returns a dictionary counting how many times each word appears.

#### Requirements
Completed program should:

- Split the input string into words.
- Use a dictionary to map each word to the number of times it appears.
- Ignore case (e.g., `"Cat"` and `"cat"` should count as the same word).
- Example usage:
  ```python
  print(count_words("cat dog Cat bird dog cat"))
  # {'cat': 3, 'dog': 2, 'bird': 1}
  ```

### 🛠️ Working with Sets and Tuples

#### Description
Write a function called `common_favorites()` that takes two lists of favorite items and returns the items shared between them.

#### Requirements
Completed program should:

- Convert each list to a set to find the shared items.
- Return the result as a tuple of the common items, sorted alphabetically.
- Example usage:
  ```python
  print(common_favorites(["pizza", "sushi", "tacos"], ["tacos", "pasta", "pizza"]))
  # ('pizza', 'tacos')
  ```
