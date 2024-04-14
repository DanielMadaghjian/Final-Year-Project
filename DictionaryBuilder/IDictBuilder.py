from abc import ABC, abstractmethod

class IDictBuilder(ABC):
    @abstractmethod
    def createDictionary(self, dictionary_file_path):
        pass
