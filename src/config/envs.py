import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    URL = os.environ.get("URL")
    PORT = os.environ.get("PORT")

    @classmethod
    def validate( cls ):
        envs_required = [
            cls.URL,
            cls.PORT
        ]

        if any( var is None for var in envs_required ):
            raise ValueError('Missing required environment variables.')