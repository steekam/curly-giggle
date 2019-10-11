section .text
  global _start
  _start:
    ; Create file
    mov ecx, 0777
    mov ebx, filename
    mov eax, 8 ; sys_create file
    int 80h

    ;Write into file
    mov edx, contentsLen
    mov ecx, contents
    mov ebx, eax ;File descriptor of created file
    mov eax, 4 ;sys_write
    int 80h


    ;Exit
    mov ebx, 0
    mov eax, 1
    int 80h

section .data
  filename db 'myFile.txt'
  contents db 'Hello World!'
  contentsLen equ $-contents