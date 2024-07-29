from helpers import make_schedule, is_on_truck, get_break_end, is_on_break, get_sales_staff, check_sales_available

def test_make_schedule():
    assert make_schedule([{'name': 'Hailey', 'br_start': '13:00', 'is_sales': False, 'br_end': '14:00', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Jana', 'br_start': '14:00', 'is_sales': False, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Steven', 'br_start': '14:45', 'is_sales': False, 'br_end': '15:30', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Dylan', 'br_start': '13:00', 'is_sales': True, 'br_end': '13:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Joe', 'br_start': '14:00', 'is_sales': True, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}], 
                          ['10:45', '11:00', '11:30', '12:00', '15:00']) == [{'10:45': 'Hailey'} , {'11:00': 'Jana'}, {'11:30': 'Steven'}, {'12:00': 'Dylan'}, {'15:00': 'Joe'}]
    assert make_schedule([{'name': 'Hailey', 'br_start': '13:00', 'is_sales': False, 'br_end': '14:00', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Jana', 'br_start': '14:00', 'is_sales': False, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Steven', 'br_start': '14:45', 'is_sales': False, 'br_end': '15:30', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Dylan', 'br_start': '13:00', 'is_sales': True, 'br_end': '13:45', 'is_available': True, 'tours': 0, 'current_tour': None}, 
                          {'name': 'Joe', 'br_start': '14:00', 'is_sales': True, 'br_end': '14:45', 'is_available': True, 'tours': 0, 'current_tour': None}], 
                          ['10:45', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '13:45', '14:00', '14:45', '15:00', '15:30', '15:45', '16:00', '16:30', '16:45', '17:00', '17:30']) == []
    

def test_is_on_truck():
    assert is_on_truck('10:15', '10:30') == True
    assert is_on_truck('10:15', '11:00') == False
    assert is_on_truck('10:45', '11:00') == True
    assert is_on_truck('12:45', '14:00') == False

def test_is_on_break():
    assert is_on_break('10:15', '13:00', '14:00') == False
    assert is_on_break('13:15', '13:00', '14:00') == True
    

def test_get_break_end():
    assert get_break_end('13:00', '60') == '14:00'
    assert get_break_end('14:15', '45') == '15:00'


def test_get_sales_staff():
    assert get_sales_staff([{'name' : 'Steven', 'is_sales' : True}, {'name' : 'Hailey', 'is_sales' : False}, {'name' : 'Joe', 'is_sales' : True}]) == [{'name' : 'Steven', 'is_sales' : True}, {'name' : 'Joe', 'is_sales' : True}]


def test_check_salesperson_available():
    assert check_sales_available([{'name' : 'Dylan', 'is_available' : True}, {'name' : 'Joe', 'is_available' : True}], 'Joe') == True
    assert check_sales_available([{'name' : 'Dylan', 'is_available' : False}, {'name' : 'Joe', 'is_available' : True}], 'Joe') == False




# def test_is_after_lunch():
#     assert is_after_lunch('13:00', '12:45') == True
#     assert is_after_lunch('15:00', '14:45') == True
