PYCFLAGS=-I/usr/include/python3.6m -I/usr/include/python3.6m -Wno-unused-result -Wsign-compare -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -std=c++11
PYLDFLAGS=-L/usr/lib64 -lpython3.6m -lpthread -ldl -lutil -lm -Xlinker -export-dynamic
CPPFLAGS=-Wall
IDIRS=-I Command -I Parser -I PyEngine

game: game.cpp PyEngine.o Room.o Item.o parser.o
	g++ $(PYCFLAGS) $(PYLDFLAGS) $(IDIRS) PyEngine.o Room.o Item.o parser.o game.cpp -o game

PyEngine.o: PyEngine/PyEngine.cpp PyEngine/PyEngine.h
	g++ $(PYCFLAGS) $(PYLDFLAGS) $(IDIRS) -c PyEngine/PyEngine.cpp

Room.o: PyEngine/Room.cpp PyEngine/Room.h
	g++ $(PYCFLAGS) $(PYLDFLAGS) $(IDIRS) -c PyEngine/Room.cpp

Item.o: PyEngine/Item.cpp PyEngine/Room.h
	g++ $(PYCFLAGS) $(PYLDFLAGS) $(IDIRS) -c PyEngine/Item.cpp

parser.o: Parser/parser.cpp Parser/parser.hpp
	g++ $(CPPFLAGS) $(IDIRS) -c Parser/parser.cpp

clean:
	rm -f *.o *~ game
