import file
from flask import Blueprint, send_file
from web_data import WebData
import logging

routes = Blueprint('routes', __name__)


@routes.route("/")
def index():
    return send_file("html/index.html")


@routes.route("/js")
def js():
    return send_file("html/app.js")


@routes.route("/log/<int:length>")
def log(length):
    return "<br/>".join(file.File.tail('alarm.log', length))


@routes.route("/data/<string:element>")
def data(element):
    return WebData.get(element)


@routes.route("/reboot")
def reboot():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]


@routes.route("/loglevel/<string:level>")
def debug(level):
    if level == "info":
        log_level = logging.INFO
    elif level == "debug":
        log_level = logging.DEBUG
    elif level == "error":
        log_level = logging.ERROR
    else:
        return "Invalid log level requested. Allowed values: info, debug, error"

    logging.getLogger().setLevel(log_level)
    logging.info("Log level set to " + level)
    return "Log level set to " + level
