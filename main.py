import public
import private
import api_data

# initialize module functions
public_type = public.public
private_type = private.private
# enter api credentials
api_id = api_data.api_id
api_hash = api_data.api_hash
# ask for user to choose type of channel
channel_type = int(input("Press 1 if your channel is private, press 2 if public : "))
if channel_type == 1:
    private_type(api_id, api_hash)
elif channel_type == 2:
    public_type(api_id, api_hash)
else:
    print("Incorrect type")
