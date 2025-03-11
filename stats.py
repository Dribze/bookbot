def count_words(text):
        words = text.split()
        return (len(words))

def  character_usage(text):
	char_dict = {}
	for char in text.lower():
		if char in char_dict:
			char_dict[char] += 1
		else:
			char_dict[char] = 1
	return char_dict

def sorted_characters (char_dict):
	sorted_list = []
	for  key, value in char_dict.items():
		sorted_dict = {
			'char': key,
			'count': value

		}
		sorted_list.append(sorted_dict)
	def sort_on(dict):
		return dict['count']
	sorted_list.sort( reverse=True, key=sort_on)
	return sorted_list

