%include 'external.asm'

section .text
  global _start
  _start:
    mov ecx, 0

    nextNumber:
      inc ecx
      mov eax, ecx
      add eax, 48
      push eax
      mov eax, esp
      call sprintLF

      pop eax
      cmp ecx, 9
      jne nextNumber

    call quit
