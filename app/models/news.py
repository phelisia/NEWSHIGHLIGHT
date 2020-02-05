class  News:
    '''
    News class to define News Objects
    '''

    def __init__(self,source_id,name,description,url):
        self.source_id = source_id
        self.name = name
        self.description = description
        self.url =url
class Articles:
    '''
    Articles class to define Articles objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author=author
        self.title= title
        self.description = description
        self.url =url
        self.urlToImage=urlToImage
        self.publishedAT=publishedAt
        self.content=content