# Use the official lightweight Python image.
FROM python:3.7-stretch
WORKDIR /app

COPY 'google.json' 'google.json'
ENV GOOGLE_APPLICATION_CREDENTIALS './google.json'

RUN apt-get update -y
RUN apt-get upgrade -y

# # gcloud
# RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
# RUN gcloud --version
# # RUN gcloud init

# # setup gcloud
# RUN gcloud config set project sonar-272913
# RUN gcloud iam service-accounts create sonarcicd
# RUN gcloud projects add-iam-policy-binding sonar-272913 --member="serviceAccount:sonarcicd@sonar-272913.iam.gserviceaccount.com" --role="roles/owner"
# RUN gcloud iam service-accounts keys create tmp/google.json --iam-account=sonarcicd@sonar-272913.iam.gserviceaccount.com
