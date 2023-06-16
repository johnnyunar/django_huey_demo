import random

import requests
from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from demo.models import Activity


@db_periodic_task(crontab(minute='*/1'), retries=2, retry_delay=20)
def fetch_activity():
    endpoint = "https://www.boredapi.com/api/activity"
    r = requests.get(endpoint)
    if random.randint(1, 5) == 5:
        raise Exception("Random exception: unable to fetch data from Bored API")
    elif r.status_code == 200:
        data = r.json()
        Activity.objects.create(
            name=data["activity"],
            type=data["type"],
            participants=data["participants"],
            price=data["price"],
            link=data["link"],
            key=data["key"],
            accessibility=data["accessibility"],
        )
        return data

    raise Exception("Unable to fetch data from Bored API")
