all:
	@g++ -std=c++17 src/*.cpp -Iinclude -Llib  -lmingw32 -lSDL2main -lSDL2 -lSDL2_image -O2 -DNDEBUG -o connect4_minimax -mwindows -static-libgcc -static-libstdc++
