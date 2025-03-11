import sys
from stats import count_words
from stats import character_usage
from stats import sorted_characters
def get_book_text(filepath):
	with open (filepath) as f:
		file_contents = f.read()
		return file_contents
def format_report(path , word_count, sorted_list):
	report = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""

	for item in sorted_list:
		char = item['char']
		count =  item['count']
		if char.isalpha():
			report += f"\n{char}: {count}"

	report += "\n============= END ==============="
	return report

def main ():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path = sys.argv[1]
		text = get_book_text(path)
		word_count = count_words(text)
		letters_dict = character_usage(text)
		sorted_list = sorted_characters(letters_dict)
		print(format_report(path, word_count, sorted_list))

main()
