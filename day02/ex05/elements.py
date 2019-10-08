from elem import Elem

class Html(Elem):
    def __init__(self,content,attr={}):
        super.__init__(tag="html",content=content,attr=attr)