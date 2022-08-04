from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc


class ApScheduler:
    job_stores = {
        'default': SQLAlchemyJobStore(
            url='sqlite:///jobs.sqlite'
        )

    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 100
    }
    executors = {
        'default': {'type': 'threadpool', 'max_workers': 100},
        'processpool': ProcessPoolExecutor(max_workers=20)
    }
    scheduler: BackgroundScheduler

    def init(self):
        self.scheduler = BackgroundScheduler(
            jobstores=self.job_stores,
            executors=self.executors,
            job_defaults=self.job_defaults,
            timezone=utc
        )

    def start(self):
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()
