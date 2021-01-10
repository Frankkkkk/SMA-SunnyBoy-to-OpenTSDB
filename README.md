# SMA SunnyBoy to OpenTSDB importer
This repo is a simple script that periodically imports SMA SunnyBoy inverter production values to an OpenTSDB database.

I simply run it in order to be able to graph these values on grafana.

If you have a PR, don't hesitate !

Image is on the dockerhub: [frankkkkk/sma-sunnyboy-to-opentsdb](https://hub.docker.com/r/frankkkkk/sma-sunnyboy-to-opentsdb)

# How to run
To run this, simply clone the repo, change the `docker-compose.yml` params, and then
start the container by running `docker-compose up -d`
