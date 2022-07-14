# ML_Ops_project
This is end to end machine learning projects with automation

### Tools/Software and accounts requirements

1. [Github Acconts](https://github.com)
2. [Heroku Accounts](https://dashboard.heroku.com/Login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)

### Learning from sklearn
[gitgub sklearn](https://github.com/scikit-learn/scikit-learn/tree/main/sklearn)
[scikit-learn](https://github.com/scikit-learn)
[tensorflow](https://github.com/tensorflow/tensorflow)
[keras github](https://github.com/keras-team/keras)
### creating conda environments
```
umaretiya/ML_classification_Project

conda create -n wafer3 python=3.10
conda create -p venv python == 3.7 -y
```
OR
```
conda activate venv
```
```
pip install -r requirements.txt
```
```
git add .
```
for commit a changes
```
git commit -m "first commit"
```1
Next command for git
```
git branch -M main
git remote add origin <Repo link>
git push -u origin main
```
To send changes/version on git
```
git push origin main
```
To check remote url
```
git remote -v
```
To configure CICD pipeline on heroku

HEROKU EMAIL - <heroku email>
HEROKU API - <heroku api>
HEROKU APP NAME - <app name>

### Buld docker image
```
docker build -t <image name>:<tag name> .
```
> Note: imagename fro docker must be lowercase

To list docker image
```
docker images
```
Run docker image
```
docker run -p 5000:5000 -e PORT=5000 6ce17fe3d920
```

To check runnig container in docker
```
docker ps
```

to stop docker container
```
docker stop <container_id> ad6cabc7a281
```
Creating yaml file
```
.github/workflows/main.yaml
```
```
python setup.py install
```
install ipykernel
```
pip install ipykernel
```
### setup a Machine Learning Frmaeworks

### Project End to End ML framworks with Flask:

- setup.py: setup configuration module
- app.py: flask app configuration and main moduel
- Dockerfile : cofiguration for image/container creation
- requirements.txt: All required packages-libs for projects
- templates: html files
- static:
    -css
    -js
    -images
- config
    -config.yaml
    -schema.yaml
- main(housing)
    - component
        -data_ingestion
        -data_transformation
        -data_validation
        -model_trainer
        -model_evaluation
        -model_pusher
    - config
    - logger
        -logging: for collects a log
    - exception
        -Exceptions: for handling as an exceptions
    - pipeline
        - pipeline
    - entity
        -config_entity: for Entity connfigurations

### example

[Example Porjects](https://drive.google.com/file/d/1mdWOTgWAzm8yEhWO93atcmk4YYXvTwx8/view)
[mode](https://drive.google.com/u/0/uc?id=1mdWOTgWAzm8yEhWO93atcmk4YYXvTwx8&export=download)


