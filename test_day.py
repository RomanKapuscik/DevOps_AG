from datetime import datetime
import random

random_day = random.choice(list(range(7)))
today = datetime.today().weekday()



def test_day_of_week():
    assert random_day == today