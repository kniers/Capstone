import pickle

def isVerb(checkMe):
	verbs = pickle.load( open( "verblist.p", "rb" ) )

	for v in verbs:
		if checkMe in v:
			return v

	# if we made it this far, we have no hits
	return "nope"
