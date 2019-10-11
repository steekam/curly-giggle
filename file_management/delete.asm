section .text
  global _start
  _start:
    mov ebx, filename
    mov eax, 10 ;sys_delete
    int 80h

    ;Exit
    mov ebx, 0
    mov eax, 1
    int 80h

section .data
  filename db 'myFile.txt'