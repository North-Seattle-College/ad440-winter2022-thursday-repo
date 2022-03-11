from cv2 import kmeans
from sklearn.cluster import KMeans

def get_sentence_length_list(sentences: list) -> list:
	out = []
	for sentence in sentences:
		out.append([len(sentence), 0])
	return out

def main():
	sentences = ['a', 'a', 'a', 'asdf', 'c', 'asdf', 'asdf', 'b',  'asdflkjh', 'asdflkjh', 'asdflkjh']
	sentence_length = get_sentence_length_list(sentences)
	print(sentence_length)
	kmeans = KMeans(init='random', n_clusters=3, max_iter=300)
	kmeans.fit(sentence_length)
	print(kmeans.labels_)

if __name__ == '__main__':
	main()

"""
use package kneed to determine the number of clusters
"""
