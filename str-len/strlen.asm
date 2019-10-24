; Strings group: 100565 101234 094913 102008
; The code below implements the calculation of string length
; The calculated length is used for output stream

section .text
  global _start
  _start:
  mov ebx, msg ; Load msg start memory address
  mov eax, ebx ; Both eax and ebx point to same memory address

  nextchar:
    cmp byte [eax], 0 ; check if we have reached end of string by comparing with 0
    jz finished ; Code will move to finish if code above sets zero flag
    inc eax ; increase eax index
    jmp nextchar ; continue with code

  finished:
    ; Since ebx was initialised to the start memory address, the difference with eax will
    ; be the size of the string
    sub eax, ebx

    ; Print message
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
  ; If you change the string to anything else, it will still run
  msg db 'Another string with diff length',0ah