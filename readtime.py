import sys

def read_time(document):
	with open(document) as f:
		content = f.read()
		word_count = count_words(content)
		readtime = calculate_read_time(word_count)
		readtime = min_to_hour(readtime) if (readtime > 59) else str(readtime) + ' minute'
	return readtime


def count_words(content):
	word_list = content.split(' ')
	return len(word_list)


def min_to_hour(readtime):
	one_min = 0.016667
	return str(one_min * readtime) + ' hour'


def calculate_read_time(word_count):
	average_words_per_min = 200
	return (word_count) / (average_words_per_min)

if len(sys.argv) < 2:
	print 'Please pass the document. Usage: python readtime document'
else:
	print read_time(sys.argv[1])
