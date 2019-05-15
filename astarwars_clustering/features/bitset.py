from html.parser import HTMLParser
from bitarray import bitarray


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = ''
    
    # Override start and end tag handler
    def handle_starttag(self, tag, attrs):
        self.out = self.out+''+tag

    def handle_endtag(self, tag):
        self.out = self.out+'/'+tag


# Windows and bit array
def windows(s, l):
    res = []
    for i in range(len(s)-l):
        sub = s[i:i+l]
        res.append(sub)
    return res


def to_bit_array(data, wl, bit_len):
    parser = MyHTMLParser()
    parser.feed(data)

    ws = windows(parser.out, wl)
    ba = bitarray(bit_len)
    ba.setall(0)

    for w in ws:
        ba[hash(w) % bit_len] = 1

    baAsList = list(range(len(ba)))
    for index, value in enumerate(ba):
        if value:
            baAsList[index] = 1
        else:
            baAsList[index] = 0
    return baAsList