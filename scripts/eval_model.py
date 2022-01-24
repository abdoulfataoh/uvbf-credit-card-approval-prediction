# Evaluation du modele

from os import remove
import pickle # Serialiser des objets (y comporis des modeles)
import json 

import pandas as pd
from pandas.core.algorithms import mode
from sklearn.metrics import accuracy_score, recall_score, f1_score

from config import Config

X_test = pd.read_csv(str(Config.FEATURES_PATH / "test_features.csv"))
y_test = pd.read_csv(str(Config.FEATURES_PATH / "test_labels.csv"))
y_test = y_test.to_numpy().ravel()

# Restaurer le modèle
model = pickle.load(open(str(Config.MODELS_PATH / "model.pk"), mode='rb'))

# prediction
y_pred = model.predict(X_test)

# metric de mesure de performance
accuracy = accuracy_score(y_test, y_pred)

with open(str(Config.METRICS_FILE_PATH), mode='w') as f:
    json.dump(dict(accuracy=accuracy), f)