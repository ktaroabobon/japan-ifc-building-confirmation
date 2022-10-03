/bin/zsh

TOKEN=$(gcloud auth print-identity-token)

curl --request GET -sL \
  --url 'https://japan-ifc-building-confirmation-api-vjxfkgpbxa-an.a.run.app/health' \
  --header "Authorization: Bearer $TOKEN"
