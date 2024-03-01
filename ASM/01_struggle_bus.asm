section .data
msg db "Struggle Bus!", 0xA
msg_len equ $-msg

global _start

section .text
        _start:
        mov edx, msg_len
        mov ecx, msg
        mov ebx, 1
        mov eax, 4
        int 0x80

        mov eax, 1
        int 0x80
