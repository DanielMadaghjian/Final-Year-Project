
from DictionaryBuilder.SentimentDictBuilder import SentimentDictBuilder


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
    sentiment_dict = builder.createDictionary(dictionary_file_path)
    
  