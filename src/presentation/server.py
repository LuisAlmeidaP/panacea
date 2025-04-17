import uvicorn
from fastapi import FastAPI, Depends

class Server:
    
    def __init__( self, port: int, routes ):
        self.app = FastAPI(title="AUTOMATIZACION PANASEA", version="0.0.1")
        self.port = port
        self.routes = routes
        self.app.include_router( self.routes )
    
    async def start( self ):
        config = uvicorn.Config( self.app, host="0.0.0.0", port=self.port, reload=True )
        server = uvicorn.Server( config )
        await server.serve()