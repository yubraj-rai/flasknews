from flask import Flask, render_template, jsonify, request
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
@app.route('/aljazeera')
@app.route('/bbc')
def aljazeera():
    source = "al-jazeera-english" if request.path == "/aljazeera" else "bbc-news"
    
    newsapi = NewsApiClient(api_key="e106576396b845e2a46cf6705a8dfe73")
    topheadlines = newsapi.get_top_headlines(sources=source)

    articles = topheadlines['articles']

    news_data = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news_data.append({
            'title': myarticles['title'],
            'description': myarticles['description'],
            'urlToImage': myarticles['urlToImage']
        })

    return render_template('index.html', context=news_data)

@app.route('/api/aljazeera')
@app.route('/api/bbc')
def aljazeera_api():
    source = "al-jazeera-english" if request.path == "/api/aljazeera" else "bbc-news"
    
    newsapi = NewsApiClient(api_key="e106576396b845e2a46cf6705a8dfe73")
    topheadlines = newsapi.get_top_headlines(sources=source)

    articles = topheadlines['articles']

    news_data = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news_data.append({
            'title': myarticles['title'],
            'description': myarticles['description'],
            'urlToImage': myarticles['urlToImage']
        })

    return jsonify(news_data)

if __name__ == "__main__":
    app.run(debug=False)
