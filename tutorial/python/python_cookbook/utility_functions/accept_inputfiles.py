import fileinput

# fileinput.input() returns an instance of FileInput class
with fileinput.input() as f_input:
    for line in f_input:
        print(f_input.filename(), f_input.fileno(), line, end='')