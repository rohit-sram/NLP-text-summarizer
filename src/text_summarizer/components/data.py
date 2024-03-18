import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger
from text_summarizer.utils.common import get_size
from pathlib import Path
from text_summarizer.entity import (DataConfig)

class Data:
    def __init__(self, config: DataConfig):
        self.config = config
        
    def download_file(self): 
        if not os.path.exists(self.config.local_data_file): 
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Downloaded. Contains the following information. \n{headers}")
        else: 
            logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}.")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)