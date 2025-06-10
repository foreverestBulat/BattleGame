import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.environ.get('REDIS_URL')

ADD_MAX_POWER_RANDOM = 20
ADD_MIN_POWER_RANDOM = -20