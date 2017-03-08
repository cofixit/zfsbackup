import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import notify2
import sys
import threading

URGENCY_CRITICAL = notify2.URGENCY_CRITICAL

class Notifications(dict):

    def __init__(self, main_key):
        super().__init__()
        notify2.init(main_key, mainloop='glib')
        self._mainloop_running = False

    def create(self, key, title, text, icon='dialog-notify'):
        self[key] = notify2.Notification(title, text, icon)

    def show(self, key):
        def start_loop(n):
            n.show()
            Gtk.main()

        def closed_cb(n):
            Gtk.main_quit()

        self[key].connect('closed', closed_cb)
        thr = threading.Thread(target=start_loop, args=[self[key]], kwargs={})
        thr.start()

