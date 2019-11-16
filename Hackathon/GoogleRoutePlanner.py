import googlemaps
import UserData
import IndiceToPostcodeConverter
'''
	class that deals with taking the list of postcodes produced from 'RoutePostcodeConverter' and producing a google maps url link.
	ALGORITHM:
		takes the first element of the postcodes List and applies it as the start location of the directions 
'''
class GoogleRoutePlanner :

	def __init__(self, userData, postcodes) :
		self.userData = userData
		self.postcodes = postcodes