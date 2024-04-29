from _datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format the current date and time as a string
formatted_datetime = current_datetime.strftime("%d Day:%m:%y , Time is: %H hr:%M min:%S sec")

# Print the formatted date and time
print("Current date and time:", formatted_datetime)


from _datetime import datetime
currentdate=datetime.now()
print(currentdate)
print(currentdate.strftime("Day %d-Month %m-Year %Y,%H(Hr)%M(Min)%SS(Sec)"))





