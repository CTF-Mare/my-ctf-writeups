__int64 __fastcall re_open_port(signed int a1)
{
  __int64 result; // rax@16
  __int64 v2; // rbx@16
  int optval; // [sp+1Ch] [bp-54h]@7
  socklen_t addr_len; // [sp+20h] [bp-50h]@13
  unsigned int v5; // [sp+24h] [bp-4Ch]@1
  int fd; // [sp+28h] [bp-48h]@4
  int v7; // [sp+2Ch] [bp-44h]@13
  __int16 s; // [sp+30h] [bp-40h]@7
  uint16_t v9; // [sp+32h] [bp-3Eh]@7
  int v10; // [sp+34h] [bp-3Ch]@7
  struct sockaddr addr; // [sp+40h] [bp-30h]@13
  __int64 v12; // [sp+58h] [bp-18h]@1

  v12 = *MK_FP(__FS__, 40LL);
  v5 = calc_port(dword_602100[a1 + 1], a1 + 1);
  if ( a1 > 3 )
  {
    puts("FATAL ERROR bad knock number");
    exit(1);
  }
  fd = socket(2, 1, 0);
  if ( fd < 0 )
  {
    puts("FATAL ERROR opening new socket failed!");
    exit(1);
  }
  bzero(&s, 0x10uLL);
  s = 2;
  v10 = htons(0);
  v9 = htons(v5);
  optval = 1;
  setsockopt(fd, 1, 2, &optval, 4u);
  if ( bind(fd, (const struct sockaddr *)&s, 0x10u) )
  {
    printf("Server Bind Port %d Failed!\n", v5);
    exit(1);
  }
  if ( listen(fd, 5) )
  {
    puts("Server Listen Failed!");
    exit(1);
  }
  addr_len = 16;
  v7 = accept(fd, &addr, &addr_len);
  close(fd);
  if ( v7 < 0 )
  {
    puts("FATAL ERROR on accept");
    exit(1);
  }
  result = (unsigned int)v7;
  v2 = *MK_FP(__FS__, 40LL) ^ v12;
  return result;
}
