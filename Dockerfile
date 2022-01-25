# Dockerfile to build uvbf-credit-card-approval-prediction

# Base image
FROM python:3.9

# metadata
LABEL "projet.name"="uvbf-credit-card-approval-prediction"

# workdir
WORKDIR /app

# copy current dir to /app
COPY . ./

# update apt db
RUN apt-get update

# install python requiements packages
RUN pip install -r requirements.txt

# launch model switching script
RUN chmod 777 switch-model.sh && ./switch-model.sh

# run dvc repro
RUN dvc repro

# launch script to get gdrive folder id
RUN chmod 777 gdrive-folder-id.sh && ./gdrive-folder-id.sh

# push data to gdrive
CMD [ "dvc", "push"]

