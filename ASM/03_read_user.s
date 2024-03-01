global _start

section .data
	str: times 100 db 0	;Allocate buffer of 100 bytes
	lf: db 10		;LF for full str-buffer?

section .bss
	e1_len resd 1
	dummy resd 1

section .text
_start:
	mov eax, 3	;Read user input into str variable
	mov ebx, 0
	mov ecx, str	;dest
	mov edx, 100	;length
	int 0x80

	mov [e1_len], eax	; Store # of inputted bytes
	cmp eax, edx		; check if all bytes have read
	jb .2			; jump if g2g
	mov bl, [ecx+eax-1]	; BL = last byte in buffer
	cmp bl, 10		; check for LF in buffer
	je .2			; jump if g2g
	inc DWORD [e1_len]	;if not g2g, length ++ (include 'lf')

	.1:			; Loop
	mov eax, 3		; SYS_READ
	mov ebx, 0		; ebx=0: STDIN
	mov ecx, dummy		; pointer to a temp buffer
	mov edx, 1		; read a single byte
	int 0x80
	test eax, eax		; EOF?
	jz .2			; if EOF then jump.
	mov al, [dummy]		; AL = character
	cmp al, 10		; does character == LF?
	jne .1			; if not LF or EOF the get next character
	.2:			; end of loop

	mov eax, 4		; print 100 bytes starting from str (SYS_WRITE)
	mov ebx, 1
	mov ecx, str		; src
	mov edx, [e1_len]	; length_value
	int 0x80

	mov eax, 1		; set ret value
	mov ebx, 0		; ebx == return code (in this case 0)
	int 0x80

	;https://stackoverflow.com/questions/23468176/read-and-print-user-input-with-x86-assembly-gnu-linux
