import os
import sys

def consolidateFiles(input_dir, out_file):
    try:
        if not os.path.isdir(input_dir):
            raise ValueError(f"Invalid input directory: {input_dir}")

        unique_lines = set() ## init a set() to add all unique lines 

        # Read all files in the directory
        for filename in os.listdir(input_dir):
            file_path = os.path.join(input_dir, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    for line in file:
                        clean_line = line.strip()    ## strip any whitespaces
                        if clean_line:               ## Exclude blank lines
                            unique_lines.add(clean_line) ## append all cleanedup lines to unique_line 


        sorted_lines = sorted(unique_lines)          ## Sort lines lexicographically

        # Write to output file
        with open(out_file, 'w') as out_file:
            out_file.write("\n".join(sorted_lines) + "\n")

        print(f"Consolidation complete. Output written to {out_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python consolidateFiles.py <input_dir> <out_file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file_path = sys.argv[2]

    consolidateFiles(input_directory, output_file_path)
