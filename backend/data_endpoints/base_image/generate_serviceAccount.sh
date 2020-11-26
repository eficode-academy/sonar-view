#!/bin/bash

# install gcloud on your machine, and authenticate via the browser
# Example (Works for ubuntu)
echo "If you do not have gcloud installed, look in the script for install command for ubuntu"
# echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
gcloud --version

# setup gcloud
gcloud config set project sonar-272913
gcloud iam service-accounts create sonarcicd
gcloud projects add-iam-policy-binding sonar-272913 --member="serviceAccount:sonarcicd@sonar-272913.iam.gserviceaccount.com" --role="roles/owner"
gcloud iam service-accounts keys create google.json --iam-account=sonarcicd@sonar-272913.iam.gserviceaccount.com