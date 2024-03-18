from text_summarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from text_summarizer.utils.common import read_yaml, create_directories
from text_summarizer.entity import (DataConfig)

class ConfigurationManager: 
    def __init__ (
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_config(self) -> DataConfig:
        config = self.config.data
        
        create_directories([config.root_dir])
        
        data_config = DataConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_config