# -*- coding: cp1251 -*-
from rutermextract import TermExtractor
import codecs
import re
import os
term_extractor = TermExtractor()

def main():
    #text = u'Съешь ещё этих мягких французских булок да выпей же чаю.'
    f = codecs.open('file.csv', 'w', 'cp1251')
    for name in os.listdir('D:\Articles'):
        path = os.path.join('D:\Articles', name)
        print path
        print find_keywords1(path)
        f.write(name + u';' + extract_keywords(path) + u';' + find_keywords1(path) + u'\n')
    f.close()
    
    
##def find_keywords(path):
##    f = codecs.open(path, 'r', 'cp1251')
##    text = f.read()
##    kw = re.findall(u'Ключевые слова:.+\.', text)
##    print kw
##    string = kw[0]
##    print string
##    for line in f:
##        print line
##        if re.search(u'[Кк]лючевые слова', line) != None:
##            line = line[15:]
##            print line

def find_keywords1(path):
    string = ''
    kw = ''
    f = codecs.open(path, 'r', 'cp1251')
    for line in f:
        line.lstrip()
        line.rstrip()
        line = re.sub(u' +', u' ', line)
        if kw != '':
            kw += line
            if re.search(u'\.', line) != None:
                break
        if re.search(u'Ключевые слова', line) != None:
            kw += line
    kw = re.sub(u'\-\n', u'', kw)
    kw = re.sub(u'\n', u'', kw)
    kw = re.sub(u' +', u' ', kw)
    kwords = re.split(u'[:,;]', kw)
    kwords = kwords[1:]
    for k in kwords:
        line.lstrip()
        k = re.sub(u'\.', u'', k)
        k = re.sub(u'\n', u'', k)
        string += k + u' '
    return string

def extract_keywords(path):
    kw = ''
    f = codecs.open(path, 'r', 'cp1251')
    text = f.read()
    for term in term_extractor(text, limit = 15):
        kw += term.normalized + str(term.count) + u' '
#        print term.normalized, term.count
    return kw

main()


