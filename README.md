# peoplestash-service

This project is a service that allows you to pull data about cards, users, boards etc. from your favorite Agile managment tool. The service then uses ELK stack to do visualization and analysis of our people logs.

Currently Supported Agile Management Tools

- LeanKit - LeanKit APIs


Possible Future Supported Agile Management Tools:

- PivotalTracker
- Atlassian Jira
- Telerik Team Pulse
- More...

ELK Stack versions used

- ElasticSearch: Version: 2.3.2, Build: b9e4a6a/2016-04-21T16:03:47Z, JVM: 1.8.0_92
- Logstash: Version: 2.3.2
- Kibana: Version: 4.5.0


In this project you will find:

- service
	app.py - a python web app using flask that exposes a web api that returns lean kit data that is organized into a format that works well with ELK stack.  The Flask/Python app parses the information provided by the LeanKit API in a more useable form for Logstash.

- server.config - The config file contains the Logstash config using the HTTP poller plugin.  The HTTP poller plugin for Logstash periodically calls the API from the Flask app.  The returned information is then pushed to elasticsearch from Logstash and then Kibana for visualization.  When running Logstash with the config file, run with command ./logstash -f {{configfilename}}

####TODO - add more info about how to install
####TODO - add plugins for APIs for other work tracking tools


