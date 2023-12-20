from redfin import Redfin

# Creating a variable "client" and assign it the object of type "Redfin"
client = Redfin()


address = '3411 NW 172nd Ter, Miami Gardens FL'

response = client.search(address)
url = response['payload']['exactMatch']['url']
# print(url)

initial_info = client.initial_info(url)
print(initial_info)

property_id = initial_info['payload']['propertyId']
mls_data = client.below_the_fold(property_id)
print(mls_data)

# listing_id = initial_info['payload']['listingId']
# avm_details = client.avm_details(property_id, listing_id)
