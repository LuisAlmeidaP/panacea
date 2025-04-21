from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from pathlib import Path
from .automationService import AutomationService
import subprocess

AutomationRouter = APIRouter()


@AutomationRouter.get('/')
async def get(paid: str, date: str):
    
    service = AutomationService()
    # service.test()
    service.principal(date=date, paid=paid)
    # return await service.login_procedure()





