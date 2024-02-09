
from Sentiment_Objects.Sentiment import Sentiment
from DictionaryBuilder.northAndSouthDictBuilder import northAndSouthDictBuilder

import unittest


def test_convert_member_name():
    speaker_builder = northAndSouthDictBuilder()
    result = speaker_builder.convert_Member_Name('mr-william-acourt')
    assert result == "MR WILLIAM ACOURT"
def test_get_first_word():
    speaker_builder = northAndSouthDictBuilder()
    result = speaker_builder.get_First_Word('Dorchester December 28, 1812 - April 11, 1814')
    assert result == "DORCHESTER"
    result = speaker_builder.get_First_Word('Dublin University July  4, 1892 - December 14, 1918|Belfast Duncairn December 14, 1918 - May 31, 1921')
    assert result == "DUBLIN"
    
    
    
    
    
    