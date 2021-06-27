<img src = 'https://github.com/khasaad/Natural_Language_Processing_for_sentiment_analysis/blob/main/images/logo.PNG'>

#### Key words: 
Deep Learning, NLP (Natural Language Processing), CamemBert,PyTorch, Neural Network, Python.

# Introduction:

We are going to analysis sentiments of comments from <a href = 'https://www.trustpilot.com/'>Trustpilot</a> page for french language using CamemBert model and PyTorch. 

## The project consists of three tasks:

1. The first one is to scrape the comments and reviews from Trustpilot page by each category (or all categories together). 

2. The second one is to preprocess, clean and prepare data for CamemBERT model.

3. The third one is a sentiment analysis task. Sentiment analysis, in this case, consists of classifying the opinion of a sentence whether it is positive or negative.

# How to use
<ol> 
 <li>clone the github repo:<br><code>git clone https://github.com/khasaad/Natural_Language_Processing_for_sentiment_analysis.git</code></li>
 <li>create a new virtual environment</li>
</ol>

### Scraping 
<ol>
 <li>pip install -r requirements.txt</li>
 <li><code>python scraping_comments_Trustpilot.py -c category_name -p number_of_pages </code></li>
 <p>Example: python scraping_comments_Trustpilot.py -c beauty_wellbeing -p 5</p>
 <p>The list of categories exist in dictionary_categories.txt</p>
</ol>

<p>After scraping, the data will be saved as the name of the selected category into dataframe (csv file), example: beauty_wellbeing.csv</p>

### Preprocess data

### Sentiment analysis
