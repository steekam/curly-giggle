; CONSTANTS
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1

SECTION .text
  global _start
  _start:

  ;Output msg1
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, msg1
  mov edx, msg1Len
  int 80h

  ; Read input
  mov eax, SYS_READ
  mov ebx, STDIN
  mov ecx, firstNumber
  mov edx, 2 ;Size of input
  int 80h

  ;Output msg2
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, msg2
  mov edx, msg2Len
  int 80h

  ; Read input
  mov eax, SYS_READ
  mov ebx, STDIN
  mov ecx, secondNumber
  mov edx, 2 ;Size of input
  int 80h

  ; Convert input from ASCII to Decimal
  mov eax, [firstNumber]
  sub eax, '0'

  mov ebx, [secondNumber]
  sub ebx, '0'

  add eax, ebx ;Add the numbers
  add eax, '0' ;Convert to ASCII

  mov [result], eax

  ;Output msg3
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, msg3
  mov edx, msg3Len
  int 80h

  ;Output result
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, result
  mov edx, 2
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

SECTION .data
  msg1 db "Enter the first number: "
  msg1Len equ $-msg1

  msg2 db 'Enter the second number: '
  msg2Len equ $-msg2

  msg3 db 'The result is: '
  msg3Len equ $-msg3

  ;newline
  newline db 0Ah
  newlineLen equ $-newline

SECTION .bss
  firstNumber resb 2
  secondNumber resb 2
  result resb 2