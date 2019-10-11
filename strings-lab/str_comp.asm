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

.CODE
section .text
   Assume cs:code, ds:data
   global _start
   _start:
      mov ax, data
      mov ds, ax
      mov es, ax
   ;  lea si, str1   
   ;  lea di, str2
      mov si, str1   
      mov di, str2

      mov cx, 6
      mov al, strlen1
      mov bl, strlen2
      cmp al, bl
      jne Not_Equal

      repe cmpsb
      jne Not_Equal
      jmp Equal

      Equal:
         printout msgOk, msgOkLen
         jmp exit

      Not_Equal:
         printout msgErr, msgErrLen

      ;exit
      exit: 
         mov eax, SYS_EXIT
         int 80h

section .data
  str1 db 'GLSICT'  
  strlen1 equ $-str1
  str2 db 'GLSICT',
  strlen2 equ $-str2

  msgOk db 'Strings match',0ah
  msgOkLen equ $-msgOk
  msgErr db "Strings don't match",0ah
  msgErrLen equ $-msgErr