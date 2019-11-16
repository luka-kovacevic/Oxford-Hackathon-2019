
#class that converts the route produced from TSM 
#- I Don't know how well this works, but the functions dictionaryPostToIndex and incidenceToMatrix work
class RoutePostcodeConverter :
	#when converter is initialised, it contains the route from TSM and the
	#postcodes from the google API
	def __init__(self, postcodes, routeIndices) :
		self.postcodes = postcodes
		self.routeIndices = routeIndices

	#helper function that creates a dictionary assigning postcode to index value
	def dictionaryPostToIndex(postcodes) : 
		dictionaryPostIndex = dict(zip(range(len(self.postcodes)),self.postcodes))
		return dictionaryPostIndex

	"""
		take a list of values that form the route from the travelling salesman 
		and a dictionary of indices to postcodes - from function 
		dictionaryPostToIndex and converts the route to a list of postcodes 
	"""
	def incidenceToMatrix(routeList,dictPostcodes) :
		postcodes = []
		for currentRouteValue in routeList :
			currentPostcode = dictPostcodes.get(self.currentRouteValue)
			postcodes.append(self.currentPostcode)
		return postcodes

	def getPostcodeRoute() :
		dictionary = dictionaryPostIndex(self.postcodes)
		routePostcodes = incidenceToMatrix(self.routeIndices, self.dictionary)
		return routePostcodes

