SECTION .text
  global _start
  _start:
    mov ecx, 0777
    mov ebx, filename
    mov eax, 8 ; sys_create file
    int 80h

    ;Exit
    mov ebx, 0
    mov eax, 1
    int 80h

SECTION .data
  filename db 'myFile.txt'