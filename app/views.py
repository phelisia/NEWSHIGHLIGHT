from flask import render_template
from app import app
from .request import get_news, get_articles
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    news = get_news()
    title = 'Home - News highlight'
    return render_template('index.html', title = title, sources = news )

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    articles = get_articles(news_id)
    return render_template('news.html',source_articles = articles)