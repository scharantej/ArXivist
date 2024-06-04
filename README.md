## Flask Application Design for Scraping Arxiv Papers on Superconductors

### HTML Files

- `index.html`:
  - Responsible for displaying the search page and displaying the search results.
  - Contains a form for entering a search query and a button to submit the search.
  - Includes a section to display the search results, which will be populated dynamically using JavaScript.

- `results.html`:
  - Used to display the results of a search query.
  - Will contain a list of the papers that match the search query, along with their titles, abstracts, and links to the full papers.

### Routes

- `/`:
  - Route for the search page.
  - Will render the `index.html` file and display the search page.

- `/search`:
  - Route for handling search requests.
  - Will take a search query as a parameter and use it to scrape the Arxiv website for matching papers.
  - Will return the results of the search as JSON data.

- `/results`:
  - Route for displaying search results.
  - Will render the `results.html` file and display the list of matching papers.