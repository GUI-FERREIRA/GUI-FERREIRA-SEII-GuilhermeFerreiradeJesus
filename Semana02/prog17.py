import datetime
import pytz

tday = datetime.date.today()

# weekday() - segunda=0 e domingo= 6
# isoweekday() - segunda=1 e domingo= 7
print(tday)
print(datetime.date.weekday(tday))
print(datetime.date.isoweekday(tday))


tdelta = datetime.timedelta(hours=12)

print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2000, 2, 15)
till_bday = bday - tday
print(till_bday.days)


dt = datetime.datetime(2021,3,13,14,54,10,tzinfo=pytz.UTC)
print(dir(dt))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)