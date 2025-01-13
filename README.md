# README

## Program Overview

- Implementing in Python
- All unique lines across the files are collected.
- Blank lines are removed.
- Lines are sorted lexicographically in the output.

## Pre-Requisites

Python3.x.x
UNIX/LINUX Terminal


### Instructions
1. Save the `fileConsolidation.py` script to your desired location.
2. Run the program using the command:
   ```
   python3 fileConsolidation.py <input_dir> <output_file>
   ```
   Replace `<input_dir>` with the path to the data directory containing input text files and `<output_file>` with the desired path for the consolidated output file.

3. Run python3 tests/testFileConsolidation.py to run all unit test cases

### Example
#### Input Directory Structure:
```
data/
  file1.txt
  file2.txt
```
#### Content of `file1.txt`:
```
apple
banana

cactus
```
#### Content of `file2.txt`:
```
apple
banana
dinosaur
dinosaur
frankfurter
```
#### Command:
```
python fileConsolidation.py data output.txt
```
#### Resulting `output.txt`:
```
apple
apple banana
banana
cactus
dinosaur
frankfurter
```

## Algorithm
1. Read all files from the input directory.
2. Use a set to collect unique lines, stripping whitespace and excluding blanks.
3. Sort the collected lines lexicographically.
4. Write the sorted lines to the output file.

## Complexity Analysis
- **Time Complexity**:
  - Reading files: O(n), where `n` is the total number of lines across all files.
  - Sorting: O(m log m), where `m` is the number of unique lines.
  - Overall: O(n + m log m).
- **Space Complexity**:
  - Set for unique lines: O(m), where `m` is the number of unique lines.

## Additional Test Cases
1. **Empty Directory**:
   - Input: No files in the directory.
   - Output: An empty file.

2. **Duplicate Lines Across Files**:
   - Input: `file1.txt` contains `apple`, `file2.txt` contains `apple`.
   - Output: `apple` (single occurrence).

3. **Large Dataset**:
   - Input: Multiple files with overlapping and unique entries.
   - Output: Correctly consolidated and sorted output.

4. **Files with Only Blank Lines**:
   - Input: Files with no non-blank lines.
   - Output: An empty file.

