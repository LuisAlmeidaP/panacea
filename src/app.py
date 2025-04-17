import asyncio
import sys
import os

# sys.path.append = ( os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) )


from config.envs import Env
from presentation.server import Server
from presentation.routes import router


async def main():
    Env.validate()
    server = Server( port=int(Env.PORT), routes= router )
    await server.start()

if __name__ == "__main__":
    asyncio.run( main() )