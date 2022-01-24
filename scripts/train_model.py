# Entrainement du model:
# importation du datset
# sauvegarde du modele

import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier # modele

from config import Config

Config.MODELS_PATH.mkdir(parents=True, exist_ok=True)

X_train = pd.read_csv(str(Config.FEATURES_PATH / "train_features.csv"))
y_train = pd.read_csv(str(Config.FEATURES_PATH / "train_labels.csv"))

# Entrainement du model
model = RandomForestClassifier(
    n_estimators=250,
    max_depth=12,
    min_samples_leaf=16
)
model.fit(X_train, y_train.to_numpy().ravel())

# Enregisrement du model
pickle.dump(model, open(str(Config.MODELS_PATH / "model.pk"), mode='wb'))