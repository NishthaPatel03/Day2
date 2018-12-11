def check_baggage(baggage_amount):
    if (baggage_amount>=0 and baggage_amount<=40):
        return 'true'
    else:
        return 'false'

def check_imigration(expiry_date):
    if (expiry_date>=2001 and expiry_date<=2025):
        return 'true'
    else:
        return 'false'

def check_security(nocstatus):
    if (nocstatus=='true'):
        return 'true'
    else:
        return 'false'


def traveller():
    traveler_id=1001
    traveler_name='Jim'
    baggage_amount=35
    expiry_date=2019
    nocstatus='true'
    status1=check_baggage(baggage_amount)
    status2=check_imigration(expiry_date)
    status3=check_security(nocstatus)

    if (status1=='true' and status2=='true' and status3=='true'):
        print('Traveler_id:',traveler_id)
        print('Name:',traveler_name)
        print('Allow Traveller to fly')

    else:
        print('Traveler_id:',traveler_id)
        print('Name:',traveler_name)
        print('Detain traveller for rechecking')

    return

traveller()