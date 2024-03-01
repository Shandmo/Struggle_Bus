.global _start
.intel_syntax noprefix

_start:
	//sys_write
	mov rax, 1
	mov rdi, 1
	lea rsi, [hello_world]
	mov rdx, 14
	syscall

	//sys_exit
	mov rax, 60
	mov rdi, 69
	syscall

hello_world:
	.asciz "Hello, World!\n"

//https://www.youtube.com/watch?v=6S5KRJv-7RU
//Video from Low Level Learning
