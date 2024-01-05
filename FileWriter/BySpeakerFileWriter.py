from .IFileWriter import IFileWriter
import csv
import os

class BySpeakerFileWriter(IFileWriter):
    def __init__(self, speakers_dict):
        self.speakers_dict = speakers_dict
        
    def WriteToFile(self):
        # Specify the CSV file name
        csv_file = os.path.join('Sentiment_Data_Files', 'sentiment_per_speaker.csv')
        # Open the CSV file in write mode
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header (column names)
            writer.writerow(["member_name","total_words","positive", "negative", "strong", "weak", "active", "passive", "sentiment_score", "famine_terms"])
            # Write the data from the list of objects
            for speaker_name, value in self.speakers_dict.items():
                if value.total == 0:
                    sentiment_score = 0
                else:
                    sentiment_score = (value.negative / value.total ) * 100
                formatted_score = f"{sentiment_score:.2f}%"
                writer.writerow([speaker_name, value.total, value.positive, value.negative, value.strong, value.weak, value.active, value.passive, formatted_score, value.famine_terms])