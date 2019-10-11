section .text
  global _start
  _start:
    mov ecx, 1 ; Write only
    mov ebx, filename
    mov eax, 5 ;sys_open
    int 80h

    mov edx, 2 ; whence argument
    mov ecx, 0 ; move cursor to 0bytes section
    mov ebx, eax ; File descriptor
    mov eax, 19 ;sys_lseek
    int 80h

    mov edx, 9 ; byte size to write
    mov ecx, contents
    ;mov ebx, ebx
    mov eax, 4
    int 80h

    ;Exit
    mov ebx, 0
    mov eax, 1
    int 80h

section .data
  filename db 'myFile.txt', 0h
  contents db '-updated-'