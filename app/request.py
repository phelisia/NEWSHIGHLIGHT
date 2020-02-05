from app import app
import urllib.request,json
from . models import news
News = news.News
Articles =news.Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLES_API_BASE_URL"]
def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

            print(news_results)

    return news_results
def process_results(news_results_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_results_list:
        source_id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        

        if name:
            news_object = News(source_id,name,description,url)
            news_results.append(news_object)

    return news_results

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_base_url.format(source, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        # get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results
def process_articles(articles_results_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    articles_results = []
    for articles_item in articles_results_list:
        author = articles_item.get('author')
        description = articles_item.get('description')
        title = articles_item.get('title')
        image= articles_item.get('url')
        urlToImage= articles_item.get('urlToImage')
        publishedAt=articles_item.get('publishedAt')
        content = articles_item.get('content')
        

        if news:
            articles_object = Articles(author,title,description,image,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results
