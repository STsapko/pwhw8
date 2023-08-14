import configparser
from mongoengine import connect, disconnect_all

config = configparser.ConfigParser()
config.read('config.ini')

mongodb_pass = config.get('DB', 'PASS')
mongo_user = config.get('DB', 'user')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

disconnect_all()
connection_url = f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority'
connect(host=connection_url, ssl=True)
