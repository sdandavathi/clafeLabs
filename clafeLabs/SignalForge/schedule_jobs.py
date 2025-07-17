from apscheduler.schedulers.background import BackgroundScheduler
from ai_workflow import run_workflow_for_ticker
from config import TICKER_LIST

def schedule_daily_jobs():
    scheduler = BackgroundScheduler()
    for ticker in TICKER_LIST:
        scheduler.add_job(run_workflow_for_ticker, "cron", hour=6, minute=0, args=[ticker])
    scheduler.start()