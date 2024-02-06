
from DictionaryBuilder.SentimentDictBuilder import SentimentDictBuilder
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser
from Analyser.BySpeakerSentimentAnalyser import BySpeakerSentimentAnalyser
from FileWriter.ByDateFileWriter import ByDateFileWriter
from FileWriter.ByYearlyDateFileWriter import ByYearlyDateFileWriter
from FileWriter.ByBimonthlyDateFileWriter import ByBimonthlyDateFileWriter
from FileWriter.BySpeakerFileWriter import BySpeakerFileWriter
import os

# store all file paths of hansard archive
my_path = "C:\\hansard_data"
hansard_file_list = []

for (directory, subdirectories, files) in os.walk(my_path):
    hansard_file_list.extend(files)
    break  # remove this line to include files inside subdirectories


period_speeches_file_path = "C:\\Python Projects\\final_year_project_data\\IrishFamine_Period_Speeches_1845_1852.csv"
hansard_1835_1840_file_path = "C:\\hansard_data\\1835-1840.csv"
dictionary_file_path = "C:\\Python Projects\\final_year_project_data\\inquirerbasic.csv"
famine_dict = [
    'FAMINE',
    'HUNGER',
    'STARVATION',
    'DEATH',
    'SCARCITY',
    'FOOD SHORTAGE',
    'FOOD CRISIS',
    'MALNUTRITION',
    'POVERTY',
    'DROUGHT',
    'CROP FAILURE',
    'FAMINE-STRICKEN',
    'RATIONS',
    'STARVING',
    'EXTREME HUNGER',
    'WIDESPREAD HUNGER',
    'FAILED HARVEST'
]
# used oed for synonyms during the famine period
grains_dict = [
    'WHEAT', 'WHEAT-BARLEY', 'WHEAT-GRAIN','CEREAL', 'DURUM', 'GRAIN', 'TRITICUM', 'BRAN', 'CORN',
    'OATS', 'AVENA SATIVA',
    'BARLEY', 'BARLEY-CORN', 'BARLEY-HARVEST', 'BARLEYCORN',
]
processed_grains_dict = [
    'FLOUR', 'BARLEY-FLOUR', 'FLOUR-BREAD', 'WHEAT-FLOUR', 'dough', 'pastry',
    'OATMEAL', 'PORRIDGE', 'BURGOO',
]
livestock_dict = [
    'MUTTON',
    'BEEF', 'BOEUF',
    'BACON', 'BACON-PIG', 'PANCETTA', 'FLITCH',
    'BUTTER',
    'MEAT'
]
potatoes_dict = [
    'POTATOES', 'POTATO',
    'YAM', 'YAMS',
    'SPUD', 'SPUDS',
    'VEGETABLE', 'VEGETABLES',
    
]
hay_dict = [
    'HAY','BOG-HAY','TIMOTHY', # Grass grown for Hay
]




if __name__ == '__main__':
    # STEP 1: Create Sentiment Dictionary
    builder = SentimentDictBuilder()
    builder.createDictionary(dictionary_file_path)
    
    # STEP 2: Analyse sentiment by year and by speaker
    date_analyser = ByDateSentimentAnalyser(builder.sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
    speaker_analyser = BySpeakerSentimentAnalyser(builder.sentiment_dict, famine_dict, grains_dict, processed_grains_dict, livestock_dict, potatoes_dict, hay_dict)
    
    print("analysing files....")
    for file in hansard_file_list:
        path = "C:\\hansard_data"+"\\"+file
        date_analyser.analyse_speeches(path)
        speaker_analyser.analyse_speeches(path)
        print(file + " is done analysis")
    
    # STEP 3: Write results to file
    print("writing results to file....")
    yearlyDateFileWriter = ByYearlyDateFileWriter(date_analyser.yearly_date_dict)
    bimonthlyDateFileWriter = ByBimonthlyDateFileWriter(date_analyser.bimonthly_date_dict)
    yearlyDateFileWriter.WriteToFile()
    bimonthlyDateFileWriter.WriteToFile()

    
    speakerFileWriter = BySpeakerFileWriter(speaker_analyser.speakers_dict)
    speakerFileWriter.WriteToFile()
