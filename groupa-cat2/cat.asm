;Print and display macro
%macro print_and_display 4
  mov eax, %1
  mov ebx, %2
  mov ecx, %3
  mov edx, %4
  int 80h
%endmacro


section .text
  global _start
  _start:

  print_and_display 4, 1, msgInput, msgInputLen

  loop to populate x
  populate:
    print_and_display 3, 0, userInput,1

  ;find largest element in x
  mov ecx, 3 ;length of array
  mov eax, x ; x is eax
  mov ebx, [eax] ;first element
  add eax, 1 ;go to next
  dec ecx ; decrement counter

  findLargest:
  cmp [eax], ebx
  JLE continue
  mov ebx, [eax]

  continue:
  add eax, 1 ;go to next
  loop findLargest

  done:
  add ebx, '0'
  mov [largest], ebx
  print_and_display 4,1,msgLargest,msgLargestLen
  print_and_display 4,1,largest,1




  print_and_display 4,1,newLine,1
  ;exit
  mov eax, 1
  int 80h

section .data
  x db 1,2,3
  msgInput db "Enter a number: ",0Ah
  msgInputLen equ $-msgInput

  msgLargest db "The largest number is: ",0Ah
  msgLargestLen equ $-msgLargest

  newLine db 10

section .bss
  userInput resb 1
  largest resb 2