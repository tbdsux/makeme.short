![makeme.short](https://img.icons8.com/officel/16/000000/short-position.png) [Credits](https://icons8.com/icon/NC8Fh1I7Z_Ax/short-position)<br>
# makeme.short
A Simple and Lightweight URL Shortener Flask App

#### Built on:
`Flask`
`Python 3.7`

## Running Locally
- ** Install Dependencies **
1. Clone the repository
`git clone https://github.com/TheBoringDude/makeme.short.git`
2. Install and activate virtual environment
`virtualenv venv`
    - Windows
    `venv\Scripts\activate`
    - Linux / Mac
    `source venv\Scripts\activate`
3. Install Python 3 Requirements
`pip3 install -r requirements.txt`

- ** Migrating the Database **
1. Edit the `config.py` and replace the value of `SQLALCHEMY_DATABASE_URI` with your database.
2. Migrate
```shell
python manage.py init
python manage.py migrate
python manage.py upgrade
```

- ** Starting the Server **
`python manage.py runserver -d` The -d runs in `debug` mode.

## ToDo's:
- [ ] Add Custom Error Pages
- [ ] Add Social Login Authentications (0Auth)
- [ ] Add `autodeletion algo` to the QuickLinks
- [ ] Fix future bugs...


#### Made By:
##### :heart: TheBoringDude