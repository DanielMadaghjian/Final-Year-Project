from .Speech import Speech
from Sentiment_Objects.Sentiment_score import Sentiment_score

import csv
import re
from datetime import datetime
file_encoding = "utf-8"

class SentimentAnalyser:
    def __init__(self, sentiment_dict, famine_dict):
        self.sentiment_dict = sentiment_dict
        self.famine_dict = famine_dict
        self.speeches = []
        self.speakers_dict = {}
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
                speaker_name = row['member_name']
                date = row['sitting_date']
                speech_text = row['text']
                sentiment_score = self.get_sentiment(speech_text)
                
                # append speeches list
                if self.is_Valid_Row(id):
                    self.get_speaker_sentiment(id,speaker_name,date,sentiment_score)
                    
                    if date != "":
                        self.get_date_sentiment(date,sentiment_score)
       
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
       
       
     # checks whether the row is valid, by inspecting the id
    def is_Valid_Row(self,id):
        id_to_string = str(id)
        # Check if the length of the string is 32 and it is an alphanumeric string
        return len(id_to_string) == 32 and id_to_string.isalnum()   
       
    def get_speaker_sentiment(self, id, speaker_name, date, sentiment_score):
        speech = Speech(id, speaker_name, date, sentiment_score)
        self.speeches.append(speech)

        # modify speakers_dict dictionary
        if speaker_name not in self.speakers_dict:
            self.speakers_dict[speaker_name] = sentiment_score
        else:
            self.speakers_dict[speaker_name].total = self.speakers_dict[speaker_name].total + sentiment_score.total
            self.speakers_dict[speaker_name].positive = self.speakers_dict[speaker_name].positive + sentiment_score.positive
            self.speakers_dict[speaker_name].negative = self.speakers_dict[speaker_name].negative + sentiment_score.negative
            self.speakers_dict[speaker_name].strong = self.speakers_dict[speaker_name].strong + sentiment_score.strong
            self.speakers_dict[speaker_name].weak = self.speakers_dict[speaker_name].weak + sentiment_score.weak
            self.speakers_dict[speaker_name].active = self.speakers_dict[speaker_name].active + sentiment_score.active
            self.speakers_dict[speaker_name].passive = self.speakers_dict[speaker_name].passive + sentiment_score.passive
            self.speakers_dict[speaker_name].famine_terms = self.speakers_dict[speaker_name].famine_terms + sentiment_score.famine_terms
        
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
                 
     