
from Sentiment_Objects.Sentiment import Sentiment
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score
from datetime import datetime

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
    sentiment_score = Sentiment_score(10,2,1,3,0,2,1,0)
    date = "Dec 28, 1852 @ 23:34:39.000"
    
    analyser = ByDateSentimentAnalyser(sentiment_dict, famine_dict)
    analyser.get_date_sentiment(date, sentiment_score)
    
    date_object = datetime.strptime(date, '%b %d, %Y @ %H:%M:%S.%f')
    year = date_object.year
    # check results of date_dict
    assert year in analyser.date_dict
    assert analyser.date_dict[year].total == 10
    assert analyser.date_dict[year].positive == 2
    assert analyser.date_dict[year].negative == 1
    assert analyser.date_dict[year].strong == 3
    assert analyser.date_dict[year].weak == 0
    assert analyser.date_dict[year].active == 2
    assert analyser.date_dict[year].passive == 1
    assert analyser.date_dict[year].famine_terms == 0
    