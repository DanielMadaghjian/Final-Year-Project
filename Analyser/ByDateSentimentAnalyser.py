from .ISentimentAnalyser import ISentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score

import csv
import re
from datetime import datetime
file_encoding = "utf-8"

class ByDateSentimentAnalyser(ISentimentAnalyser):
    def __init__(self, sentiment_dict, famine_dict):
        super().__init__(sentiment_dict, famine_dict)
        self.speeches = []
        self.date_dict = {}
        
    # analyses sentiment of each speech
    def analyse_speeches(self,period_speeches_file_path):
        # open the speeches file
        with open(period_speeches_file_path, 'r', encoding=file_encoding) as file:
            csv_reader = csv.DictReader(file)
            rows = []
            for row in csv_reader:
                if row:
                    rows.append(row)
            # iterate through each row and analyse the speech text
            for row in rows:
                id = row['_id']
                date = row['sitting_date']
                speech_text = row['text']
                sentiment_score = self.get_sentiment(speech_text)
                
                # append speeches list
                if self.is_Valid_Row(id):
                    # calculate sentiment by date (year)
                    if date != "":
                        self.get_date_sentiment(date,sentiment_score)
     # checks whether the row is valid, by inspecting the id
    def is_Valid_Row(self,id):
        id_to_string = str(id)
        # Check if the length of the string is 32 and it is an alphanumeric string
        return len(id_to_string) == 32 and id_to_string.isalnum()   
       
        
    def get_date_sentiment(self,date,sentiment_score):
        date_object = datetime.strptime(date, '%b %d, %Y @ %H:%M:%S.%f')
        year = date_object.year
        # modify date_dict dictionary
        if year not in self.date_dict:
            self.date_dict[year] = sentiment_score
        else:
            self.date_dict[year].total = self.date_dict[year].total + sentiment_score.total
            self.date_dict[year].positive = self.date_dict[year].positive + sentiment_score.positive
            self.date_dict[year].negative = self.date_dict[year].negative + sentiment_score.negative
            self.date_dict[year].strong = self.date_dict[year].strong + sentiment_score.strong
            self.date_dict[year].weak = self.date_dict[year].weak + sentiment_score.weak
            self.date_dict[year].active = self.date_dict[year].active + sentiment_score.active
            self.date_dict[year].passive = self.date_dict[year].passive + sentiment_score.passive
            self.date_dict[year].famine_terms = self.date_dict[year].famine_terms + sentiment_score.famine_terms
                 
     