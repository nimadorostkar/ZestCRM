# Turky-Rahyab-Task API Services
<hr>

The announcements system  in **Django** Framework. [Nima Dorostkar](https://nimadorostkar.com/)



### Clone this repository

```
git clone https://github.com/nimadorostkar/Turky-Rahyab-Task.git
```

#### Pip
```bash
pip install -r requirements.txt

```

#### Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

<br>

![Turky-Rahyab-Task](https://github.com/nimadorostkar/Turky-Rahyab-Task/blob/master/Screenshot.png)


<br><br>



Build code with docker compose
```
docker-compose build
```

Run the built container
```
docker-compose up -d
```



Build the image and spin up the containers:
```
docker-compose up -d --build
```



Migrate databases
```
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
```



Collect static files
```
docker-compose exec app python manage.py collectstatic
```



Create super user
```
docker-compose exec app python manage.py createsuperuser
```
