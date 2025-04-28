main: libadd
	g++ -o test test.cc  -I../cpp_step/ -L../cpp_step/ -ladd -g

libadd:
	g++ -c -o ../cpp_step/add.o ../cpp_step/add.cc
	ar rcs ../cpp_step/libadd.a ../cpp_step/add.o