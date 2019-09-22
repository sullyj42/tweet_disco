## This is the function file.

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def language_analysis(file_name):
  # open file "file_name". this file contains the database about twitter feeds
  # assuming the data is text 
  f = open(file_name, "r") 
  text=f.read()
  #print (text)
  document = types.Document(
      content=text,
      type=enums.Document.Type.PLAIN_TEXT)

  #print(document)

  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(document=document).document_sentiment

  #print('Text: {}'.format(text))
  #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

  return sentiment.score, sentiment.magnitude;

