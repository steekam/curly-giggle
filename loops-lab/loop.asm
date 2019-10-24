section .text
  global _start
  _start:
    mov ecx, 10
    mov eax, '1'

    loop1:
      mov [val], eax
      mov eax, 4
      mov ebx, 1
      push ecx

    mov ecx, val
    mov edx, 1
    int 80h

    mov eax, [val]
    sub eax, '0'
    inc eax
    add eax, '0'
    pop ecx
    loop loop1

    mov eax, 1
    int 80h

section .bss
  val resb 1