# file_processor.py

with open("input.txt", "r") as infile:
    lines = infile.readlines()

# 줄 내용이 있는 경우만 처리
processed_lines = ["Processed: " + line.strip() for line in lines if line.strip()]

with open("output.txt", "w") as outfile:
    for line in processed_lines:
        outfile.write(line + "\n")