echo ">>> runCompileDummy.sh"
COMPILER=$(root-config --cxx)
FLAGS=$(root-config --cflags --libs)
$COMPILER -g -O3 -Wall -Wextra -Wpedantic -o skimDummy skimDummy.cxx $FLAGS
