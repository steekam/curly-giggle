; CONSTANTS
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1

section .text
  global _start
  _start:

  ;Output msg
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, msg
  mov edx, msgLen
  int 80h

  ;newline
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, newline
  mov edx, newlineLen
  int 80h

  mov [msg], dword 'Hand'

  ;Output msg
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, msg
  mov edx, msgLen
  int 80h

  ;newline
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, newline
  mov edx, newlineLen
  int 80h

  ;exit
  mov eax, SYS_EXIT
  int 80h

section .data
  msg db 'Base Ball'
  msgLen equ $-msg

  ;newline
  newline db 0Ah
  newlineLen equ $-newline