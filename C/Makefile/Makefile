# 链接 .o + .o -> main
main : hello.o main.o
	gcc hello.o main.o -o main

# 预处理 -E .cpp -> .i
hello.i : hello.c hello.h
	gcc -E hello.c -o hello.i
main.i : main.c hello.h
	gcc -E main.c -o main.i

# 编译 -S .i -> .s
hello.s : hello.i
	gcc -S hello.i -o hello.s
main.s : main.i
	gcc -S main.i -o main.s

# 汇编 -c .s -> .o
hello.o : hello.s
	gcc -c hello.s -o hello.o
main.o : main.s
	gcc -c main.s -o main.o

clean :
	rm *.o *.s *.i