# Bookshare Microservices
It is a Microservices application. One of my side projects to practice and implement different concepts learnt about microservices architecture.

## MESSAGE FORMAT

Every application shall use a standard message format to broadcast events to the rabbit mq.

Every message should be a dictionary or a hashmap format including two major keys: `event` and `data`.

#### Convention to follow
**data**: Data can be sent in any format, but usually a HashMap or a dictionary format

**event**: The following naming convention should be followed to event type:

`<service_name>_<event_scope>_<event_type>`

- **service_name**: the actual name of service, e.g. auth
- **event_scope**: The scope of event such as user, customer
- **event_type**: The event type as a user is added modified or deleted.

**NOTE:** Since we cannot use the hashmaps/dicts to transfer messages, we will need to convert them to buffers, fo this we will use the `pickle` library to dump it to binary representation, and we will later decode them in the consumer sides as well.

##### Example of a broadcast message
```python
import pickle

message = {
    "event": "auth_user_add"
    "data": {
        "first_name": "Anjal",
        "last_name": "Bam"
        "username": "anjalbam"
    }
}

bin_message = pickle.dumps(message)
# bin_message is sent to the queue

# On Consumer side
message = pickle.loads(bin_message)
```

> **Note:** This convention of messaging needs to be followed along all the services for data exchange among them.