section .text
  global _start
  _start:
  mov ebx, msg
  mov eax, ebx ; Both eax and ebx point to same memory address

  nextchar:
    cmp byte [eax], 0
    jz finished
    inc eax
    jmp nextchar

  finished:
    sub eax, ebx ; find the string length

    mov edx, eax
    mov ecx, msg
    mov ebx, 1 
    mov eax, 4
    int  80h

    ;Exit
    mov ebx, 0
    mov eax,1
    int 80h


section .data
  msg db 'Another string with diff length',0ah