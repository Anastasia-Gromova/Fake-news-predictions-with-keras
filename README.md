## Fake news predictions with Keras

The dataset "Fake News" of the fake news was taken from the Kaggle competition https://www.kaggle.com/c/fake-news. File contains the title of article, it's author, the text and the labels if the article is true ('0') or potentially fake('1').
</br>In this repository there will be shown the examples of text vectorization and training the model using the text data.

### Fake news dataset vectorization

This example of text vectorization given in the file 'fake_news_vectorization.py' requires the spaCy python package and the English multi-task CNN provided by it, which can be obtained with the following terminal commands:

```
pip install spacy
```
```
python -m spacy download en_core_web_md
```

The dataset contains three columns with text data which should be converted to a numerical data for the further training. 
