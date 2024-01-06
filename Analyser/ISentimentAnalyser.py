from abc import ABC, abstractmethod
from Sentiment_Objects.Sentiment_score import Sentiment_score
import re


class ISentimentAnalyser(ABC):
    def __init__(self, sentiment_dict, famine_dict):
        self.sentiment_dict = sentiment_dict
        self.famine_dict = famine_dict
        
    @abstractmethod
    def analyse_speeches(self, period_speeches_file_path):
        pass
    
     # returns the sentiment score of each speech        
    def get_sentiment(self,speech_text):
        words = re.findall(r'\b\w+\b', speech_text)
        sentiment_score = Sentiment_score(0,0,0,0,0,0,0,0)
        sentiment_score.total = len(words)
        index = 0
        # iterate through each word and find the sentiment
        for word in words:
            word_upper_case = word.upper()
            if word_upper_case in self.sentiment_dict:
                sentiment = self.sentiment_dict[word_upper_case]
                sentiment_score.positive = sentiment_score.positive  + 1 if sentiment.positive == "Positiv" else sentiment_score.positive
                sentiment_score.negative = sentiment_score.negative + 1 if sentiment.negative == "Negativ" else sentiment_score.negative
                sentiment_score.strong = sentiment_score.strong + 1 if sentiment.strong == "Strong" else sentiment_score.strong
                sentiment_score.weak = sentiment_score.weak + 1 if sentiment.weak == "Weak" else sentiment_score.weak
                sentiment_score.active = sentiment_score.active + 1 if sentiment.active == "Active" else sentiment_score.active
                sentiment_score.passive = sentiment_score.passive + 1 if sentiment.passive == "Passive" else sentiment_score.passive
                if word_upper_case in self.famine_dict:
                    sentiment_score.famine_terms = sentiment_score.famine_terms + 1
                # check for phrases in famine_dict
                elif word_upper_case == "FOOD":
                    if index < len(words) - 1:
                        next_word = words[index + 1]
                        phrase = word_upper_case + " " + next_word.upper()
                        if phrase in self.famine_dict:
                            sentiment_score.famine_terms = sentiment_score.famine_terms + 1
            index = index + 1
        return sentiment_score        