import uuid

def get_uid_str():
    uid = str(uuid.uuid4())
    return uid.replace('-', "")


def get_formatted_broadcast_message(event_type=None, data=None):
    """A utility function to get the broadcast message following the standard convention"""
    return {
        "event": event_type,
        "data": data
    }
