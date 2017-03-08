import notifications
from notifications import Notifications

if __name__ == "__main__":
    n = Notifications('test')
    n.create(
            'thekey',
            'The Title', 
            'This is the text.'
    )
    n['thekey'].set_urgency(notifications.URGENCY_CRITICAL)
    n.show('thekey')

