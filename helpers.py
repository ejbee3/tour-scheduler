from classes import RotationIterator
from datetime import datetime, timedelta

TIME_FRMT = '%H:%M'

def get_break_end(break_start, break_length):
    br_end = datetime.strptime(break_start, TIME_FRMT) + timedelta(minutes=int(break_length))
    return br_end.strftime(TIME_FRMT)


# def is_after_lunch(slot, second_sales_break_end):
#     diff = int((datetime.strptime(slot, TIME_FRMT) - datetime.strptime(second_sales_break_end, TIME_FRMT)).total_seconds() / 60)
#     print(diff)
#     if diff > 0:
#         return True
#     else:
#         return False
    

def get_sales_staff(staff):
    sales_staff = []
    for i in range(len(staff)):
        for j in range(i + 1, len(staff)):
            if staff[i]['is_sales'] and staff[j]['is_sales']:
                sales_staff += [staff[i], staff[j]]
    return sales_staff


def is_on_truck(tour, slot):
    if tour == None:
        return False
    else:
        current_tour = datetime.strptime(tour, TIME_FRMT)
        current_slot = datetime.strptime(slot, TIME_FRMT)
        diff = int((current_slot - current_tour).total_seconds() / 60)
        if diff < 45:
            return True
        else:
            return False


def is_on_break(slot, break_start, break_end):
    br_start = datetime.strptime(break_start, TIME_FRMT)
    br_end = datetime.strptime(break_end, TIME_FRMT)
    if br_start - timedelta(minutes=15) <= datetime.strptime(slot,TIME_FRMT) < br_end + timedelta(minutes=10):
        return True
    else:
        return False


def check_sales_available(staff):
    # always only two sales people on any day (both aren't always photographers tho~~)
    sales1 = staff[0]
    sales2 = staff[1]
    if sales1['is_available'] and sales2['is_available']:
        return True
    else:
        return False
    

def make_schedule(staff, slots):
    schedule = []
    rotation = RotationIterator(staff)
    for slot in slots:
        all_staff_busy = False
        busy_count = 0
        for i, person in enumerate(staff):
            #check conditions to see if person is available
            if not person['is_available']:
                busy_count += 1
            person_is_on_truck = is_on_truck(person['current_tour'], slot)
            person_is_on_break = is_on_break(slot, person['br_start'], person['br_end'])
            if (
                    not person_is_on_truck and 
                    not person_is_on_break
                ):
                person['is_available'] = True
            # check if sales is available
            if person['is_sales'] and i == len(staff) - 1: 
                sales_staff = get_sales_staff(staff)
                if not check_sales_available(sales_staff):
                    person['is_available'] = False
                # print(f"{person['name']} : {person['is_available']}") 
        # check for edge cases
        if busy_count == len(staff):
            all_staff_busy = True
        # get sales on truck after lunch
        no_tours = sorted(staff, key=lambda x: (x['tours'], x['is_sales']))
        if 1500 <= int(slot.replace(':', '')) <= 1530 and no_tours[0]['tours'] == 0:
            staff.sort(key=lambda x: (x['tours'], x['is_sales'], int(x['br_start'].replace(':', ''))))
            rotation.restart()
        else:
            staff.sort(key=lambda x: (x['is_sales'], int(x['br_start'].replace(':', ''))))     
        while True:
            try:
                person = next(rotation)
            except StopIteration:
                rotation.restart()
            else:
                if person['is_available']:
                    schedule.append({slot : person['name']})
                    person['is_available'] = False
                    person['tours'] += 1
                    person['current_tour'] = slot
                    break
                elif all_staff_busy:
                    schedule.append({slot : 'NO PG'})
                    break
    return schedule


make_schedule([{'name': 'Hailey', 'br_start': '13:00', 'is_sales': False, 'br_end': '14:00', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Jana', 'br_start': '14:00', 'is_sales': False, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Steven', 'br_start': '14:45', 'is_sales': False, 'br_end': '15:30', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Dylan', 'br_start': '13:00', 'is_sales': True, 'br_end': '13:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Joe', 'br_start': '14:00', 'is_sales': True, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}], 
                          ['10:45', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '13:45', '14:00', '14:45', '15:00'])



    


