from text_summarizer.config.config import ConfigurationManager
from text_summarizer.components.data import Data
from text_summarizer.logging import logger

class DataTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_config = config.get_data_config()
        data = Data(config=data_config)
        data.download_file()
        data.extract_zip_file()