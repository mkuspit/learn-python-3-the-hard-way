import sys
script, input_encoding, error = sys.argv

def main(langugage_file, encoding, errors):
	line = langugage_file.readline()
	if line:
		print_line(line, encoding, errors)
		return main(langugage_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, '<===>', cooked_string)




languages = open('languages.txt', encoding='utf-8')

main(languages, input_encoding, error)



# file from https://learnpythonthehardway.org/python3/languages.txt

# One must run it like this:
# python 23_strings_bytes_and_character_encoding.py utf-8 strict
