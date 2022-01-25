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

# launch script
RUN chmod 777 launch.sh


