# Bookshare Microservices
It is a Microservices application. One of my side projects to practice and implement different concepts learnt about microservices architecture.

## Service List
- [x] Auth - handle user authorization and authentication
- [x] Store - handle book ordering, lending, borrowing, along with borrowing history, etc.
- [ ] BookMetadata - Handle Storage of book meta data such as isbn, name, author, cover images, etc.
- [ ] Notification Service - handle notifications on Requests, Orders, etc.
- [ ] Posts should handle user posting books, reviews, and public requests.


## Feature Progress

- [x] Create two services: Auth and Store

- [x] the `auth` service will handle all the authentication and authorization

- [x] There will be individual database services for each service

- [x] Create an API gateway (in our case it is called `mool_dwar`) which identify services based on endpoints, and reroute the requests to the respective services

- [x] Create a message queue, we've used `RabbitMQ`, for asynchronous communication between the services

- [x] Establish a communication standard, or specifically message exchange format, to facilitate a seamless communication between the services. This will help make communication uniform across various services in future too.

- [x] Create a communication between the auth and store such that, if a user is created in authentication service, it should create an entry in `Owner` model in the store service, which will treat and manage its own data there. This model is supposed to be in sync with the User table where both of them share the same `idx`.

- [x] The API Gateway will also handle the inter service communication to make sure the services receive the requests only from the gateway and otherwise will get rejected.

- [ ] If any user creation update or deletion, any events shall trigger an event with a broadcast message to all the listening services and will make changes likewise.

- [ ] The API and management for authentication for services.


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