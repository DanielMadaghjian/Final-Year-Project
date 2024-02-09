from abc import ABC, abstractmethod

class IFileWriter(ABC):
    @abstractmethod
    def WriteToFile(self, destination_file_path, dictionary):
        pass
    