section text
  global _start
  _start:
    mov esi, 4
    mov ecx, 5
    clc
    
    li:
    mov al, [num1+esi]
    adc al, [num2+esi]
    aaa
    pushf
    or al, 30h
    popf

    mov [sum+esi], al
    dec esi
    loop li

    mov edx, len
    mov ecx, msg
    mov ebx, 1
    mov eax, 4
    int 80h

    mov edx, 5
    mov ecx, sum
    mov ebx, 1
    mov eax, 4
    int 80h

    ; newline
    mov edx, newlineLen
    mov ecx, newline
    mov ebx, 1
    mov eax, 4
    int 80h

    ;exit
    mov eax, 1
    int 80h

section .data
  msg db "The sum is: "
  len equ $-msg

  newline db 0ah
  newlineLen equ $-newline

  num1 db '12345'
  num2 db '23456'
  sum db '      ' ;6 spaces