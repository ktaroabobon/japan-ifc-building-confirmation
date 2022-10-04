/bin/zsh

TOKEN=$(gcloud auth print-identity-token)
#gcloud auth print-identity-token >> token.txt

curl --request GET -sL \
  --url 'https://japan-ifc-building-confirmation-api-vjxfkgpbxa-an.a.run.app/health' \
  --header "Authorization: Bearer $TOKEN"

#curl --request GET -sL \
#  --url 'https://japan-ifc-building-confirmation-api-vjxfkgpbxa-an.a.run.app/law/21-1' \
#  --header "Authorization: Bearer $TOKEN" \
#  --header 'Content-Type: application/json' \
#  -d @./data/post_data.json
