from fastapi import APIRouter
from .automation.automationController import AutomationRouter

router = APIRouter()
router.include_router(AutomationRouter, prefix="/automation", tags=["Automation"])