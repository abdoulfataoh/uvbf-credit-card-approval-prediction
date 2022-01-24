# Fichier de configuration global

from pathlib import Path


class Config:
    RANDON_SEED = 30    # valeur de la graine
    TEST_SIZE = 0.2
    ASSETS_PATH = Path("./assets")
    ORIGINAL_DATASETS_FILES_PATH = ASSETS_PATH / "original_datasets"
    ORIGINAL_APPLICATION_FILE_PATH = ORIGINAL_DATASETS_FILES_PATH / "application_record.csv"
    ORIGINAL_APPLICATION_FILE_DOWNLOAD_LINK = "https://drive.google.com/uc?id=1-4Jsn8eeqgdJiLpuKdFbvuYTnLqubJJw"
    ORIGINAL_CREDIT_FILE_PATH = ORIGINAL_DATASETS_FILES_PATH / "credit_record.csv"
    ORIGINAL_CREDIT_FILE_DOWNLOAD_LINK = "https://drive.google.com/uc?id=1-CrKXi8HZ3AYnkgodaPi41c4hWiujkLr"
    DATASET_PATH = ASSETS_PATH / "data"
    FEATURES_PATH = ASSETS_PATH / "features"
    MODELS_PATH = ASSETS_PATH / "models"
    METRICS_FILE_PATH = ASSETS_PATH / "metrics.json"

print(str(Config.ORIGINAL_APPLICATION_FILE_PATH))