from .IFileWriter import IFileWriter
import csv
import os

class ByBimonthlyDateFileWriter(IFileWriter):
    def __init__(self, bimonthly_date_dict):
        self.bimonthly_date_dict = bimonthly_date_dict
        
    def WriteToFile(self):
        # Specify the CSV file name
        csv_file = os.path.join('Sentiment_Data_Files', 'sentiment_per_bimonthly.csv')
        # Create the directory if it doesn't exist
        os.makedirs('Sentiment_Data_Files', exist_ok=True)
        
        # Open the CSV file in write mode
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header (column names)
            writer.writerow(["year","month","total_words","positive", "negative", "strong", "weak", "active", "passive", "sentiment_score","famine_terms"])
            # Lists to store data for the graph
            dates = []
            scores = []
            # Write the data from the list of objects
            for date, value in self.bimonthly_date_dict.items():
                if value.total == 0:
                    sentiment_score = 0
                else:
                    sentiment_score = (value.negative / value.total ) * 100
                formatted_score = f"{sentiment_score:.2f}%"
                writer.writerow([date.year,date.month, value.total, value.positive, value.negative, value.strong, value.weak, value.active, value.passive, formatted_score, value.famine_terms])
                 # Append data to the lists for the graph
                dates.append(date)
                scores.append(sentiment_score)