__int64 __fastcall client_handle(int a1)
{
  __int64 v1; // rbx@1
  char *v2; // rax@1
  __int64 v3; // rbx@12
  char *v4; // rax@12
  __int64 result; // rax@16
  __int64 v6; // rbx@16
  int fd; // [sp+Ch] [bp-74h]@1
  char v8; // [sp+1Bh] [bp-65h]@12
  int buf; // [sp+1Ch] [bp-64h]@2
  int v10; // [sp+20h] [bp-60h]@1
  socklen_t len; // [sp+24h] [bp-5Ch]@1
  socklen_t v12; // [sp+28h] [bp-58h]@12
  int i; // [sp+2Ch] [bp-54h]@1
  unsigned int v14; // [sp+30h] [bp-50h]@14
  int v15; // [sp+34h] [bp-4Ch]@2
  int v16; // [sp+38h] [bp-48h]@5
  int v17; // [sp+3Ch] [bp-44h]@8
  struct sockaddr addr; // [sp+40h] [bp-40h]@1
  struct sockaddr v19; // [sp+50h] [bp-30h]@12
  __int64 v20; // [sp+68h] [bp-18h]@1

  fd = a1;
  v20 = *MK_FP(__FS__, 40LL);
  v10 = 0;
  len = 16;
  getpeername(a1, &addr, &len);
  v1 = ntohs(*(uint16_t *)&addr.sa_data[0]);
  v2 = inet_ntoa(*(struct in_addr *)&addr.sa_data[2]);
  printf("portknockd:get client from:(%s,%d)\n", v2, (unsigned int)v1);
  for ( i = 0; i <= 4; ++i )
  {
    buf = read_urandom();
    v15 = write(fd, &buf, 4uLL);
    if ( v15 != 4 )
    {
      puts("Failed writing to socket");
      close(fd);
      exit(1);
    }
    v16 = read(fd, &v10, 4uLL);
    if ( v16 != 4 )
    {
      puts("Failed reading from socket");
      puts("the length of recv data is not 4bytes!close the socket");
      close(fd);
      exit(1);
    }
    v17 = calc_something(buf, i);
    if ( v17 != v10 )
    {
      puts("wrong data!close the socket");
      close(fd);
      exit(1);
    }
    if ( i == 4 )
    {
      read_flag(fd, &v8, 128);
      v12 = 16;
      getpeername(fd, &v19, &v12);
      v3 = ntohs(*(uint16_t *)&v19.sa_data[0]);
      v4 = inet_ntoa(*(struct in_addr *)&v19.sa_data[2]);
      printf("have send flag to:(%s,%d) close the socket \n", v4, (unsigned int)v3);
      close(fd);
      exit(1);
    }
    close(fd);
    v14 = re_open_port(i);
    fd = v14;
  }
  result = v14;
  v6 = *MK_FP(__FS__, 40LL) ^ v20;
  return result;
}
