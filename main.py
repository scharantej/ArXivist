
import os
import requests
from flask import Flask, render_template, request, jsonify


# create a Flask app
app = Flask(__name__)

# configure the app settings
app.config['SECRET_KEY'] = 'your_secret_key'


@app.route('/')
def index():
    """Render the search page."""
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    """Handle search requests."""
    # get the search query from the request
    query = request.form['query']

    # scrape the Arxiv website for matching papers
    papers = scrape_arxiv(query)

    # return the results of the search as JSON data
    return jsonify(papers)


@app.route('/results')
def results():
    """Render the search results page."""
    # get the search results from the request
    papers = request.json

    # render the results page with the search results
    return render_template('results.html', papers=papers)


def scrape_arxiv(query):
    """Scrape the Arxiv website for matching papers."""
    # construct the search URL
    url = 'https://arxiv.org/search/?query=' + query

    # make a GET request to the search URL
    response = requests.get(url)

    # parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all the paper results
    papers = soup.find_all('li', {'class': 'arxiv-result'})

    # extract the paper titles, abstracts, and links
    results = []
    for paper in papers:
        title = paper.find('p', {'class': 'title'}).text
        abstract = paper.find('p', {'class': 'abstract'}).text
        link = paper.find('a', {'class': 'title-link'})['href']

        results.append({
            'title': title,
            'abstract': abstract,
            'link': link
        })

    return results


if __name__ == '__main__':
    # run the app
    app.run(debug=True)
