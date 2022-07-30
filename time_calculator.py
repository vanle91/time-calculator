def add_time(start, duration, day=""):

  days_of_week = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
  }
  day_keys = list(days_of_week.keys())
  
  start_time = start.split()
  time = start_time[0].split(':')

  hour = time[0]
  minute = time[1]
  period = start_time[1]

  add_duration = duration.split(':')
  add_hour = add_duration[0]
  add_minute = add_duration[1]

  new_hour = int(hour) + int(add_hour) + (12 if period == 'PM' else 0)
  new_minute = int(minute) + int(add_minute)

  if new_minute > 60:
    new_minute = new_minute % 60
    new_hour = new_hour + 1

  days_count = new_hour // 24
  
  if days_count > 0:
    new_hour = new_hour % 24
  
  if new_hour >= 12:   
    period = 'PM'
  else:
    period = 'AM'

  if new_hour == 0:
    new_hour = 12
    
  if new_hour > 12:
    new_hour = new_hour - 12

  if new_minute < 10:
    new_minute = f'0{str(new_minute)}'

  new_day = ""
  if day != "":
    day = day.title()
    new_day = days_of_week.get(day) + days_count
    new_day = new_day % 7 if (new_day // 7) > 0 else new_day
    new_day = f', {day_keys[new_day]}'

  if (days_count == 1):
    days_later = f" (next day)"
  else:
    days_later = f" ({days_count} days later)" if days_count > 0 else ""

  new_time = f"{new_hour}:{new_minute} {period}{new_day}{days_later}"
  
  return new_time