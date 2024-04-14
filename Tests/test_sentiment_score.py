
from Sentiment_Objects.Sentiment import Sentiment
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser

import unittest

def test_bydate_sentiment_analyser():
    sentiment_dict = {
            'GOOD': Sentiment("Positiv", " ", "Strong", " ", "Active", " "),
            'BAD': Sentiment(" ", "Negativ", "Strong", " ", " ", "Passive"),
    }
    famine_dict = [
        'FAMINE',
        'HUNGER',
        'STARVATION',
        'DEATH',
        'SCARCITY',
        'FOOD SHORTAGE',
        'FOOD CRISIS',
        'MALNUTRITION',
        'POVERTY',
        'DROUGHT',
        'CROP FAILURE',
        'FAMINE-STRICKEN',
        'RATIONS',
        'STARVING',
        'EXTREME HUNGER',
        'WIDESPREAD HUNGER',
        'FAILED HARVEST'
    ]
    grains_dict = [
    'WHEAT', 'WHEAT-BARLEY', 'WHEAT-GRAIN','CEREAL', 'DURUM', 'GRAIN', 'TRITICUM', 'BRAN', 'CORN',
    'OATS', 'AVENA SATIVA',
    'BARLEY', 'BARLEY-CORN', 'BARLEY-HARVEST', 'BARLEYCORN',
    ]
    processed_grains_dict = [
        'FLOUR', 'BARLEY-FLOUR', 'FLOUR-BREAD', 'WHEAT-FLOUR', 'dough', 'pastry',
        'OATMEAL', 'PORRIDGE', 'BURGOO',
    ]
    livestock_dict = [
        'MUTTON',
        'BEEF', 'BOEUF',
        'BACON', 'BACON-PIG', 'PANCETTA', 'FLITCH',
        'BUTTER',
        'MEAT'
    ]
    potatoes_dict = [
        'POTATOES',
        'YAM',
        'SPUD'
        'VEGETABLE'
        
    ]
    hay_dict = [
        'HAY','BOG-HAY','TIMOTHY' # Grass grown for Hay
    ]
    
    speech_text = "This is a good example. Bad example is not GOOD. grain, famine, flour, bacon-pig, potatoes, hay ."
    sentiment_analyser = ByDateSentimentAnalyser(sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
    sentiment_score = sentiment_analyser.get_sentiment(speech_text)
    
    # assert sentiment_score.total == 16
    # assert sentiment_score.positive == 2
    # assert sentiment_score.negative == 1
    # assert sentiment_score.strong == 3
    # assert sentiment_score.weak == 0
    # assert sentiment_score.active == 2
    # assert sentiment_score.passive == 1
    # assert sentiment_score.famine_terms == 1
    assert sentiment_score.grains_terms == 1
    assert sentiment_score.processed_grains_terms == 1
    assert sentiment_score.livestock_terms == 1
    assert sentiment_score.potatoes_terms == 1
    assert sentiment_score.hay_terms == 1