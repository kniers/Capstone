import eng

# Define the available verbs
verbs = { 
        "eat": {"eat", "drink"}, 
        "take": {"take", "grab", "get", "steal"}, 
        "look": {"look", "inspect"}, 
        "go": {"go"}, 
        "use": {"use"}, 
        "kill": {"kill"}, 
        "open": {"open", "unlock", "pull out"}, 
        "close": {"close"}, 
        "touch": {"touch", "feel"}, 
        "wear": {"wear", "equip"}, 
        "read": {"read"}, 
        "drop": {"drop"}, 
        "hit": {"hit", "punch", "break"}, 
        "talk": {"talk", "speak", "ask"}, 
        "sharpen": {"sharpen", "whet"}, 
        "give": {"give"},
        "whack": {"whack"}
    }

eng.setVerbs(verbs)
