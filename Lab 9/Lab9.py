import random
import urllib.request
#Part a
def count_words(w):
	# f=open("text.txt","r")
	# print("woah", f.read())
	text="I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me."
	text = text.split(" ")

	dictionary = {}
	for word in text:
		if word not in dictionary:
			dictionary[word]=text.count(word)
	return dictionary[w]


#print(count_words("man."))

def get_dict_ppj():
	f=open("ppj.txt","r")
	text= f.read()
	text = text.split(" ")

	dictionary = {}
	for word in text:
		if word not in dictionary:
			dictionary[word]=text.count(word)
	return dictionary

# print(get_dict_ppj())
#part b
def top10(L):
	largest_int_list=[]
	for i in range(0,10):
		largest_int = max(L)
		largest_int_list.append(largest_int)
		L.remove(largest_int)

		# for j in range(L.count(largest_int)):
		# 	L.remove(largest_int)

	return largest_int_list


# L=[]
# for i in range(1,100):
# 	L.append(random.randint(1,10))
# print(top10(L))


#Part c
def most_frequent(freq):
	list_of_words = []
	word_list = list(freq.keys())
	count_list = list(freq.values())


	max_counts = top10(list(freq.values()))
	for count in max_counts:
		max_index = count_list.index(count)
		list_of_words.append(word_list[max_index])

		word_list.pop(max_index)
		count_list.pop(max_index)
	return list_of_words


# text="I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me."
# text = text.split(" ")

# dictionary = {}
# for word in text:
# 	if word not in dictionary:
# 		dictionary[word]=text.count(word)

# print(most_frequent(dictionary))



#problem 4
def get_search_results_num(url):
	f = urllib.request.urlopen(url)
	page = f.read().decode("utf-8")
	f.close()
	index1 = page.index("fz-14 lh-22\">About ")
	index2 = page.index(" search results</span></h2>")
	return page[index1+len("fz-14 lh-22\">About "):index2]

	return page[index1:index2]
# get_search_results_num("https://ca.search.yahoo.com/search;_ylt=Av3YHOEya_QRKgRTD8kMWgst17V_?p=python&toggle=1&cop=mss&ei=UTF-8&fr=yfp-t-715&fp=1")

def choose_variant(variants):
	original_url = "https://ca.search.yahoo.com/search;?p="

	text_string_1=variants[0].replace(" ", "%20")
	text_string_2=variants[1].replace(" ", "%20")
	print(text_string_1)
	url_1 = original_url+text_string_1#.replace("python", variants[0])
	results_1 = get_search_results_num(url_1)
	url_2 = original_url+text_string_2#.replace("python", variants[1])
	results_2 = get_search_results_num(url_2)

	print(results_1, results_2)
	if int(results_1.replace(",",""))>int(results_2.replace(",","")):
		return variants[0]
	return variants[1]

print(choose_variant(["five-year anniversary", "fifth anniversary"]))