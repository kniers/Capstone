import eng

# Define the available verbs
verbs = { "eat": {"eat"}, "take": {"take", "grab", "get", "steal"}, "look": {"look", "inspect"}, "go": {"go"}, "use": {"use"}, "kill": {"kill"}, "open": {"open", "unlock", "pull out"}, "touch": {"touch", "feel"}, "wear": {"wear", "equip"}, "read": {"read"}, "drop": {"drop"}, "hit": {"hit", "punch"}, "talk": {"talk", "speak"}, "sharpen": {"sharpen", "whet"}}

eng.setVerbs(verbs)
