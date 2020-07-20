from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

# One must run it like this:
# python 15_reading_files.py ex15.txt

### Study Drills
txt.close()
txt_again.close()
