from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_guest_number = request.form['guests']
    event_location = request.form['location']
    event_desc = request.form['description']
    new_event = Event(event_name, event_date, event_guest_number, event_location, event_desc, False)
    
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

