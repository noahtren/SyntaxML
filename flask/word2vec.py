import gensim.downloader as api
import sys

model = api.load("glove-twitter-25")  # download the model and return as object ready for use

def find_top(query, key_list):
# query must be a string
# key list must be a list of strings such as "python for loop"
    query = query.lower().split()
    min_dist = sys.maxsize; to_return = ""
    for key in key_list:
        key = key.lower().split()
        print(query, key)
        result = model.wmdistance(query, key)
        print("Analyzing {}: Association: {}".format(key, result))
        if result < min_dist:
            min_dist = result
            to_return = key
    return " ".join(to_return)