from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    sunday_the_first_count = 0
    for single_date in daterange(start_date, end_date):
        # print(single_date.strftime("%Y-%m-%d"), single_date.weekday())
        if single_date.day == 1 and single_date.weekday() == 6:
            sunday_the_first_count += 1
            print(single_date.strftime("%Y-%m-%d"), single_date.weekday())
    print(sunday_the_first_count)