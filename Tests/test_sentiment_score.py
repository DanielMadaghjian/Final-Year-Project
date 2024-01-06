
from Sentiment_Objects.Sentiment import Sentiment
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser

def test_bydate_sentiment_analyser():
    sentiment_dict = {
            'GOOD': Sentiment("Positiv", " ", "Strong", " ", "Active", " "),
            'BAD': Sentiment(" ", "Negativ", "Strong", " ", " ", "Passive"),
    }
    famine_dict = {
        'famine': 0,
        'hunger': 0,
        'starvation': 0,
        'death': 0,
        'scarcity': 0,
        'food shortage': 0,
        'food crisis': 0,
        'food scarcity': 0
    }
    
    speech_text = "This is a good example. Bad example is not GOOD."
    sentiment_analyser = ByDateSentimentAnalyser(sentiment_dict, famine_dict)
    sentiment_score = sentiment_analyser.get_sentiment(speech_text)
    
    assert sentiment_score.total == 10
    assert sentiment_score.positive == 2
    assert sentiment_score.negative == 1
    assert sentiment_score.strong == 3
    assert sentiment_score.weak == 0
    assert sentiment_score.active == 2
    assert sentiment_score.passive == 1