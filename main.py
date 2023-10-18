import gensim.downloader as g1

model = g1.load("glove-wiki-gigaword-100");


x = model.most_similar('board')
print(x)
vec = model.get_vector("board")
vec2 = model.get_vector("committee")
print(vec)
print(vec2)

