section .text
  global _start
  _start:
    mov ecx, 9
    mov eax, '9'

    li:
    mov [num], eax
    mov eax, 4
    mov ebx, 1
    push ecx

    mov ecx, num
    mov edx, 1
    int 80h

    mov eax, [num]
    sub eax, '0'
    dec eax
    add eax, '0'
    pop ecx
    loop li

    mov eax, 4
    mov ebx, 1
    mov ecx, 10
    mov edx, 1
    int 80h

    mov eax,1
    int 80h

section .bss
  num resb 1