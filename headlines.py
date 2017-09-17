import feedparser
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
 'cnn': 'http://rss.cnn.com/rss/edition.rss',
 'fox': 'http://feeds.foxnews.com/foxnews/latest',
 'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/", methods=['GET', 'POST'])
def get_news():
    query = request.form.get("publication") #change request.args.get to request.form.get to change between form param in POST and args params in GET
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc" #default publication is bbc
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html",
    articles=feed['entries'])

    # will be making query like http://localhost:5000/?publication=bbc


if __name__ == '__main__':
    app.run(port=5000, debug= True)