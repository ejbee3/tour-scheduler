from flask import Flask, render_template, request
from helpers import get_break_end, make_schedule

app = Flask(__name__)

STAFF = ['Megan', 'Hailey', 'Steven', 
                'Dylan', 'Michael', 'Joe', 'Adriana', 'Jana', 'Tashari']

@app.route("/", methods=['GET', 'POST'])
def home():
    STAFF.sort()
    return render_template("home.html", staff=STAFF)


@app.route("/made", methods=['GET', 'POST'])
def made():
    open_slots = []
    todays_staff = []
    for i in range(0, int(request.args.get("length"))):
        open_slot = request.args.get("slot" + str(i))
        hour = int(open_slot[0])
        if hour > 0 and hour < 9 and len(open_slot) == 4:
            open_slot = f"{hour + 12}:{open_slot[2:]}"
        open_slots.append(open_slot)
    STAFF.sort()
    # make todays staff list of dicts
    for i, name in enumerate(STAFF):
        str_i = str(i)
        if request.form.get("working" + str_i):
            sales = request.form.get("sales" + str_i)
            info_dict = {'name' : name,
                         'br_start' : request.form.get("brStart" + str_i),
                        'br_len' : request.form.get("brLen" + str_i),
                        'is_sales' : True if sales else False
                        }
            todays_staff.append(info_dict)

    for person in todays_staff:
        br_end = get_break_end(person['br_start'], person['br_len'])
        person.update({'br_end' : br_end, 'is_available': False, 'tours': 0, 'current_tour': None})
        del person['br_len']
    
    # predicted_schedule = make_schedule(todays_staff, open_slots)
    print(open_slots)
    
    return render_template("made.html")

if __name__ == '__main__':
    app.run(debug=True)