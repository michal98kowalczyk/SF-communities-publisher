# SF-communities-publisher

command line tool to publish Salesforce communities in a faster way using Python and Salesforce CLI

# Prerequisites

- Salesforce CLI
- Python

# Config 
Example of configuration file you can find in config/org.yml file, there you can specify Experience Sites that you want to publish as an array of string

# How to start
- clone repo
- run following commands:
  ```
  pip install pip install -r requirements.txt
  python main.py org={YOUR_ORG_NAME_SPECIFIED_IN_CONFIG_FILE} #e.g. python main.py org=DevTrail1
  ```
