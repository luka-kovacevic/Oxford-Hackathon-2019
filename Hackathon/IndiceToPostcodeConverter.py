
#class that converts the route produced from TSM 
#- I Don't know how well this works, but the functions dictionaryPostToIndex and incidenceToMatrix work
class RoutePostcodeConverter :
	#when converter is initialised, it contains the route from TSM and the
	#postcodes from the google API
	#WHEN INIITIALISED WITH A LIST FROM THE TSM, IT SHOULD CREATE A MEMBER VARIABLE THAT IS A LIST OF POSTCODES THAT REPRESENTS THE SAME ROUTE
	#[0,7,2,3,4,12,6,8,1,11,10,5,9,0] -(after __init__)-> [p0,p7,p2,p3,p4,p12,p6,p8,p1,p11,p10,p5,p9,p0]  
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

