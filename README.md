# Project description
Interaction of regulators and implementers.
There are 3 containers for service.
  - `nginx` container
  - `pg_data` container for persistent db data
  - `web` container with Python code

## Installation
You need [Docker](https://docs.docker.com/engine/installation/) installed:
##### To start on local machine
- Start local `docker-machine`. For example:
  ```sh
  $ eval $(docker-machine env default)
  ```
- In root project directory
  ```sh
  $ docker-compose up -d
  ```

##### To start on Digital Ocean machine
- Create docker machine on DO. For example:
  ```sh
  $ docker-machine create --driver digitalocean --digitalocean-access-token=aa9399a2175a93b17b1c86c807e08d3fc4b79876545432a629602f61cf6ccd6b production
  ```
- In root project directory
  ```sh
  $ eval $(docker-machine env production)
  $ docker-compose -f docker-compose-production.yml up -d
  ```
