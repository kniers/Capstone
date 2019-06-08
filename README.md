Capstone group project

Text adventure game
COCKTAIL HEIST
By Adam Deaton, Collin Zurbrugg, Brendan James, and Steven Knier
Summer 2019

Compiling
On the OSU flip server, compile with "make game"
On any other linux computer:
  1. Install python3.6
  2. Run "python3.6-config --cflags" and save the output in the makefile as PYCFLAGS
  3. Run "python3.6-config --ldflags" and save the output in the makefile as PYLDFLAGS
  4. Compile with "make game"
  
Playing
Launch the game with "./game". The Content directory must be in the same directory as the game executable.

Running tests
Run a test by directing a file to the input.

The basic test is successful if the game completes with a "Congratulations" message
./game < test.txt

The full test is successful if no errors are thrown during the test and the game
completes with a "Congratulations" message
./game < fulltest.txt
