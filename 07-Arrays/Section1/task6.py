###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

if __name__ == "__main__":
    days_to_print = [1,4,7]
    for days in days_to_print:
        print(weekday(days))
