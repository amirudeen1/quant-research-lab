import os
import random
import logging
import numpy as np

def set_seed(seed: int = 42):
    """Locks all randomness for perfectly reproducible backtests."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    # Note: If we use PyTorch or TensorFlow later, we will lock them here too.

def get_logger(name: str) -> logging.Logger:
    """Standardized logging for the entire quant lab."""
    logger = logging.getLogger(name)
    
    # Prevent duplicate logs if called multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File output (saves a permanent record)
        file_handler = logging.FileHandler('quant_lab.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger