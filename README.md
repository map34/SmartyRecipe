# Smarty Recipe

[![Build Status](https://travis-ci.org/ADLSOceanHub/SmartyRecipe.svg?branch=master)](https://travis-ci.org/ADLSOceanHub/SmartyRecipe)

Make cooking hassle-free and more friendly

## Configs

* Use PowerShell or Bash shell for the steps below

## Build images

From the root folder of the project:

```bash
docker-compose -f infra/docker_dev/docker-compose.yml -p smarty_recipe build
```

## Using Docker

### Script Managements

From the root folder of the project:

```bash
# Note, these are not sequential steps. You can use any of them independently of each other.

# To run bash shell
docker-compose -f infra/docker_dev/docker-compose.yml -p smarty_recipe run --rm webserver bash

# To run Flask Python shell
docker-compose -f infra/docker_dev/docker-compose.yml -p smarty_recipe run --rm webserver bash -c "source activate TEST && python backend/server/manage.py shell"

# To run the cluster up
docker-compose -f infra/docker_dev/docker-compose.yml -p smarty_recipe up
```

### Spin Up Jupyter Hub

* Make sure the images are built properly.
* To run Jupyter Hub

```bash
docker-compose -f infra/docker_dev/docker-compose.yml -p smarty_recipe run --rm -p 8888:8888 webserver bash -c "source activate TEST && jupyter notebook --allow-root --notebook-dir=./notebooks --ip=0.0.0.0 --port=8888"
```
* Go http://localhost:8888?token=[token] (make sure copy paste the token from the terminal to [token])
