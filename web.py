import file
from flask import Blueprint
from web_data import WebData

routes = Blueprint('routes', __name__)


@routes.route("/")
def index():
    return "<br/>".join(file.File.tail('alarm.log', 10))


@routes.route("/nextalarm")
def next_alarm():
    return WebData.get('alarm_time')
