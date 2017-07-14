import notify2
import threading
import webbrowser

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

def validate(address):
    # notification for client, may select yes and no
    # default no
    # notification needs to be of critical urgency
    def create_validate_notification(address):
        n = notify2.Notification(
                "Backup Server Request",
                "You received a backup request by {}. Do you accept?", 
                "dialog-information")
        n.set_urgency(notify2.URGENCY_CRITICAL)
        n.add_action("yes", "Yes", None)
        n.add_action("no", "No", None)
        
        n.show()
        Gtk.main()

    create_validate_notification(address)

    def set_backup_server(address):
        pass

if __name__ == "__main__":
    notify2.init("Flask Action Test", mainloop='glib')
    validate('test')
        
