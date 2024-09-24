## UPDATES: 
1. The main endpoint uri = "ws://localhost:8008/ws" (websocket) can accept any parameters from class Config to tune the LLM replies 
2. IMPORTANT: The original files were not changed. All the files with the updates has prefix "extended" extended_original_file_name.py 

## How to launch

TIP: back end also has a default front end but it doesn't support multi agents, only gpt-researcher 

# How to launch the original service: 

1. To launch the original service execute: "docker-compose up --build" This will launch front end and back end service. 
or
1.1 You can also click on the Run button in the root main.py module
or
1.2 Execute: uvicorn main:app --reload


# How to launch the updated service for Valor: 

1. Execute: uvicorn extended_main:app --reload
or
1.1 Run extended_main.py in VS code 
or compose file 
1.2 docker-compose -f docker-compose.valor.yml up --build  This will launch only the backend but still will have default front end from python 


# How to launch standalone updated service for Gerardo server LOCAL: 

IMPORTANT: git branch name "local"
IMPORTANT: if you have an issue with the websocket connection in local development check front end page component for a quick fix
INFO: Dockerfile.extended - is a general extended Dockerfile that is used for Python backend can also be used for Valor
1. Execute: uvicorn extended_main:app --reload
or 
1.1 Run extended_main.py in VS code - this will launch Python front and backend 
or compose file
1.2 docker-compose -f docker-compose-standalone.local.yml up --build  - this will launch Python + React 

# How to launch standalone updated service for Gerardo server Prod: 
IMPORTANT: git branch name "prod" checkout on the server for Ubuntu
1. sudo docker compose -f docker-compose-standalone.prod.yml up --build  - this will launch Python + React 


## Local Development

1. Added Pipfile, so you can use pipenv to start your virt. environment