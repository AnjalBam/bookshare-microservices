from store.models import Owner


def handle_auth_user_create(data):
    try:
        owner = Owner.objects.create(
            usr_idx=data["idx"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            username=data["username"],
        )
        print("Owner created: ", owner)
    except Exception as e:
        print(e)
        print("Failed creating owner with event 'auth_user_create'")


"""
{'first_name': 'Anjal', 
'last_name': 'Bam', 
'is_staff': False, 
'is_active': True, 
'idx': 'usr_23_ddb5e7ada3954d9789a5ba1fd27782dc', 
'email': 'anjalbam11@gmail.com', 
'is_verified': True}}

"""

event_handler_map = {
    "auth_user_create": handle_auth_user_create,
}