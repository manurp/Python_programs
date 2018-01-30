import datetime
import calendar

balance = 80000
interest_rate = 5 * 0.01
montly_payment = 1000
montly_withdrawl = 500

today = datetime.date.today()

# print(today)

days_in_current_month = calendar.monthrange(today.year, today.month)[1]

# print(days_in_current_month)
# print(today.day)

days_till_end_month = days_in_current_month - today.day
# print(days_till_end_month)

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
# print(start_date)

end_date = start_date

count = 10
while count:
    interest_charge = (interest_rate) * balance
    balance += interest_charge + montly_payment
    balance -= montly_withdrawl

    balance = 0 if balance < 0 else round(balance, 2)
    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
    # print(balance)
    count -= 1
