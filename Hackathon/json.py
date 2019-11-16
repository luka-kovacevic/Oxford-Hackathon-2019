import json

jdata= [
      {"formatted_address" : "Lambeth, London SE1 7PB, United Kingdom"}
   ]

def address(json_object, name):
    for dict in json_object:
        if dict['formatted_address'] == formatted_address:
            return dict[formated_address]

def postcode(s):
    return re.findall(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', s)

print("test")
print(postcode(address(jdata)))


