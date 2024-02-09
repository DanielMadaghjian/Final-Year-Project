from .IFileWriter import IFileWriter
import csv
import os

class BySpeakerFileWriter(IFileWriter):
   
    def WriteToFile(self, destination_file_path, dictionary):
        # Specify the CSV file name
        csv_file = os.path.join('Sentiment_Data_Files', destination_file_path)
        os.makedirs('Sentiment_Data_Files', exist_ok=True)
        # Open the CSV file in write mode
        with open(csv_file, mode='w', newline='',encoding="utf-8") as file:
            writer = csv.writer(file)
            # Write the header (column names)
            writer.writerow(["member_name","total_words","positive", "negative", "strong", "weak", "active", "passive", "negative_sentiment", "famine_terms", "grain_terms", "processed_grain_terms", "livestock_terms", "potato_terms", "hay_terms"])
            # Write the data from the list of objects
            for speaker_name, value in dictionary.items():
                if value.total == 0:
                    sentiment_score = 0
                else:
                    sentiment_score = (value.negative / value.total ) * 100
                formatted_score = f"{sentiment_score:.2f}%"
                writer.writerow([speaker_name, value.total, value.positive, value.negative, value.strong, value.weak, value.active, value.passive, formatted_score, value.famine_terms, value.grains_terms, value.processed_grains_terms, value.livestock_terms, value.potatoes_terms, value.hay_terms])
    