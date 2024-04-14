from .IDictBuilder import IDictBuilder
import re
import csv
from Sentiment_Objects.Sentiment import Sentiment

class northAndSouthDictBuilder(IDictBuilder):
    # Counties in Northern Ireland
    northern_ireland_counties = ["ANTRIM", "ARMAGH", "DERRY", "DOWN", "FERMANAGH", "TYRONE"]
    # Counties in Southern Ireland (Republic of Ireland)
    southern_ireland_counties = ["CARLOW", "CORK", "CLARE", "DONEGAL", "DUBLIN", "GALWAY", "KERRY", "KILDARE", "KILKENNY", "LAOIS", "LEITRIM", "LIMERICK", "LONGFORD", "LOUTH", "MAYO", "MEATH", "MONAGHAN", "OFFALY", "ROSCOMMON", "SLIGO", "TIPPERARY", "WATERFORD", "WESTMEATH", "WEXFORD", "WICKLOW"]
    def __init__(self):
        self.northern_speakers = []
        self.southern_speakers = []
    
    def createDictionary(self, dictionary_file_path):
        print("Creating southern and northern lists....")
        
         
        with open(dictionary_file_path, 'r') as file:
            # Create a CSV reader
            csv_reader = csv.DictReader(file)
            rows = []
            for row in csv_reader:
                rows.append(row)
            # Iterate through each row in the CSV
            for row in rows:
                member_name = row['unique-name']
                converted_member_name = self.convert_Member_Name(member_name)
                constituency = row['constituencies-pipe-delimeted']
                constituency_location = self.get_First_Word(constituency)
                
                if constituency_location in self.northern_ireland_counties:
                    self.northern_speakers.append(converted_member_name)
                elif constituency_location in self.southern_ireland_counties:
                    self.southern_speakers.append(converted_member_name)
                    
    def convert_Member_Name(self, member_name):
        # Split the username into words using the hyphen as a delimiter
        words = member_name.split('-')

        # Capitalize each word and join them with a space
        formatted_name = ' '.join(word.capitalize() for word in words)
        return formatted_name.upper()
    
    def get_First_Word(self, text):
        # Split the text into words
        words = text.split()

        # Make the first word uppercase
        if words:
            first_word = words[0].upper()
            return first_word