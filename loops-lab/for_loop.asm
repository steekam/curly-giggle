section .data
  msg db "Repeating Message",10
  len equ $-msg


section .text
  global _start
  _start:
    mov eax,0 ;count
    jmp forloop

    forloop:
      cmp eax, 20
      je finished
      push eax
      mov eax,4
      mov ebx,1
      mov ecx, msg
      mov edx, len
      int 80h

      pop eax
      add eax, 1
      jmp forloop

    finished:
      mov eax, 1
      mov ebx, 0
      int 80h