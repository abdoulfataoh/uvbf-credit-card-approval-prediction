# Creation du dataset:
# Telecharge le fichier qui contient les infos sur la table "application"
# Telecharge le fichier qui contient les infos sur la table "credit"
# Creation du dataset final en mergant les deux tables(fichiers)
# Split en train et test
# Enregistrer dans "assets/data"

from numpy.core.defchararray import index
import gdown
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from config import Config

# Set seed
np.random.seed(Config.RANDON_SEED)

# Creer le dossier assets/original_dataset
Config.ORIGINAL_DATASETS_FILES_PATH.mkdir(parents=True, exist_ok=True)

# # Creer le dossier assets/data
Config.DATASET_PATH.mkdir(parents=True, exist_ok=True)

# Telecharge le fichier applications
gdown.download(
    str(Config.ORIGINAL_APPLICATION_FILE_DOWNLOAD_LINK),
    str(Config.ORIGINAL_APPLICATION_FILE_PATH),
    quiet=False
)

# Telecharge le fichier credit
gdown.download(
    str(Config.ORIGINAL_CREDIT_FILE_DOWNLOAD_LINK),
    str(Config.ORIGINAL_CREDIT_FILE_PATH),
    quiet=False
)

# daframes 'application' et 'credit'
application_df = pd.read_csv(str(Config.ORIGINAL_APPLICATION_FILE_PATH))
credit_df = pd.read_csv(str(Config.ORIGINAL_CREDIT_FILE_PATH))

# merger les deux dataframe en utilisant l'ID
full_dataset = application_df.merge(credit_df, on='ID')

# split du dataset
df_train, df_test = train_test_split(
    full_dataset, test_size=Config.TEST_SIZE, 
    random_state=Config.RANDON_SEED
)

# sauvegarde des dataframes
df_train.to_csv(str(Config.DATASET_PATH / "train.csv"), index=None)
df_test.to_csv(str(Config.DATASET_PATH / "test.csv"), index=None)