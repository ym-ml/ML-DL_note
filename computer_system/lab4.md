
## phase3.o:     
file format elf32-i386

Disassembly of section .text:

00000000 <do_phase>:
   0:	55                   	           push   %ebp
   1:	89 e5                	       mov    %esp,%ebp
   3:	53                        	   push   %ebx
   4:	83 ec 24              	   sub    $0x24,%esp
   7:	65 a1 14 00 00 00      mov    %gs:0x14,%eax
   d:	89 45 f4             	       mov    %eax,-0xc(%ebp)
  10:	31 c0                	    xor    %eax,%eax
  12:	c6 45 df 00          	movb   $0x0,-0x21(%ebp)
  16:	c6 45 e0 01          	movb   $0x1,-0x20(%ebp)
  1a:	c6 45 e1 02          	movb   $0x2,-0x1f(%ebp)
  1e:	c6 45 e2 03          	movb   $0x3,-0x1e(%ebp)
  22:	c6 45 e3 04          	movb   $0x4,-0x1d(%ebp)
  26:	c6 45 e4 05          	movb   $0x5,-0x1c(%ebp)
  2a:	c6 45 e5 06          	movb   $0x6,-0x1b(%ebp)
  2e:	c6 45 e6 07          	movb   $0x7,-0x1a(%ebp)
  32:	c6 45 e7 08          	movb   $0x8,-0x19(%ebp)
  36:	c6 45 e8 09          	movb   $0x9,-0x18(%ebp)
  3a:	c6 45 e9 10          	movb   $0x10,-0x17(%ebp)
  ==3e:	0f b6 54 05 df       	movzbl -0x21(%ebp,%eax,1),%edx==
  ==43:	0f b6 92 00 00 00 00 	movzbl 0x0(%edx),%edx==
  *1.0x0是重定位之前的结果,可以先链接反汇编看一下
  2.movzbl是将八位扩展到32位,和后面的dl取后八位相对应*
  ==4a:	88 54 05 e9          	mov    %dl,-0x17(%ebp,%eax,1)==
  *这里实现了'查表',以一个赋值了的数组,查地址为0x0处的数组/字符串*
  
  4e:	83 c0 01             	add    $0x1,%eax
  51:	83 f8 0a             	cmp    $0xa,%eax
  54:	75 e8                	jne    3e <do_phase+0x3e>
  56:	c6 45 f3 00          movb   $0x0,-0xd(%ebp)   *当时考虑到了是'\0',并且计算地址,确实是*
  5a:	83 ec 0c             	sub    $0xc,%esp
  5d:	8d 5d e9             	lea    -0x17(%ebp),%ebx
  60:	53                   	    push   %ebx
  61:	e8 fc ff ff ff       	       call   62 <do_phase+0x62>
  66:	83 c4 08             	        add    $0x8,%esp
  69:	53                   	            push   %ebx
  6a:	68 00 00 00 00       	    push   $0x0
  6f:	e8 fc ff ff ff       	        call   70 <do_phase+0x70>
  74:	83 c4 10             	        add    $0x10,%esp
  77:	8b 45 f4             	        mov    -0xc(%ebp),%eax
  7a:	65 33 05 14 00 00 00 	xor    %gs:0x14,%eax
  81:	74 05                	        je     88 <do_phase+0x88>
  83:	e8 fc ff ff ff       	       call   84 <do_phase+0x84>
  88:	8b 5d fc             	       mov    -0x4(%ebp),%ebx
  8b:	c9                   	leave  
  8c:	c3                   	ret    

## Phase4
 804906d:	c7 45 de 57 59 51 4b 	movl   $0x4b515957,-0x22(%ebp)
 8049074:	c7 45 e2 48 42 44 4e 	movl   $0x4e444248,-0x1e(%ebp)
 804907b:	66 c7 45 e6 54 55    	movw   $0x5554,-0x1a(%ebp)
 8049081:	c6 45 e8 00          	    movb   $0x0,-0x18(%ebp)
 8049085:	89 c3                	        mov    %eax,%ebx
 8049087:	0f b6 4c 05 de       	    movzbl -0x22(%ebp,%eax,1),%ecx
 804908c:	8d 51 bf             	        lea    -0x41(%ecx),%edx
 804908f:	80 fa 19             	        cmp    $0x19,%dl
 8049092:	0f 87 d3 00 00 00    	ja     804916b <do_phase+0x110>
 ==0x41 是A,A-Z=0x19(25), 所以就是大于A之间跳走,在A--Z之间则进入switch-case== 
 8049098:	0f b6 d2             	       movzbl %dl,%edx
 804909b:	ff 24 95 f8 95 04 08 	jmp    *0x80495f8(,%edx,4)  ==这就是传说中的跳转表==
 ==跳转表是一个指针数组,每个元素是一个指针,四个字节,注意是小端==
 *比如对A,0x41,%edx=0,查表得到地址a2 90 04 08,所以就会跳到mov $0x42,%ecx*
 
 80490a2:	b9 42 00 00 00       	mov    $0x42,%ecx
 80490a7:	e9 bf 00 00 00       	jmp    804916b <do_phase+0x110>
 80490ac:	b9 4d 00 00 00       	mov    $0x4d,%ecx
 80490b1:	e9 b5 00 00 00       	jmp    804916b <do_phase+0x110>
 80490b6:	b9 35 00 00 00       	mov    $0x35,%ecx
 80490bb:	e9 ab 00 00 00       	jmp    804916b <do_phase+0x110>
 80490c0:	b9 30 00 00 00       	mov    $0x30,%ecx
 80490c5:	e9 a1 00 00 00       	jmp    804916b <do_phase+0x110>
 80490ca:	b9 39 00 00 00       	mov    $0x39,%ecx
 80490cf:	e9 97 00 00 00       	jmp    804916b <do_phase+0x110>
 80490d4:	b9 75 00 00 00       	mov    $0x75,%ecx
 80490d9:	e9 8d 00 00 00       	jmp    804916b <do_phase+0x110>
 80490de:	b9 3a 00 00 00       	mov    $0x3a,%ecx
 80490e3:	e9 83 00 00 00       	jmp    804916b <do_phase+0x110>
 80490e8:	b9 7c 00 00 00       	mov    $0x7c,%ecx
 80490ed:	eb 7c                	jmp    804916b <do_phase+0x110>
 80490ef:	b9 7d 00 00 00       	mov    $0x7d,%ecx
 80490f4:	eb 75                	jmp    804916b <do_phase+0x110>
 80490f6:	b9 7c 00 00 00       	mov    $0x7c,%ecx
 80490fb:	eb 6e                	jmp    804916b <do_phase+0x110>
 80490fd:	b9 31 00 00 00       	mov    $0x31,%ecx
 8049102:	eb 67                	jmp    804916b <do_phase+0x110>
 8049104:	b9 3f 00 00 00       	mov    $0x3f,%ecx
 8049109:	eb 60                	jmp    804916b <do_phase+0x110>
 804910b:	b9 7c 00 00 00       	mov    $0x7c,%ecx
 8049110:	eb 59                	jmp    804916b <do_phase+0x110>
 8049112:	b9 37 00 00 00       	mov    $0x37,%ecx
 8049117:	eb 52                	jmp    804916b <do_phase+0x110>
 8049119:	b9 38 00 00 00       	mov    $0x38,%ecx
 804911e:	eb 4b                	jmp    804916b <do_phase+0x110>
 8049120:	b9 48 00 00 00       	mov    $0x48,%ecx
 8049125:	eb 44                	jmp    804916b <do_phase+0x110>
 8049127:	b9 70 00 00 00       	mov    $0x70,%ecx
 804912c:	eb 3d                	jmp    804916b <do_phase+0x110>
 804912e:	b9 36 00 00 00       	mov    $0x36,%ecx
 8049133:	eb 36                	jmp    804916b <do_phase+0x110>
 8049135:	b9 7c 00 00 00       	mov    $0x7c,%ecx
 804913a:	eb 2f                	jmp    804916b <do_phase+0x110>
 804913c:	b9 51 00 00 00       	mov    $0x51,%ecx
 8049141:	eb 28                	jmp    804916b <do_phase+0x110>
 8049143:	b9 34 00 00 00       	mov    $0x34,%ecx
 8049148:	eb 21                	jmp    804916b <do_phase+0x110>
 804914a:	b9 73 00 00 00       	mov    $0x73,%ecx
 804914f:	eb 1a                	jmp    804916b <do_phase+0x110>
 8049151:	b9 33 00 00 00       	mov    $0x33,%ecx
 8049156:	eb 13                	jmp    804916b <do_phase+0x110>
 8049158:	b9 3f 00 00 00       	mov    $0x3f,%ecx
 804915d:	eb 0c                	jmp    804916b <do_phase+0x110>
 804915f:	b9 32 00 00 00       	mov    $0x32,%ecx
 8049164:	eb 05                	jmp    804916b <do_phase+0x110>
 8049166:	b9 55 00 00 00       	mov    $0x55,%ecx

 804916b:	88 4c 1d e9          	mov    %cl,-0x17(%ebp,%ebx,1)
 804916f:	83 c0 01             	add    $0x1,%eax


objdump -dr ...  可以显示重定位信息

## phase2.o
0804905b  < PRvMUdVD >:
 804905b:	55                   	push   %ebp
 804905c:	89 e5                	mov    %esp,%ebp
 804905e:	83 ec 08             	sub    $0x8,%esp
 8049061:	83 ec 0c             	sub    $0xc,%esp
 8049064:	ff 75 08             	==pushl  0x8(%ebp)==
 8049067:	e8 04 f6 ff ff       	call   8048670 <puts@plt>
 804906c:	83 c4 10             	add    $0x10,%esp
 804906f:	83 ec 08             	sub    $0x8,%esp
 8049072:	ff 75 08             	pushl  0x8(%ebp)
 8049075:	68 c0 b0 04 08       	push   $0x804b0c0
 804907a:	e8 d1 f5 ff ff       	call   8048650 <strcpy@plt>
 804907f:	83 c4 10             	add    $0x10,%esp
 8049082:	90                   	nop
 8049083:	c9                   	leave  
 8049084:	c3                   	ret    


08049085 <do_phase>:
 8049085:	55                   	push   %ebp
 8049086:	89 e5                	mov    %esp,%ebp
 8049088:	83 ec 1c             	sub    $0x1c,%esp
 804908b:	68 00 00 36 33       	push   $0x33360000
 8049090:	68 34 32 30 33       	push   $0x33303234
 8049095:	68 35 32 30 32       	push   $0x32303235 *注意方向,不过多试几次就行*
 804909a:	54                   	==push   %esp==           
 **这里push %esp之后< PRvMUdVD >中pushl  0x8(%ebp)传给puts的才是正确的地址**
 804909b:	e8 bb ff ff ff       	call   804905b < PRvMUdVD >
 ......
