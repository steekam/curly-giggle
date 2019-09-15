section .text
  global _start
  _start:

  mov eax, 4
  mov ebx, 1
  mov ecx, display
  mov edx, displayLen
  int 80h

  ; Display first letter of my name 4 times
  mov eax, 4
  mov ebx, 1
  mov ecx, letter
  mov edx, letterLen
  int 80h

  ;Display newline
  mov eax, 4
  mov ebx, 1
  mov ecx, newline
  mov edx, newlineLen
  int 80h

  ; Name display
  mov eax, 4
  mov ebx, 1
  mov ecx, nameDisplay
  mov edx, nameDisplayLen
  int 80h

  ;Name 4 times
  mov eax, 4
  mov ebx, 1
  mov ecx, name
  mov edx, nameLen
  int 80h

  mov eax, 1
  int 80h

section .data
  display db 'The first letter of my name is: ', 0Ah
  displayLen equ $-display

  letter times 4 db 'S'
  letterLen equ $-letter

  ;newline
  newline db 0Ah
  newlineLen equ $-newline

  ;Name display
  nameDisplay db 'My name is:', 0Ah
  nameDisplayLen equ $-nameDisplay

  ;Name
  name times 4 db 'Stephen Wanyee', 0Ah
  nameLen equ $-name
