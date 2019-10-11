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
  mov edx, 3 ;Size of input
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
  mov edx, 3 ;Size of input
  int 80h

  ; Convert input from ASCII to Decimal
  mov al, [firstNumber]
  sub al, '0'

  mov bl, [secondNumber]
  sub bl, '0'

  add al, bl ;Add the numbers

  mov ecx, result     ;Address of result
  cmp al, 10
  jb  SingleDigit

  mov byte [ecx], '1'
  inc ecx          ;Move to position for the units/newline
  inc edx          ;String length if double digit sum
  sub eax, 10       ;Only keep the units


  SingleDigit:
    add al, '0'      ;From number 0-9 to character '0'-'9'
    mov ah, 0xA      ;Append newline
    mov [ecx], ax

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
  mov edx, 4
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
  firstNumber resb 4
  secondNumber resb 4
  result resb 2