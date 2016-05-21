#include <cstdio>
#include <cstring>

char str[505], gao[505];

int main(){
	scanf("%s", str);
	for(int i = 0; i < 128; ++i)
		if(i > 47 && i <= 96) gao[i + 53] = i;
		else if(i <= 46) gao[i + i % 11] = i;
		else gao[i - i % 61] = i;
	for(int i = 0; i < strlen(str); ++i)
		printf("%c", gao[str[i]]);
	
	puts("");
}
