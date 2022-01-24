# Encodage des valeurs categorielles:
# Combinaison des dataframe train et test pour entrainer l'encoder
# Transformation des valeurs
# enregistrer

import pandas as pd
from config import Config
from sklearn.preprocessing import LabelEncoder

# creer un dossier pour les features
Config.FEATURES_PATH.mkdir(parents=True, exist_ok=True)

# charger les dataframes train et test
df_train = pd.read_csv(str(Config.DATASET_PATH / "train.csv"))
df_test = pd.read_csv(str(Config.DATASET_PATH / "test.csv"))

# concatener les dataframes train et test
full_dataset = pd.concat([df_train, df_test])

# nouvelles instances
train_features = pd.DataFrame()
test_features = pd.DataFrame()

# transformation des valeurs categorielles en analysant tout le df
le = LabelEncoder()
for column in full_dataset:
    if full_dataset[column].dtype == 'object':
        le.fit(full_dataset[column])   # l'encoder analyse une colonne du df complet
        train_features[column] = le.transform(df_train[column]) # encode une colonne du df train
        test_features[column] = le.transform(df_test[column]) # encode une colonne du df test
    else:
        train_features[column] = df_train[column]
        test_features[column] = df_test[column]

# enregistrement des labels pour train et test
train_features["STATUS"].to_csv(str(Config.FEATURES_PATH / "train_labels.csv"), index=None)
test_features["STATUS"].to_csv(str(Config.FEATURES_PATH / "test_labels.csv"), index=None)

# supprimer les  colonnes ID et STATUS
train_features.drop(["ID", "STATUS"], axis=1, inplace=True)
test_features.drop(["ID", "STATUS"], axis=1, inplace=True)

# Enregistrement des features pour train et test
train_features.to_csv(str(Config.FEATURES_PATH / "train_features.csv"), index=None)
test_features.to_csv(str(Config.FEATURES_PATH / "test_features.csv"), index=None)