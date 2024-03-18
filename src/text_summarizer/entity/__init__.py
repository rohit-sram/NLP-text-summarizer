from dataclasses import dataclass
from pathlib import Path

#Entity- return type of a function(s)
@dataclass(frozen=True)
class DataConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path