from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def language_analysis(text):
  document = types.Document(
      content=text,
      type=enums.Document.Type.PLAIN_TEXT)

  #print(document)

  # Detects the sentiment of the text
  sentiment = client.analyze_sentiment(document=document).document_sentiment

  print('Text: {}'.format(text))
  print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))



# Instantiates a client
client = language.LanguageServiceClient()
print(client)
# The text to analyze
text1 = u'You are beautiful'
text2 = u"you are so bad"

language_analysis(text1)
language_analysis(text2)


