from text_summarizer.pipeline.stage_01_data import DataTrainingPipeline
from text_summarizer.logging import logger

STAGE_NAME = "Data (Ingestion Stage)"

try: 
    logger.info(f"Stage {STAGE_NAME} has begun")
    data = DataTrainingPipeline()
    data.main()
    logger.info(f"Stage {STAGE_NAME} completed")
    
except Exception as e:
    logger.exception(e)
    raise e