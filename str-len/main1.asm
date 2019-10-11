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

SECTION .data
msg     db      'Hello, brave new world!', 0Ah ; we can modify this now without having to update anywhere else in the program
 
SECTION .text
    global  _start
    _start:
 
    mov     ebx, msg        ; move the address of our message string into EBX
    mov     eax, ebx        ; move the address in EBX into EAX as well (Both now point to the same segment in memory)
    mov     di, msg

    
    nextchar:
        cmp     byte [eax], 0   ; compare the byte pointed to by EAX at this address against zero (Zero is an end of string delimiter)
        jz      finished        ; jump (if the zero flagged has been set) to the point in the code labeled 'finished'
        inc     eax             ; increment the address in EAX by one byte (if the zero flagged has NOT been set)
        jmp     nextchar        ; jump to the point in the code labeled 'nextchar'
 
    finished:
        sub     eax, ebx        ; subtract the address in EBX from the address in EAX
                                ; remember both registers started pointing to the same address (see line 15)
                                ; but EAX has been incremented one byte for each character in the message string
                                ; when you subtract one memory address from another of the same type
                                ; the result is number of segments between them - in this case the number of bytes
 
    mov     edx, eax        ; EAX now equals the number of bytes in our string
    mov     ecx, msg        ; the rest of the code should be familiar now
    mov     ebx, STDOUT
    mov     eax, SYS_WRITE
    int     80h
    
    ;exit
    exit: 
      mov eax, SYS_EXIT
      int 80h