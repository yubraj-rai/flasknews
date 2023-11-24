Flask News Web Application

This is a simple Flask web application that fetches news data from the NewsAPI and displays it on the web page. The application has different routes for displaying news from different sources such as Al Jazeera and BBC.

Prerequisites

    Python (3.x recommended)
    Flask
    NewsAPI Key (Get your API key here)

Installation

    Clone the repository: git clone git@github.com:yubraj-rai/flask_news_app.git

Navigate to the project directory:

    cd flask-news-app

Install dependencies using pip:

    pip install -r requirements.txt
    

Configuration

    Get your NewsAPI Key: https://newsapi.org/

    Open app.py in a text editor and replace "NEWS_API_KEY" with your actual NewsAPI key.

    NEWS_API_KEY = "e106576396b845e2a46cf6705a8dfe73"
    newsapi = NewsApiClient(api_key="YOUR-NEWSAPI-KEY")

Usage

    Run the Flask application:
    
    python app.py
    Example: /bin/python3 "/app_path/FlaskNewsApplication/app.py"
    

    Open your web browser and go to http://localhost:5000/ to view the home page.

    Explore different routes:
        http://localhost:5000/bbc for BBC news.
        http://localhost:5000/aljazeera for Al Jazeera news.

API Endpoints

You can also access the news data as JSON through API endpoints:

    http://localhost:5000/api/bbc for BBC news API.
    http://localhost:5000/api/aljazeera for Al Jazeera news API.

Contributing

Feel free to contribute to this project. Create issues, fork the repository, and submit pull requests.

License

This project is not licensed.

Deployment
https://flasknews.onrender.com
