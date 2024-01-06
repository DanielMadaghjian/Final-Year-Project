
from DictionaryBuilder.SentimentDictBuilder import SentimentDictBuilder
from Analyser.ByDateSentimentAnalyser import ByDateSentimentAnalyser
from Analyser.BySpeakerSentimentAnalyser import BySpeakerSentimentAnalyser
from FileWriter.ByDateFileWriter import ByDateFileWriter
from FileWriter.BySpeakerFileWriter import BySpeakerFileWriter


period_speeches_file_path = "C:\\Python Projects\\final_year_project_data\\IrishFamine_Period_Speeches_1845_1852.csv"
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


if __name__ == '__main__':
    # STEP 1: Create Sentiment Dictionary
    builder = SentimentDictBuilder()
    builder.createDictionary(dictionary_file_path)
    
    # STEP 2: Analyse sentiment by year and by speaker
    date_analyser = ByDateSentimentAnalyser(builder.sentiment_dict, famine_dict)
    date_analyser.analyse_speeches(period_speeches_file_path)
    speaker_analyser = BySpeakerSentimentAnalyser(builder.sentiment_dict, famine_dict)
    speaker_analyser.analyse_speeches(period_speeches_file_path)
    
    # STEP 3: Write results to file
    dateFileWriter = ByDateFileWriter(date_analyser.date_dict)
    dateFileWriter.WriteToFile()
    
    speakerFileWriter = BySpeakerFileWriter(speaker_analyser.speakers_dict)
    speakerFileWriter.WriteToFile()
   