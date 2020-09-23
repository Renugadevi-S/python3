#Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)


from datetime import date
first_date=date(2014, 7, 2)
sec_date=date(2014, 8, 11)
diff=sec_date-first_date
print(diff.days)
