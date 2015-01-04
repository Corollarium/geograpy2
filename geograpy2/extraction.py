import nltk
from newspaper import Article
from nltk.tag.stanford import POSTagger

class Extractor(object):
    """Extracts possible place names from text.

    Attributes:
      text (str or unicode): The text to parse. Unicode is accepted.
      url (list of str): The url to parse, if there is one.
      places (list): The list of possible place names found. 
    """

    def __init__(self, text=None, url=None):
        """Inits the parser.
        
        Args: 
            text (str or unicode): The text to parse. Unicode is accepted.
            url (str): Alternatively pass a url, which will be downloaded and
                stripped of HTML.
        """
        if not text and not url:
            raise Exception('text or url is required')

        self.text = text
        self.url = url
        self.places = []
        
        if self.url is not None:
            self.download_text()
    
    def download_text(self):
        """Downloads text from self.url and strip HTML tags.
        """
        if not self.text and self.url:
            a = Article(self.url)
            a.download()
            a.parse()
            self.text = a.text

    def named_entities(self):
        # word_tokenize should work well for most non-CJK languages
        text = nltk.word_tokenize(self.text)
        
        # TODO: this works only for english. Stanford's pos tagger supports
        # more languages
        # http://www.nltk.org/api/nltk.tag.html#module-nltk.tag.stanford
        # http://stackoverflow.com/questions/1639855/pos-tagging-in-german
        # PT corpus http://aelius.sourceforge.net/manual.html
        # 
        pos_tag = nltk.pos_tag(text)
        
        nes = nltk.ne_chunk(pos_tag)
        return nes
        

    def find_entities(self):
        """Parse text and tokenize it.
        """
        nes = self.named_entities()
        for ne in nes:
            if type(ne) is nltk.tree.Tree:
                if ne.label() in ['GPE', 'PERSON', 'ORGANIZATION']:
                    self.places.append(u' '.join([i[0] for i in ne.leaves()]))
