import os
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try: 
        with open(path_to_yaml) as yaml_file: 
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully") 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty or invalid")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dir: list, verbose=True):
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
@ensure_annotations
def get_size(path: Path) -> str:
    size_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_kb} KB"