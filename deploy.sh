#!/bin/bash
# gcloud builds submit --tag gcr.io/cdn-dinoia/gig_geolocation

docker build --rm -f "Dockerfile" -t gig_geolocation:latest .
docker tag gig_geolocation gcr.io/cdn-dinoia/gig_geolocation:latest
docker push gcr.io/cdn-dinoia/gig_geolocation:latest

gcloud beta run deploy gig_geolocation --image gcr.io/cdn-dinoia/gig_geolocation 

aplay /usr/share/sounds/purple/alert.wav
