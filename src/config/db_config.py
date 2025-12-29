import os
import platform
from dotenv import load_dotenv
from mysql.connector import pooling

# jika di windows, paksa use_pure=True, jika di linux biarkan default
USE_PURE = True if platform.system() == "Windows" else False

load_dotenv()

dbconfig1 = {
    "host"    : os.getenv("DB_HOST"),
    "user"    : os.getenv("DB_USER"),
    "password": os.getenv("DB_PSWD"),
    "use_pure": USE_PURE
    }

mypool = pooling.MySQLConnectionPool(
    pool_name = "abucom_pool",
    pool_size = 3,
    **dbconfig1
    )