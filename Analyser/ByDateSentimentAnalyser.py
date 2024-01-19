from .ISentimentAnalyser import ISentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score
from dateutil import parser

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
                date = row['sitting_date']
                speech_text = row['text']
                sentiment_score = self.get_sentiment(speech_text)
                

                # calculate sentiment by date (year)
                if self.is_Valid_Date(date):
                    self.get_date_sentiment(date,sentiment_score)
     # checks whether the row is valid, by inspecting the id
    def is_Valid_Date(self,date):
        try:
            # Attempt to parse the date using datetime.strptime
            datetime.strptime(date, '%d %B %Y')
            return True
        except ValueError:
            return False
       
        
    def get_date_sentiment(self,date,sentiment_score):
        try:
            year = int(date.split()[-1])
            # modify date_dict dictionary
            if year not in self.date_dict:
                self.date_dict[year] = sentiment_score
            else:
                self.date_dict[year].total += sentiment_score.total
                self.date_dict[year].positive += sentiment_score.positive
                self.date_dict[year].negative += sentiment_score.negative
                self.date_dict[year].strong += sentiment_score.strong
                self.date_dict[year].weak += sentiment_score.weak
                self.date_dict[year].active += sentiment_score.active
                self.date_dict[year].passive += sentiment_score.passive
                self.date_dict[year].famine_terms += sentiment_score.famine_terms        
        except:
            print("date value Error")
     