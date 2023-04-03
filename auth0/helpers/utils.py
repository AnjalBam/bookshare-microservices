import uuid

def get_uid_str():
    uid = str(uuid.uuid4())
    return uid.replace('-', "")