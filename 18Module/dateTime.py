from datetime import dateTime

current_date = dateTime.now()
print("Current date and time:", current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)
print("Hour:", current_date.hour)
print("Minute:", current_date.minute)
print("Second:", current_date.second)
print("Microsecond:", current_date.microsecond)
print("Timezone:", current_date.tzinfo)
print("ISO format:", current_date.isoformat())
print("Formatted date:", current_date.strftime("%Y-%m-%d %H:%M:%S"))