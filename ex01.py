import Mecab
m = MeCab.Tagger()
te = m.parse('아버지가방에들어가신다')
print(te)