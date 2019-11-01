addition:
  add ebx, [eax]
  add eax, 1
  loop addition

  or ebx, 30h ; convert to ASCII
  mov [sum], ebx
  ret