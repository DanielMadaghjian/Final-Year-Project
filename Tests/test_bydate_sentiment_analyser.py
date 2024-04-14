
from Sentiment_Objects.Sentiment import Sentiment
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser
from Analyser.YearMonth import YearMonth
from Sentiment_Objects.Sentiment_score import Sentiment_score
from datetime import datetime
import unittest

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

def test_byYearly_sentiment_analyser():
    sentiment_score1 = Sentiment_score(10,2,1,3,0,2,1,0,1,2,1,0,3)
    sentiment_score2 = Sentiment_score(5,2,1,3,0,2,1,0,1,2,1,0,3)
    sentiment_score3 = Sentiment_score(20,2,1,3,0,2,1,0,1,2,1,0,3)
    date1 = '19 December 1852'
    date2 = '19 September 1852'
    date3 = '19 March 1851'

    analyser = ByDateSentimentAnalyser(sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
    # analyse yearly sentiment
    analyser.get_yearly_date_sentiment(date1, sentiment_score1)
    analyser.get_yearly_date_sentiment(date2,sentiment_score2)
    analyser.get_yearly_date_sentiment(date3,sentiment_score3)
    year = 1852
    assert year in analyser.yearly_date_dict
    assert analyser.yearly_date_dict[year].total == 15
    assert analyser.yearly_date_dict[year].positive == 4
    assert analyser.yearly_date_dict[year].negative == 2
    assert analyser.yearly_date_dict[year].strong == 6
    assert analyser.yearly_date_dict[year].weak == 0
    assert analyser.yearly_date_dict[year].active == 4
    assert analyser.yearly_date_dict[year].passive == 2
    assert analyser.yearly_date_dict[year].famine_terms == 0
    assert analyser.yearly_date_dict[year].grains_terms == 2
    assert analyser.yearly_date_dict[year].processed_grains_terms == 4
    assert analyser.yearly_date_dict[year].livestock_terms == 2
    assert analyser.yearly_date_dict[year].potatoes_terms == 0
    assert analyser.yearly_date_dict[year].hay_terms == 6
    year = 1851
    assert year in analyser.yearly_date_dict
    assert analyser.yearly_date_dict[year].total == 20
    
def test_byBiMonthly_sentiment_analyser():
    sentiment_score1 = Sentiment_score(10,2,1,3,0,2,1,0,1,2,1,0,3)
    sentiment_score2 = Sentiment_score(5,2,1,3,0,2,1,0,1,2,1,0,3)
    sentiment_score3 = Sentiment_score(20,2,1,3,0,2,1,0,1,2,1,0,3)
    date1 = '19 December 1852'
    date2 = '19 September 1852'
    date3 = '28 November 1852'
    analyser = ByDateSentimentAnalyser(sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
    # analyse bimonthly sentiment
    analyser.get_bimonthly_date_sentiment(date1, sentiment_score1)
    analyser.get_bimonthly_date_sentiment(date2, sentiment_score2)
    analyser.get_bimonthly_date_sentiment(date3, sentiment_score3)
    key1 = YearMonth(1852, 12)
    key2 = YearMonth(1852, 10)
    assert key1 in analyser.bimonthly_date_dict
    assert analyser.bimonthly_date_dict[key1].total == 30
    assert key2 in analyser.bimonthly_date_dict
    assert analyser.bimonthly_date_dict[key1].total == 5
    