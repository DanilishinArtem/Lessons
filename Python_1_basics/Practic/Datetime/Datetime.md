# Datetime
- date - for years, months, days;
- time - for hours, minutes and seconds;
- datetime - for dates and time simultaneously
- timedelta - for intervals dates and/or time

```python
from datetime import date

if __name__ == "__main__":
    halloween = date(2019, 10, 31)
    print(f'[INFO] day: {halloween.day}, month: {halloween.month}, year: {halloween.year}')
```
Example for deltatime
```python
from datetime import date
from datetime import timedelta

if __name__ == "__main__":
    now = date.today()
    one_day = timedelta(days=1)
    tomorrow = now + one_day
    over_17days = now + 17*one_day
    print(f'[INFO] now: {now.isoformat()}, tomorrow: {tomorrow.isoformat()}, over 17 days: {over_17days}')
```