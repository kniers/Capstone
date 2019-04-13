let ExampleDoor = {
    name: 'Door',
    verbs: {
        look: function() {
            if (ExampleRoom.flags.looked == true) {
                print("There's a bright green door in front of you. Looks to be unlocked. Slightly ajar even.")
            } else {
                print("What door?")
            }
        },
        go: function() {
            if (ExampleRoom.flags.looked == true) {
                print("You exit the door and you're back on campus as OSU. Graduation ceremony is about to start. Go you! You beat the game and you're getting a CS degree.")
                WinGame()
            } else {
                print("What door?")
            }
        },
        exit: function() {
            ExampleDoor.verbs.go()
        }
    }
}

let ExampleRoom = {
    name: 'Example Room',
    altNames: ['Example', 'ExampleRoom'],
    longDescription: "You find yourself in a empty, generic example room. This game doesn't feel very complete... You question the life choices that brought you here.",
    shortDescription: "Back in the example room, nothing has changed",
    verbs: {
        look: function() {
         if (ExampleRoom.flags.looked == true) {
             print("There's a door. What are you still doing here?")
         } else {
             print("You look around the empty room and find a door right in front of you. Was that there before?")
             ExampleRoom.flags.looked = true
         }
        }
    },
    flags: {
        looked: false
    },
    items: ["ExampleDoor"]
 }