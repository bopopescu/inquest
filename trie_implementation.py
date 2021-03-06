from collections import defaultdict

# Convert the input word list to a trie type data structure 
def add_words_to_trie(words):
	trie = dict()
	for word in words:
		curdict = trie
		for letter in word: 
			curdict = curdict.setdefault(letter, {})
		curdict = curdict.setdefault('_end_', '_end_')
	return trie

# recursive helper function for trie get 
def recursive_get_word(trie, prefix, wordlist):

	for (k,v) in trie.iteritems():
		if isinstance(v,dict):
			recursive_get_word(v, prefix + k, wordlist)
		if v == '_end_':
			wordlist.append(prefix)
			
# Return all the words from input trie that match the given prefix
def get_words_from_trie(trie, prefix):
	current_dict = trie
	word = ''
	wordlist = []
	for letter in prefix:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return wordlist
	else:
		recursive_get_word(current_dict, prefix, wordlist)
	return wordlist
		


def main():
	w = []
	w.append('cat')
	w.append('caty')
	w.append('dog')
	w.append('car')
	w.append('catasys')
	trie =  add_words_to_trie(w)
	print trie
	get_words_to_trie(trie, 'catal')
	print wordlist

if __name__ == '__main__':
	main()