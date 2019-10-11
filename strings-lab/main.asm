; CONSTANTS
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1

;Macros

; Print out message
%macro printout 2
  mov eax, SYS_WRITE
  mov ebx, STDOUT
  mov ecx, %1
  mov edx, %2
  int 80h
%endmacro


section .text
  global _start
  _start:
    ; printout msg1,msg1Len

    ; Load source and destination
    lea si, msg1
    lea di, msg2

    CLD ; move left to right

    ;Load length of source to CX
    mov cx, msg1Len

    ;Compare
    repe cmpsb
    jne printErr
    
    printOk:
      printout msgOk, msgOkLen
      jmp exit
    
    printErr:
      printout msgErr, msgErrLen

    ;exit
    exit: 
      mov eax, SYS_EXIT
      int 80h

section .data
  msg1 db 'Hello World',0ah
  msg1Len equ $-msg1

  msg2 db 'Hello World',0ah
  msg2Len equ $-msg2

  msgOk db 'Strings match',0ah
  msgOkLen equ $-msgOk
  msgErr db "Strings don't match",0ah
  msgErrLen equ $-msgErr