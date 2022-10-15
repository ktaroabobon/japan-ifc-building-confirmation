PROJECT_ID=jpn-ifc-bc-api
SERVICE_NAME=japan-ifc-building-confirmation-api
REGION=asia-northeast1
SA_NAME=jpn-ifc-bc-api-identity

.PHONY: help
help:
	cat ./Makefile

.PHONY: auth
auth:
	gcloud components update
	gcloud auth	login
	gcloud auth configure-docker

# gcloudのconfigの設定
.PHONY: gcloud/set/config
gcloud/set/config:
	gcloud config set project $(PROJECT_ID)
	gcloud config set run/region $(REGION)

# gcloudのservice accountの作成
.PHONY: gcloud/create/sa
gcloud/create/sa:
	gcloud iam service-accounts create ${SA_NAME}

# 本番用のimageをビルド
.PHONY: build/prod
build/prod:
	docker build -t asia.gcr.io/${PROJECT_ID}/${SERVICE_NAME}-image:${TAG} .

# GCRにimageをデプロイ
.PHONY: gcr/deploy
gcr/deploy:
	docker push asia.gcr.io/${PROJECT_ID}/${SERVICE_NAME}-image:${TAG}

# GCRからimageを削除
.PHONY: __gcr/delete
__gcr/delete:
	gcloud container images delete asia.gcr.io/${PROJECT_ID}/${SERVICE_NAME}-image:${TAG}

# CCRのimageをCloud Runにデプロイ
.PHONY: cloud-run/deploy
cloud-run/deploy:
	gcloud run deploy ${SERVICE_NAME} \
		--image asia.gcr.io/${PROJECT_ID}/${SERVICE_NAME}-image:${TAG} \
		--region ${REGION} \
		--no-allow-unauthenticated \
		--service-account ${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com \

.PHONY: deploy/all
deploy/all:
	$(MAKE) gcloud/set/config -f deploy.mk
	$(MAKE) build/prod TAG=$(TAG) -f deploy.mk
	$(MAKE) gcr/deploy TAG=$(TAG) -f deploy.mk
	$(MAKE) cloud-run/deploy TAG=$(TAG) -f deploy.mk

.PHONY: test/prod
test/prod: API_HOST_URL=https://japan-ifc-building-confirmation-api-vjxfkgpbxa-an.a.run.app
test/prod:
	 curl --request GET -sL \
  	 --header "Authorization: Bearer $$(gcloud auth print-identity-token)" \
  	 --url ${API_HOST_URL}/health
