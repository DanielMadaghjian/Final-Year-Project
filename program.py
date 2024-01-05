
from DictionaryBuilder.SentimentDictBuilder import SentimentDictBuilder
from Analyser.SentimentAnalyser import SentimentAnalyser


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
    analyser = SentimentAnalyser(builder.sentiment_dict, famine_dict)
    analyser.analyse_speeches(period_speeches_file_path)
    
    # STEP 3: Write results to file