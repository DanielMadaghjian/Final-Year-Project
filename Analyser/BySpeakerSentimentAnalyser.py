from .ISentimentAnalyser import ISentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score
from .Speech import Speech

import csv
import re
file_encoding = "utf-8"

class BySpeakerSentimentAnalyser(ISentimentAnalyser):
    def __init__(self, sentiment_dict, famine_dict):
        super().__init__(sentiment_dict, famine_dict)
        self.speeches = []
        self.speakers_dict = {}
        
         
    # analyses sentiment of each speech
    def analyse_speeches(self,period_speeches_file_path):
        # open the speeches file
        with open(period_speeches_file_path, 'r', encoding=file_encoding) as file:
            csv_reader = csv.DictReader(file)
            rows = []
            for row in csv_reader:
                if row:
                    rows.append(row)
            id = 0
            # iterate through each row and analyse the speech text
            for row in rows:
                speaker_name = row['membername']
                date = row['sitting_date']
                speech_text = row['text']
                sentiment_score = self.get_sentiment(speech_text)
                
                # append speeches list
                # if self.is_Valid_Row(id):
                #     # calculate sentiment by speaker
                #     self.get_speaker_sentiment(id,speaker_name,date,sentiment_score)
                # calculate sentiment by speaker
                if self.is_Valid_Row(speaker_name):
                    self.get_speaker_sentiment(id,speaker_name,date,sentiment_score)
                    id = id + 1
     # checks whether the row is valid, by inspecting the speaker name
    def is_Valid_Row(self,speaker_name):
        if speaker_name and speaker_name[0].isupper():
            return True
        else:
            return False
          
       
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