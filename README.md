# ChatGPT
User chat with chatGpt using openAPI.

### Clone project use follwing command
```
git clone https://github.com/ongraphpythondev/djangoChatAPI.git
```
### Create virtual enviorment and activate it 
```
python -m venv venv
source venv/bin/activate
```
### Install the requirements file
```
pip install -r requirements.txt
```

### To run this project, first you have to download the mongoDB(if you don't have)
For this, you can go to below website.
```
https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04-source
```
or you can follow the below steps.
```
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
sudo apt install mongodb-org
```
now you have to run the mongoDB server
```
sudo systemctl start mongod.service
```


change the directory to main directory
### migrate and run the server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Change the API_KEY in .env file
```
OPENAI_API_KEY = ENTER YOUR API KEY HERE
```

### visit this page 
```
127.0.0.1:8000/
```

