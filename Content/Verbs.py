import eng

# Define the available verbs
verbs = { 
        "eat": {"eat", "drink"},
        "take": {"take", "grab", "get", "steal", "snatch"},
        "look": {"look", "inspect", "examine"},
        "go": {"go", "walk"},
        "use": {"use"},
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
        "give": {"give"},
        "twist": {"twist"}
    }

eng.setVerbs(verbs)
