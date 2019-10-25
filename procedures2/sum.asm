SYS_OUT equ 1
SYS_IN equ 0
SYS_WRITE equ 4
SYS_READ equ 3
SYS_EXIT equ 1

;Macros
%macro write 2
  mov eax, SYS_WRITE
  mov ebx, SYS_OUT
  mov ecx, %1
  mov edx, %2
  int 80h
%endmacro

%macro read 2
  mov eax, SYS_READ
  mov ebx, SYS_IN
  mov ecx, %1
  mov edx, %2
  int 80h
%endmacro

section .text
  global _start
  _start:

  write msg1, msg1Len
  read firstNumber, 2

  write msg2, msg2Len
  read secondNumber, 2

  ;move values to eax and ebx
  mov eax, [firstNumber]
  sub eax, '0'

  mov ebx, [secondNumber]
  sub ebx, '0'
  call sumOf

  write msgSum, msgSumLen
  write sum, 2

  write lf, 1

  mov eax, 1
  mov ebx, 0
  int 80h

  ;Procedure to find sum
  sumOf:
    add eax, ebx
    add eax, '0' ;convert to ASCII
    mov [sum], eax
    ret

section .data
  msg1 db "Enter first number: "
  msg1Len equ $-msg1
  msg2 db "Enter the second number: "
  msg2Len equ $-msg2
  msgSum db "The sum is: "
  msgSumLen equ $-msgSum
  lf db 10

section .bss
  firstNumber resb 2
  secondNumber resb 2
  sum resb 2