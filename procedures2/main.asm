%include 'functions.asm'


section .text
  global _start
  _start:
    mov eax, msg1
    call sprint

    mov edx, 255
    mov ecx, name
    mov ebx, 0
    mov eax, 3
    int 80h

    mov eax, msg2
    call sprint

    mov eax, name
    call sprint

    call quit

section .data
  msg1 db "Please enter your name: ",0h
  msg2 db "Hello, ",0h
  lf db 10

section .bss
  name: resb 255