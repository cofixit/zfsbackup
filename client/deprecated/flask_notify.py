#!/usr/bin/python3.5

from flask import Flask
app = Flask(__name__)

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import notify2
import sys
import webbrowser
import threading

global thr
thr = None

def create_notification(since):
    n = notify2.Notification(
            "No backup since {} days".format(since), 
            "You haven't made a backup since {} days. Please consider making a backup.".format(since), 
            "dialog-information")

    n.set_urgency(notify2.URGENCY_CRITICAL)
    n.add_action("create-backup", "Create a Backup now", create_backup_cb)
    n.add_action("backup-system", "Show Backup System", backup_system_cb)
    n.add_action("default", "Show Backup System", backup_system_cb)
    n.connect('closed', closed_cb)

    n.show()
    Gtk.main()

def create_backup_cb(n, action):
    assert action == "create-backup"
    print("Creating Backup.")
    n.close()

def backup_system_cb(n, action):
    assert action == "backup-system" or action == "default"
    print("Going to backup system.")
    webbrowser.open_new("http://localhost:5000")
    n.close()

def closed_cb(n):
    print("Notification closed")
    Gtk.main_quit()

@app.route("/notify-no-backup/<int:since>")
def notify_no_backup(since):
    global thr
    if thr is None or not thr.is_alive():
        thr = threading.Thread(target=create_notification, args=[since], kwargs={})
        thr.start()
        return "Notification created."
    return "Error: There is already a notification."

if __name__ == "__main__":
    Flask.debug = True
    notify2.init("Flask Action Test", mainloop='glib')
    app.run()

