# Blog & Private Journaling WebApp

## Requirements
- Python >= 3.8
- Flask  >= 2.0.1
- Flask SQLAlchemy >= 2.5.1
- Flask Migrate >= 3.0.1

### Configuration

1. Clone the repo
```shell
git clone https://gitlab.com/dw16/blog-and-private-journaling-webapp.git blog
```

2. Step into folder
```shell
cd blog
```

3. Create virtual environment
```shell
virtualenv venv 
```

4. Activate the venv
```shell
source venv/bin/activate
```

5. Install the dependencies
```shell
pip install -r requirements.txt
```

6. Copy the <kbd>.env.dist</kbd> to <kbd>.env</kbd> and setup your DB on <kbd>.env</kbd>

7. Run the migrations.
```shell
flask db upgrade
```

8. Run the flask app
```shell
python run.py
```

Happy Coding