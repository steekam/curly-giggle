%include "procs.asm"

STD_OUT equ 1
SYS_WRITE equ 4
SYS_READ equ 3
SYS_EXIT equ 1

;Macros
%macro printer 2
  mov eax, SYS_WRITE
  mov ebx, STD_OUT
  mov ecx, %1
  mov edx, %2
  int 80h
%endmacro

section .text
  global _start:
  _start:
  
  mov ecx, 4 ; array size
  mov ebx, 0 ; init sum to 0
  mov eax, x ;move array to eax

  call addition

  printer sumMsg, sumMsgLen
  printer sum, 1
  printer lf, 1

  exit:
  mov eax, SYS_EXIT
  mov ebx, 1
  int 80h


section .data
  x db 1,2,3,1
  sumMsg db "The sum is: "
  sumMsgLen equ $-sumMsg
  lf db 10

section .bss
  sum resb 2