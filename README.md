# Python-Tasks5
# Task 1: Read a File and Handle Errors

## Problem Statement

Write a Python program that:
1. Opens and reads a text file named `sample.txt`.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.

## Implementation

Here is the Python code that accomplishes the above task:

```python
def read_file(filename):
    """Open and read a text file, printing its content line by line."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without extra whitespace
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the filename
filename = 'sample.txt'

# Call the function to read the file
read_file(filename)
```
# Task 2: Write and Append Data to a File

## Problem Statement

Write a Python program that:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

## Implementation

Here is the Python code that accomplishes the above task:

```python
def write_to_file(filename, data):
    """Write data to a file."""
    with open(filename, 'w') as file:
        file.write(data + '\n')  # Write the user input and add a newline

def append_to_file(filename, additional_data):
    """Append additional data to the file."""
    with open(filename, 'a') as file:
        file.write(additional_data + '\n')  # Append the additional data with a newline

def read_file(filename):
    """Read and display the content of the file."""
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFinal content of the file:")
        print(content)

# Specify the filename
filename = 'output.txt'

# Take user input
user_input = input("Please enter some data to write to the file: ")
write_to_file(filename, user_input)

# Take additional input to append
additional_input = input("Please enter additional data to append to the file: ")
append_to_file(filename, additional_input)

# Read and display the final content of the file
read_file(filename)
```
