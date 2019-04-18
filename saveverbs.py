#to save more verbs, edit the object in this file, run the file, and the file
#verbs.p will be updated

import pickle

verbs = { "eat": {"eat"}, "take": {"take", "grab"}}

pickle.dump( verbs, open( "verblist.p", "wb" ) )
