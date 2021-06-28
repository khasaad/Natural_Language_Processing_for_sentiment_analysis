<img src = 'https://github.com/khasaad/Natural_Language_Processing_for_sentiment_analysis/blob/main/images/logo.PNG'>

#### Key words: 
Deep Learning, NLP (Natural Language Processing), CamemBert, PyTorch, Neural Network, Python.

# Introduction:

We are going to analysis sentiments of comments from <a href = 'https://www.trustpilot.com/'>Trustpilot</a> page for french language using CamemBert model and PyTorch. 

## The project consists of three tasks:

1. The first one is to scrape the comments and reviews from Trustpilot page by each category (or all categories together). 

2. The second one is to preprocess, clean and prepare data for CamemBERT model.

3. The third one is a sentiment analysis task. Sentiment analysis, in this case, consists of classifying the opinion of a sentence whether it is positive or negative.

# How to use
<ul> 
 <li>clone the github repo:<br><code>git clone https://github.com/khasaad/Natural_Language_Processing_for_sentiment_analysis.git</code></li>
 <li>create a new virtual environment</li>
</ul>

### Scraping 
<ul>
 <li><code>pip install -r requirements_scraping.txt</code></li>
 <li><code>python scraping_comments_Trustpilot.py -c category_name -p number_of_pages </code></li>
 <p>Example: python scraping_comments_Trustpilot.py -c beauty_wellbeing -p 5</p>
 <p>The list of categories exist in dictionary_categories.txt</p>
</ul>

<p>After scraping, the data will be saved as the name of the selected category into dataframe (csv file), example: beauty_wellbeing.csv</p>

### Preprocess data
<ul>
 <li><code>pip install -r requirements_clean_Data.txt</code></li>
 
 <p>Using data_engineering.ipynb to clean the dataframe after scraping to prepare it for train model.
Add dataframe name which you got it after scraping in the jupyter notebook data_engineering, you will get new dataframe with cleaned data.</p>
 <p>Example: add dataframe_name = 'beauty_wellbeing.csv', you will get 'cleaned_beauty_wellbeing.csv'</p> 
</ul>

### Sentiment analysis using CamemBERT model

<p>CamemBERT model is French Language Model and trained on 138GB of French text. </p>
<p>Using Natural_Language_Processing_for_sentiment_analysis.ipynb to train your model using cleaned dataframe, then you can save the model and test it with set of comments.</p>

<p>There are a huge disparity between positive and negative comments, so SMOTE has been used for unbalanced data and neutral comments were excluded.<p>
 
 <img src='https://github.com/khasaad/Natural_Language_Processing_for_sentiment_analysis/blob/main/images/sentiment.PNG'>
 
 # Test trained model
 <ul>
  <li><code>Download <a href= 'https://drive.google.com/file/d/1FYesHGFMQR6TM1vF3l79UpbONcYCbmCE/view?usp=sharing'>sentiments_model_trained.pt</a> from Drive and load it in test_model.ipynb</code></li>
 </ul>
  
 <p>After you have trained the model, you can test it with a new different set of comments. </p>
 <p>Before that, use data_engineering.ipynb to clean data, then use test_model.ipynb to test your model. (There are a ready dataframe for testing 'comments_for_test.csv')</p>
 
