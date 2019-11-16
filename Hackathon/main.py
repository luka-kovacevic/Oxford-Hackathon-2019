import sys
import GetPlaces, GoogleRoutePlanner, Graph, IndiceToPostcodeConverter, postcodes, TravellingSalesman, UserData

if __name__ == "__main__":
    getPlaces(sys.argv[0], sys.argv[1], sys.argv[2])