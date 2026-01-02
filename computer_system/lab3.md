1. 学校用的是小端.
	对于$ebp+4,   
	x/4x $ebp+4 是从+4往上走个字节
```handdrawn-ink
{
	"versionAtEmbed": "0.3.4",
	"filepath": "computer_system/Ink/Drawing/2026.1.2 - 21.14pm.drawing",
	"width": 472,
	"aspectRatio": 1.5904179006252057
}
```
2. 编译汇编:gcc -m32 -c -o asm.o asm.s 由汇编代码.s文件 生成了.o文件,然后可以正常对.o文件用objdump    *-c 生成 .o文件 *
3. gcc -m32 hello.c -o hello 生成可执行文件
4. 由第四题可认识到,ebp的旧值,是函数最最开始的`push %ebp`的时候ebp的值.