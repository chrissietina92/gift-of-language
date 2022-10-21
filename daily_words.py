from datetime import date, datetime
from #rebeccas pythonfile import login_interface


# Userdefined exception
class Value_not_in_twenty_four_hour(ValueError):
    # called if the time entered is not in 24hr time
    pass


def set_reminder_time():

    try:
        print("Please enter the time you would like your daily reminder in 24hr format.")
        reminderHour = int(input("Enter the Hour : "))
        reminderMin = int(input("Enter the Minute : "))

        if 24 < reminderHour < 1 and 60 < reminderMin < 1:
            raise Value_not_in_twenty_four_hour
    
    except Value_not_in_twenty_four_hour:
        print("Please enter your reminder time in 24hr format.")

    else:          
        if reminderHour == datetime.datetime.now().hour and reminderMin == datetime.now().minute: #if the current time is equal to the reminder time

            display_random_word_and_definition()

        

def display_random_word_and_definition():
    pass
    #  prints a randomly selected word and its definition from the api

if login_interface() == True:  # if user successfully logs in
    set_reminder_time()        # let them set a time reminder for their random words

    
    