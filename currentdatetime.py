def getdatetime(timedateformat='complete'):
    from datetime import datetime
    timedateformat = timedateformat.lower()
    if timedateformat == 'day':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2]
    elif timedateformat == 'month':
        return ((str(datetime.now())).split(' ')[0]).split('-')[1]
    elif timedateformat == 'year':
        return ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'minute':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
    elif timedateformat == 'second':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
    elif timedateformat == 'millisecond':
        return (str(datetime.now())).split('.')[1]
    elif timedateformat == 'yearmonthday':
        return (str(datetime.now())).split(' ')[0]
    elif timedateformat == 'daymonthyear':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hourminutesecond':
        return ((str(datetime.now())).split(' ')[1]).split('.')[0]
    elif timedateformat == 'secondminutehour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'complete':
        return str(datetime.now())
    elif timedateformat == 'datetime':
        return (str(datetime.now())).split('.')[0]
    elif timedateformat == 'timedate':
        return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]
print(getdatetime())