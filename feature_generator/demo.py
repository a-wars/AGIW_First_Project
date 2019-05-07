from features import TagFrequency
import numpy as np


html_src1='<html><body><ul class="list1"><li>A</li><li>B</li></ul><ul class="list2"><li>Y</li><li>Z</li></ul></body></html>'
html_src2='<html><body><p>Another page with a paragraph tag </p></body></html>'
vectorizer=TagFrequency()

matrix=[]
feature_vec1=np.array(vectorizer(html_src1))
feature_vec2=np.array(vectorizer(html_src2))

matrix.append(feature_vec1)
matrix.append(feature_vec2)
for vec in matrix:
    vec=np.pad(vec,(0,3),'constant')
    print(type(vec))
    print(vec)
    print('\n')