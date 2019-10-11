section .text
  global _start
  _start:
    ;Create
    mov ecx, 0777
    mov ebx, filename
    mov eax, 8 ; sys_create file
    int 80h

    mov [fd], eax

    ;Write content
    mov eax,4
    mov ebx, [fd]
    mov ecx, parte
    mov edx, parte_len
    int 80h

    ;Close file
    mov eax, 6
    mov ebx, [fd]
    int 80h

    ;Exit
    mov ebx, 0
    mov eax, 1
    int 80h


section .data
  filename db 'file.txt',0h
  parte db 'partition'
  parte_len equ $-parte

section .bss
  fd resb 1