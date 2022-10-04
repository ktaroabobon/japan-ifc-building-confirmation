/bin/zsh

PROJECT_ID=jpn-ifc-bc-api

gcloud config set project $PROJECT_ID

gcloud config set run/region asia-northeast1

docker build -t asia.gcr.io/$PROJECT_ID/japan-ifc-building-confirmation-api-image:v1.1 .

docker images

docker push asia.gcr.io/$PROJECT_ID/japan-ifc-building-confirmation-api-image:v1.1

gcloud iam service-accounts create jpn-ifc-bc-api-identity

gcloud run deploy japan-ifc-building-confirmation-api \
  --image asia.gcr.io/$PROJECT_ID/japan-ifc-building-confirmation-api-image:v1.1 \
  --no-allow-unauthenticated \
  --region asia-northeast1 \
  --service-account jpn-ifc-bc-api-identity@$PROJECT_ID.iam.gserviceaccount.com
