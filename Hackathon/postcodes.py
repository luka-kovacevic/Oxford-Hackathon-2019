import re

jdata= {
   "candidates" : [
      {
         "formatted_address" : "Lambeth, London SE1 7PB, United Kingdom"
      }
   ],
   "status" : "OK"
}

def address(json_object, name):
    l = [] 
        
    for x in json_object['candidates']:
        l.append(x['formatted_address'])
        
    return l

def postcode(l):
    
    postcodes = []
    
    for s in l:
        postcodes.append(re.findall(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', s))
    
    return postcodes

print(postcode(address(jdata,"formatted_address")))


