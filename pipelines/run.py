from datetime import timedelta

from flows import flow
from prefect import Flow
from prefect.schedules import IntervalSchedule

scheduler = IntervalSchedule(interval=timedelta(minutes=10))

flow.run()

flow.schedule = scheduler

flow.run()