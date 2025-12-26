import os
from dotenv import load_dotenv
from mysql.connector import pooling

load_dotenv()

dbconfig1 = {
    "host"    : os.getenv("DB_HOST"),
    "user"    : os.getenv("DB_USER"),
    "password": os.getenv("DB_PSWD"),
    }

mypool = pooling.MySQLConnectionPool(
    pool_name = "abucom_pool",
    pool_size = 3,
    **dbconfig1
    )