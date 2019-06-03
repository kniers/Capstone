import eng

# Define the available verbs
verbs = { 
        "eat": {"eat", "drink"},
        "take": {"take", "grab", "get", "steal", "snatch"},
        "look": {"look", "inspect", "examine", "check", "search"},
        "go": {"go", "walk", "step", "climb"},
        "use": {"use", "flip"},
        "kill": {"kill"},
        "open": {"open", "unlock", "pull out"},
        "close": {"close"},
        "touch": {"touch", "feel"},
        "wear": {"wear", "equip"},
        "read": {"read"},
        "drop": {"drop"},
        "hit": {"hit", "punch", "break", "whack"},
        "talk": {"talk", "speak", "ask"}, 
        "sharpen": {"sharpen", "whet"}, 
        "give": {"give", "feed"},
	"feel": {"feel"},
	"listen": {"listen"},
	"push": {"push"},
	"twist": {"twist"},
	"investigate": {"investigate"}
    }

eng.setVerbs(verbs)
