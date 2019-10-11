section .text

global _start

_start: 
	xor ebx, ebx
	mov edx, $msg_len

next_char: 
	mov al, [msg+ebx]
	cmp al, 'a'
	jb no_change
	cmp al, 'z'
	ja no_change
	and al, 0xDF

no_change:
	mov [res+ebx], al
	inc ebx
	cmp ebx, edx
	jnz next_char

	mov ecx, $msg
	mov ebx, 1
	mov eax, 4
	int 80h

	mov ecx, $res
	mov ebx, 1
	mov eax, 4
	int 80h

	mov ebx, 0
	mov eax, 4
	int 80h

section .data
msg	db "You can't always get what you want", 0xa
msg_len equ $ -msg
res db "                                  ", 0xa
