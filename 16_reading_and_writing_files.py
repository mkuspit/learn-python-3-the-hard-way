# List of commands you can give to files:
# close             save and close a file
# read              read content of a file
# readline          read just one line of a file
# truncate          empty the contents of a file
# write('stuff')    writes 'stuff' to a file
# seek(0)           moves read/write location to the beginning of a file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, fit Ctrl-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input('line1: ')
line2 = input('line2: ')
line3 = input('line3: ')

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally we close it.")
target.close()

# One must run it like this:
# python 16_reading_and_writing_files.py ex16.txt
