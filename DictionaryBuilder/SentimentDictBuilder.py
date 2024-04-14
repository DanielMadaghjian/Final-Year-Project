from .IDictBuilder import IDictBuilder
import re
import csv
from Sentiment_Objects.Sentiment import Sentiment

class SentimentDictBuilder(IDictBuilder):
    def __init__(self):
        self.sentiment_dict = {}
    
    def createDictionary(self, dictionary_file_path):
        print("Creating sentiment dictionary....")
        
         
        with open(dictionary_file_path, 'r') as file:
            # Create a CSV reader
            csv_reader = csv.DictReader(file)
            rows = []
            for row in csv_reader:
                rows.append(row)
            # Iterate through each row in the CSV
            for row in rows:
                entry = row['ï»¿Entry']
                entry = re.sub(r'^\W+|\W+$', '', entry)
                entry = self.check_duplicate(entry)
                positive = row['Positiv']
                negative = row['Negativ']
                strong = row['Strong']
                weak = row['Weak']
                active = row['Active']
                passive = row['Passive']
                if entry not in self.sentiment_dict:
                    self.sentiment_dict[entry] = Sentiment(positive, negative, strong, weak, active, passive)
                    print(entry)
                    
        # check if the entry is a duplicate, by checking if it ends with #1
    def check_duplicate(self,entry):
        ending_chars = entry[-2:]
        if ending_chars == "#1":
            # remove the #1 from the entry
            entry = entry[:-2]
        return entry