def cosine_similarity(vec1,vec2):
	#for numerator
	numerator = 0
	for key in vec1.keys():
		try:
			if vec2[key]:
				#check if this is the right thing to do!
				numerator += vec2[key]*vec1[key]
		except:
			pass

	#for denominator
	sum1, sum2=0,0
	for i in range(len(vec1.values())): #gets number of elements in the vector
		sum1+=list(vec1.values())[i]**2
	for i in range(len(vec2.values())):
		sum2+=list(vec2.values())[i]**2

	denominator = ((sum1)*(sum2))**(1/2)
	return numerator/denominator
# print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
# dictionary =  {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1,"unattractive": 1}

def build_semantic_descriptors(sentences):
        
	master_dictionary = {}
	end = len(sentences)
	i=0
	while i<end:
		sentence = sentences[i]
		for duplicate_words in sentence:
			while sentence.count(duplicate_words)>1:
				sentence.remove(duplicate_words)

		for search_word in sentence:
			if (search_word not in master_dictionary) and search_word!= "":
				master_dictionary[search_word]={}
			for word in sentence:
				if search_word != word and word!="" and search_word!="":
					if word not in master_dictionary[search_word]:
						master_dictionary[search_word][word]=0
					master_dictionary[search_word][word]+=1
		i+=1

	return  master_dictionary


# sentences=[["i", "am", "a", "sick", "man"],
#  ["i", "am", "a", "spiteful", "man"],
#  ["i", "am", "an", "unattractive", "man"],
#  ["i", "believe", "my", "liver", "is", "diseased"],
#  ["however", "i", "know", "nothing", "at", "all", "about", "my",
#  "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
# build_semantic_descriptors(sentences)['nothing'])


def build_semantic_descriptors_from_files(filenames):
	text=""
	for file in filenames:
		f = open(file, "r", encoding = "latin1")
		text+=f.read().lower()

	other_punct = [",", "-", "--", ":", ";", "\n"]
	
	text = text.replace(","," ")
	text = text.replace("\n"," ")
	text = text.replace(";"," ")
	text = text.replace(":"," ")
	text = text.replace("--"," ")
	text = text.replace("-"," ")

	text = text.replace("!",".")
	text = text.replace("?",".")

	text_list = text.split(".")

	master_text_list=[]
	for sentence in text_list:
		master_text_list.append(sentence.split(" "))

	dictionary = build_semantic_descriptors(master_text_list)
	return dictionary

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
	score = []
	if word not in semantic_descriptors:
		return choices[0]
	for choice in choices:#iterates through each word in choices

		if choice not in semantic_descriptors:#the score for that choice is -1
			score.append(-1)

		else:
			returned_score = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice]) #the score for that choice is passed
			score.append(returned_score)
	max_score = max(score)
	return choices[score.index(max_score)]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
	f = open(filename,"r", encoding = "latin1")
	text = f.read()
	questions = text.split("\n")
	score = 0
	for question in questions:
		words = question.split(" ")
		if len(words)==0:
			continue

		# print("most similar word",most_similar_word(words[0], words[2:4], semantic_descriptors, similarity_fn))

		if words[1] == most_similar_word(words[0], words[2:], semantic_descriptors, similarity_fn):
			score += 1

	percentage_score = score/len(questions) * 100
	return percentage_score

if __name__ == "__main__":
	semantic_descriptors=build_semantic_descriptors_from_files(['wp.txt', 'sw.txt'])
	print(run_similarity_test("test.txt", semantic_descriptors, cosine_similarity))
    