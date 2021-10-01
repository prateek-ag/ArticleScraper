from bs4 import BeautifulSoup
from bs4.element import Comment
from googlesearch import search
import nltk
import re
from urllib2 import urlopen
from threading import Thread


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def timeout():
    raise Exception('Something is taking Too long')

def get_full_quote(quote):
    toReturn = re.sub("[\[].*?[\]] ", "", quote)
    for j in search('"' + quote + '"', num=10, stop=10):
        print(j)
        try:
            result = { 'success': False, 'value': None }
            def _task(result):
                try                  : result['value'] = urlopen(j)
                except Exception as e: result['value'] = e
                else                 : result['success'] = True
            t = Thread(target=_task, args=(result,))
            t.start()
            t.join(15)
            html = result['value']
            html.read()
            
        except Exception as e:
            print(e)
            print("Can't open URL")

        else:
            alltext = text_from_html(html)
            charmap = {0x201c: u'"',
                       0x201d: u'"',
                       0x2018: u"'",
                       0x2019: u"'"}

            alltext = alltext.translate(charmap)
            final = re.findall(r'"([^"]*)"', alltext)
            splitFinal = [n for s in final for n in nltk.tokenize.sent_tokenize(s)]

            match = [s for s in splitFinal if quote in s]
            if match:
                if match[0].endswith(('?', '!', '.', ',')) and match[0][0].isupper():
                    toReturn = match[0]
                    break
                elif len(match[0]) > len(quote):
                    toReturn = match[0]
    return toReturn
