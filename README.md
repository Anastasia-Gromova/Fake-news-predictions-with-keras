## Fake news predictions with Keras

The dataset "Fake News" of the fake news was taken from the Kaggle competition https://www.kaggle.com/c/fake-news. File contains the title of article, it's author, the text and the labels if the article is true ('0') or potentially fake('1').
</br>In this repository there will be shown the examples of text vectorization and training the model using the text data.

### Fake news dataset vectorization

This example of text vectorization given in the file 'fake_news_vectorization.py' requires the spaCy python package and the English multi-task CNN provided by it, which can be obtained with the following terminal commands:

```
pip install spacy
python -m spacy download en_core_web_md
```

The dataset contains three columns with text data which should be converted to a numerical data for the further training. In the code for each column and each row is converted to 300 vectors and later adds these vectors to new 300 columns. The vectorized dataset which will be saved in a file contains in total 906 columns including the old ones.
</br>
</br> The example of the first 5 rows:

![alt tag](vectorized_dataset_table.jpg)

### Fake news dataset training

The following code 'fake_news_training.py' requires Numpy, Pandas and Keras packages.
</br>This example shows the simple keras model for the vectorized dataset predictions. The dataset is automatically separated on the training and validation parts (33% of the dataset). The following output shows that the result for testing is around 0.97, which means that 97% of the predictions were correct. The binary output is approximately evenly distributed, which means that simple accuracy can precisely describe the performance of the model.
</br>
</br>The output of the code:
```
Train on 10970 samples, validate on 7314 samples
Epoch 1/5
 - 3s - loss: 0.0285 - acc: 0.9201 - val_loss: 0.0149 - val_acc: 0.9561
Epoch 2/5
 - 1s - loss: 0.0119 - acc: 0.9661 - val_loss: 0.0113 - val_acc: 0.9669
Epoch 3/5
 - 1s - loss: 0.0099 - acc: 0.9723 - val_loss: 0.0144 - val_acc: 0.9601
Epoch 4/5
 - 2s - loss: 0.0083 - acc: 0.9777 - val_loss: 0.0123 - val_acc: 0.9660
Epoch 5/5
 - 1s - loss: 0.0079 - acc: 0.9786 - val_loss: 0.0093 - val_acc: 0.9743
```
