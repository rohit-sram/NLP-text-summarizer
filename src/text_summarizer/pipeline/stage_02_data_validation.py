from text_summarizer.config.config import ConfigurationManager
from text_summarizer.components.data_validation import DataValidation
from text_summarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_files_exist()