# credit card approval prediction

### Description
Les cartes de pointage de crédit sont une méthode de contrôle des risques courante dans le secteur financier. elle utilise les informations personnelles et les données soumises par les demandeurs de carte de crédit pour prédire la probabilité de défaillances futures et d'emprunts par carte de crédit. La banque peut décider d'émettre ou non une carte de crédit au demandeur. Les cotes de crédit peuvent quantifier objectivement l'ampleur du risque.

Dans ce depot, nous utilisons l'appentissage machine pour proposer deux modeles dont l'un basé sur la **regression logistique** et l'autre basé sur le **random forest** pour predire le status d'un client

### Contributeurs
 - KABORE Abdoul Fataoh
 - OUEDRAOGO Ibrahim Alassane
 - ROBGO Karima
 - ROUAMBA Faridatou
 
### Dataset
 - [reference kaggle](https://www.kaggle.com/rikdifos/credit-card-approval-prediction?select=credit_record.csv)

### Fonctionnement
<p align="center">
  <img width="180" src="https://drive.google.com/uc?export=download&id=1u29V3rylBuTiRfg8rMvXiHXmv05vp1xF">
</p>

### Reproduction

#### clonage du projet
- ```git clone https://github.com/abdoulfataoh/uvbf-credit-card-approval-prediction.git```
- ```cd uvbf-credit-card-approval-prediction```

#### Installation installation pipenv
- ```sudo apt-get install pipenv```
- ou ```pip install pipenv```

### Specifier la version de python
- ```vim Pipefile```
- remplacer la version python de cette ligne ```python_version = "3.9"``` par la version equivalente
#### Installation des dependances
- ```pipenv install --dev```

#### Activation d'un environnement virtuel
- ```pipenv shell```

#### Specifier un repertoire google drive pour le versionning du dataset
- ```dvc remote modify  gdrive url gdrive://<google drive folder id>```

#### Switcher sur le modele preferé
- ```git checkout logistic-regression-experiment pour la regression logistic```
- ```git checkout random-forest-experiment pour RandomForestClassifier```
#### Repro
- ```dvc repro```

### Pousser les dataset versionné vers le dossier google drive
- ```dvc push```
