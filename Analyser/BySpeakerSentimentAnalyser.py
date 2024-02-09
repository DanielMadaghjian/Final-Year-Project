from .ISentimentAnalyser import ISentimentAnalyser
from Sentiment_Objects.Sentiment_score import Sentiment_score
from .Speech import Speech

import csv
import re
file_encoding = "utf-8"

class BySpeakerSentimentAnalyser(ISentimentAnalyser):
    def __init__(self, sentiment_dict, northern_speakers, southern_speakers, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict):
        super().__init__(sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
        self.northern_speakers = northern_speakers
        self.southern_speakers = southern_speakers
        self.speeches = []
        self.speakers_dict = {}
        self.northern_speakers_dict = {}
        self.southern_speakers_dict = {}
        
         
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
                if self.is_Valid_Member(speaker_name):
                    self.get_speaker_sentiment(id,speaker_name,date,sentiment_score)
                    id = id + 1
     # checks whether the row is valid, by inspecting the id
    def is_Valid_Row(self,id):
        id_to_string = str(id)
        # Check if the length of the string is 32 and it is an alphanumeric string
        return len(id_to_string) == 32 and id_to_string.isalnum()   
       
    def is_Valid_Member(self, speaker_name):
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
            self.update_dict(self.speakers_dict,speaker_name, sentiment_score)
        # modify northern_speakers_dictionary
        if speaker_name not in self.northern_speakers_dict and self.check_northern_speaker(speaker_name):
            self.northern_speakers_dict[speaker_name] = sentiment_score
        elif speaker_name in self.northern_speakers_dict:
            self.update_dict(self.northern_speakers_dict, speaker_name, sentiment_score)
        # modify southern_speakers_dictionary
        if speaker_name not in self.southern_speakers_dict and self.check_southern_speaker(speaker_name):
            self.southern_speakers_dict[speaker_name] = sentiment_score
        elif speaker_name in self.southern_speakers_dict:
            self.update_dict(self.southern_speakers_dict,speaker_name, sentiment_score)
            
            
    def update_dict(self, dict, speaker_name, sentiment_score):
        dict[speaker_name].total = self.speakers_dict[speaker_name].total + sentiment_score.total
        dict[speaker_name].positive = self.speakers_dict[speaker_name].positive + sentiment_score.positive
        dict[speaker_name].negative = self.speakers_dict[speaker_name].negative + sentiment_score.negative
        dict[speaker_name].strong = self.speakers_dict[speaker_name].strong + sentiment_score.strong
        dict[speaker_name].weak = self.speakers_dict[speaker_name].weak + sentiment_score.weak
        dict[speaker_name].active = self.speakers_dict[speaker_name].active + sentiment_score.active
        dict[speaker_name].passive = self.speakers_dict[speaker_name].passive + sentiment_score.passive
        dict[speaker_name].famine_terms = self.speakers_dict[speaker_name].famine_terms + sentiment_score.famine_terms
        dict[speaker_name].grains_terms = self.speakers_dict[speaker_name].grains_terms + sentiment_score.grains_terms
        dict[speaker_name].processed_grains_terms = self.speakers_dict[speaker_name].processed_grains_terms + sentiment_score.processed_grains_terms
        dict[speaker_name].livestock_terms = self.speakers_dict[speaker_name].livestock_terms + sentiment_score.livestock_terms
        dict[speaker_name].potatoes_terms = self.speakers_dict[speaker_name].potatoes_terms + sentiment_score.potatoes_terms
        dict[speaker_name].hay_terms = self.speakers_dict[speaker_name].hay_terms + sentiment_score.hay_terms
            
    # def update_speakers_dict(self, speaker_name, sentiment_score):
    #     self.speakers_dict[speaker_name].total = self.speakers_dict[speaker_name].total + sentiment_score.total
    #     self.speakers_dict[speaker_name].positive = self.speakers_dict[speaker_name].positive + sentiment_score.positive
    #     self.speakers_dict[speaker_name].negative = self.speakers_dict[speaker_name].negative + sentiment_score.negative
    #     self.speakers_dict[speaker_name].strong = self.speakers_dict[speaker_name].strong + sentiment_score.strong
    #     self.speakers_dict[speaker_name].weak = self.speakers_dict[speaker_name].weak + sentiment_score.weak
    #     self.speakers_dict[speaker_name].active = self.speakers_dict[speaker_name].active + sentiment_score.active
    #     self.speakers_dict[speaker_name].passive = self.speakers_dict[speaker_name].passive + sentiment_score.passive
    #     self.speakers_dict[speaker_name].famine_terms = self.speakers_dict[speaker_name].famine_terms + sentiment_score.famine_terms
    #     self.speakers_dict[speaker_name].grains_terms = self.speakers_dict[speaker_name].grains_terms + sentiment_score.grains_terms
    #     self.speakers_dict[speaker_name].processed_grains_terms = self.speakers_dict[speaker_name].processed_grains_terms + sentiment_score.processed_grains_terms
    #     self.speakers_dict[speaker_name].livestock_terms = self.speakers_dict[speaker_name].livestock_terms + sentiment_score.livestock_terms
    #     self.speakers_dict[speaker_name].potatoes_terms = self.speakers_dict[speaker_name].potatoes_terms + sentiment_score.potatoes_terms
    #     self.speakers_dict[speaker_name].hay_terms = self.speakers_dict[speaker_name].hay_terms + sentiment_score.hay_terms
    # def update_northern_speakers_dict(self, speaker_name, sentiment_score):
    #     self.northern_speakers_dict[speaker_name].total = self.speakers_dict[speaker_name].total + sentiment_score.total
    #     self.northern_speakers_dict[speaker_name].positive = self.speakers_dict[speaker_name].positive + sentiment_score.positive
    #     self.northern_speakers_dict[speaker_name].negative = self.speakers_dict[speaker_name].negative + sentiment_score.negative
    #     self.northern_speakers_dict[speaker_name].strong = self.speakers_dict[speaker_name].strong + sentiment_score.strong
    #     self.northern_speakers_dict[speaker_name].weak = self.speakers_dict[speaker_name].weak + sentiment_score.weak
    #     self.northern_speakers_dict[speaker_name].active = self.speakers_dict[speaker_name].active + sentiment_score.active
    #     self.northern_speakers_dict[speaker_name].passive = self.speakers_dict[speaker_name].passive + sentiment_score.passive
    #     self.northern_speakers_dict[speaker_name].famine_terms = self.speakers_dict[speaker_name].famine_terms + sentiment_score.famine_terms
    #     self.northern_speakers_dict[speaker_name].grains_terms = self.speakers_dict[speaker_name].grains_terms + sentiment_score.grains_terms
    #     self.northern_speakers_dict[speaker_name].processed_grains_terms = self.speakers_dict[speaker_name].processed_grains_terms + sentiment_score.processed_grains_terms
    #     self.northern_speakers_dict[speaker_name].livestock_terms = self.speakers_dict[speaker_name].livestock_terms + sentiment_score.livestock_terms
    #     self.northern_speakers_dict[speaker_name].potatoes_terms = self.speakers_dict[speaker_name].potatoes_terms + sentiment_score.potatoes_terms
    #     self.northern_speakers_dict[speaker_name].hay_terms = self.speakers_dict[speaker_name].hay_terms + sentiment_score.hay_terms
    # def update_southern_speakers_dict(self, speaker_name, sentiment_score):
    #     self.southern_speakers_dict[speaker_name].total = self.speakers_dict[speaker_name].total + sentiment_score.total
    #     self.southern_speakers_dict[speaker_name].positive = self.speakers_dict[speaker_name].positive + sentiment_score.positive
    #     self.southern_speakers_dict[speaker_name].negative = self.speakers_dict[speaker_name].negative + sentiment_score.negative
    #     self.southern_speakers_dict[speaker_name].strong = self.speakers_dict[speaker_name].strong + sentiment_score.strong
    #     self.southern_speakers_dict[speaker_name].weak = self.speakers_dict[speaker_name].weak + sentiment_score.weak
    #     self.southern_speakers_dict[speaker_name].active = self.speakers_dict[speaker_name].active + sentiment_score.active
    #     self.southern_speakers_dict[speaker_name].passive = self.speakers_dict[speaker_name].passive + sentiment_score.passive
    #     self.southern_speakers_dict[speaker_name].famine_terms = self.speakers_dict[speaker_name].famine_terms + sentiment_score.famine_terms
    #     self.southern_speakers_dict[speaker_name].grains_terms = self.speakers_dict[speaker_name].grains_terms + sentiment_score.grains_terms
    #     self.southern_speakers_dict[speaker_name].processed_grains_terms = self.speakers_dict[speaker_name].processed_grains_terms + sentiment_score.processed_grains_terms
    #     self.southern_speakers_dict[speaker_name].livestock_terms = self.speakers_dict[speaker_name].livestock_terms + sentiment_score.livestock_terms
    #     self.southern_speakers_dict[speaker_name].potatoes_terms = self.speakers_dict[speaker_name].potatoes_terms + sentiment_score.potatoes_terms
    #     self.southern_speakers_dict[speaker_name].hay_terms = self.speakers_dict[speaker_name].hay_terms + sentiment_score.hay_terms
    
    def check_northern_speaker(self, speaker_name):
        if speaker_name.upper() in self.northern_speakers:
            return True
        return False
    
    def check_southern_speaker(self, speaker_name):
        if speaker_name.upper() in self.southern_speakers:
            return True
        return False
    