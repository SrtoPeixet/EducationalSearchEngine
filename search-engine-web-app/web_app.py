import nltk
from flask import Flask, render_template
from flask import request

from app.analytics.analytics_data import AnalyticsData
from app.analytics.user import TrackedUser
from app.core import utils
from app.search_engine.search_engine import SearchEngine

app = Flask(__name__)

searchEngine = SearchEngine()
analytics_data = AnalyticsData()
tweets,corpus_terms = utils.load_documents_corpus()

tweet_results = []

# Set the corpus to the Search Engine
searchEngine.set_corpus(corpus_terms)

def track_user():
    ip_address = request.remote_addr
    requested_url = request.url
    referer_page = request.referrer
    page_name = request.path
    query_string = request.query_string
    user_agent = request.user_agent.string
    return TrackedUser(ip_address,requested_url,referer_page,page_name,query_string,user_agent)


@app.route('/')
def search_form():

    analytics_data.add_main_page_visit(track_user())
    print(track_user())

    return render_template('index.html', page_title="Welcome")


@app.route('/search', methods=['POST'])
def search_form_post():
    global tweet_results
    search_query = request.form['search-query']
    results_idx = searchEngine.search(search_query)
    tweet_results = utils.parse_results(tweets,results_idx)
    found_count = len(results_idx)

    return render_template('results.html', results_list=tweet_results, page_title="Results", found_counter=found_count)


@app.route('/doc_details', methods=['GET'])
def doc_details():
    # getting request parameters:
    # user = request.args.get('user')
    clicked_position = int(request.args["position"])
    analytics_data.page_visited(
        track_user(), tweet_results[clicked_position].id)
    

    return render_template('doc_details.html', tweet=tweet_results[clicked_position], position=clicked_position)


@app.route('/stats', methods=['GET'])
def stats():
    """
    Show simple statistics example. ### Replace with dashboard ###
    :return:
    """
    ### Start replace with your code ###
    try:
        pos = request.args["pos"]
    except:
        pos = False
    if pos:
        return render_template('stats_for_doc.html', analytics_data=analytics_data, tweet=tweet_results[int(pos)])
    return render_template('stats.html', analytics_data=analytics_data,utils=utils)
    ### End replace with your code ###

@app.route('/sentiment')
def sentiment_form():
    return render_template('sentiment.html')


@app.route('/sentiment', methods=['POST'])
def sentiment_form_post():
    text = request.form['text']
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text)))['compound'])
    return render_template('sentiment.html', score=score)

if __name__ == "__main__":
    app.run(port="8088", host="0.0.0.0", threaded=False, debug=True)
