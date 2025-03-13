import requests
from esdbclient import EventStoreDBClient, NewEvent, StreamState    # Import the necessary modules from the esdbclient package
import uuid

link = "http://localhost:8080/cgi-bin/get_data.py"

# get request object
f = requests.get(link)

# get the response text, strip whitespace
json_event = f.text.strip()

# create a client
client = EventStoreDBClient(uri="esdb://localhost:2113?tls=false")  

# Create event_id
event_id = uuid.uuid4()

# Set event Type
event_type = "your_event_type" 

event_data = json_event

data_as_bytes = event_data.encode()

event = NewEvent(type=event_type, data=data_as_bytes, id=event_id)


# Define the stream name where the event will be appended
stream_name = "choose_a_stream_name"

client.append_to_stream(             # Append the event to a stream
    stream_name,                    # Name of the stream to append the event to
    events=[event],              # The event to append (in a list)
    current_version=StreamState.ANY  # Set to append regardless of the current stream state (you can ignore this for now)
)

client.close()