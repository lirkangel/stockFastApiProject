from conn.apschedule import ApScheduler
from utils.funcs import singleton


@singleton
class AppConnection:
    apscheduler: ApScheduler = ApScheduler()
    redis: None
