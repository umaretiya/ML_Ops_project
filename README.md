# ML_Ops_project
This is end to end machine learning projects with automation

### Tools/Software and accounts requirements

1. [Github Acconts](https://github.com)
2. [Heroku Accounts](https://dashboard.heroku.com/Login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT Cli](https://git-scm.com/downloads)

### creating conda environments
```
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

HEROKU EMAIL - umaretiya@gmail.com
HEROKU API - 04420eaa-c5d2-4bd9-bf8b-93f70c2d1ad3
HEROKU APP NAME - flask-ml01

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
