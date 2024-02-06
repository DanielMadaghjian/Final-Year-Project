from .ISentimentAnalyser import ISentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score
from dateutil import parser
from .YearMonth import YearMonth

import csv
import re
from datetime import datetime
file_encoding = "utf-8"

MONTH_MAPPING = {
    'January': 2, 'February': 2, 'March': 4, 'April': 4, 'May': 6, 'June': 6,
    'July': 8, 'August': 8, 'September': 10, 'October': 10, 'November': 12, 'December': 12
}

class ByDateSentimentAnalyser(ISentimentAnalyser):
    def __init__(self, sentiment_dict, famine_dict):
        super().__init__(sentiment_dict, famine_dict)
        self.speeches = []
        self.bimonthly_date_dict = {}
        self.yearly_date_dict = {}
        
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
                speaker_name = row['membername']

                # calculate sentiment by date (year)
                if self.is_Valid_Date(date) and self.is_Valid_Member(speaker_name):
                    self.get_yearly_date_sentiment(date, sentiment_score)
                    self.get_bimonthly_date_sentiment(date,sentiment_score)
     # checks whether the row is valid, by inspecting the id
    def is_Valid_Date(self,date):
        try:
            # Attempt to parse the date using datetime.strptime
            datetime.strptime(date, '%d %B %Y')
            return True
        except ValueError:
            return False
        
    def is_Valid_Member(self, speaker_name):
        if speaker_name and speaker_name[0].isupper():
            return True
        else:
            return False
        
    def get_yearly_date_sentiment(self,date, sentiment_score):
        try:
            # Parse the date string into a datetime object
            dt_object = datetime.strptime(date, '%d %B %Y')
            
            # Extract year and month from the datetime object
            year = dt_object.year

            # modify date_dict dictionary
            if year not in self.yearly_date_dict:
                self.yearly_date_dict[year] = sentiment_score
            else:
                # Update sentiment scores for existing key
                existing_score = self.yearly_date_dict[year]
                existing_score.total += sentiment_score.total
                existing_score.positive += sentiment_score.positive
                existing_score.negative += sentiment_score.negative
                existing_score.strong += sentiment_score.strong
                existing_score.weak += sentiment_score.weak
                existing_score.active += sentiment_score.active
                existing_score.passive += sentiment_score.passive
                existing_score.famine_terms += sentiment_score.famine_terms       
        except:
            print("yearly date value Error")   
        
    def get_bimonthly_date_sentiment(self,date,sentiment_score):
        try:
            # Parse the date string into a datetime object
            dt_object = datetime.strptime(date, '%d %B %Y')
            
            # Extract year and month from the datetime object
            year = dt_object.year
            month_name = dt_object.strftime('%B')
            month = MONTH_MAPPING.get(month_name)
            key = YearMonth(year, month)
            # modify date_dict dictionary
            if key not in self.bimonthly_date_dict:
                self.bimonthly_date_dict[key] = sentiment_score
            else:
                # Update sentiment scores for existing key
                existing_score = self.bimonthly_date_dict[key]
                existing_score.total += sentiment_score.total
                existing_score.positive += sentiment_score.positive
                existing_score.negative += sentiment_score.negative
                existing_score.strong += sentiment_score.strong
                existing_score.weak += sentiment_score.weak
                existing_score.active += sentiment_score.active
                existing_score.passive += sentiment_score.passive
                existing_score.famine_terms += sentiment_score.famine_terms       
        except:
            print("bimonthly date value Error")
            
   
        
     