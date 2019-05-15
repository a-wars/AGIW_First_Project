from bs4 import BeautifulSoup
import numpy as np

def get_class(tag):
    classes=tag.get('class')
    return frozenset(classes or '')


def tag_to_token(tag):
    return (tag.name,get_class(tag))

class TagFrequency(object):
    def __init__(self):
        self.dictionary = {}
        self.dimension = 0

    def __call__(self, page):
        to_index = []
        soup=BeautifulSoup(page,'lxml')
        for fragment in soup.findAll():
            token = tag_to_token(fragment)
            index = self.dictionary.get(token)
            if index is not None:
                to_index.append(index)
            else:
                to_index.append(self.dimension)
                self.dictionary[token] = self.dimension
                self.dimension += 1
        vector = np.zeros((len(self.dictionary),))
        for index in to_index:
            vector[index] += 1
        return vector/np.sum(vector)


