#include <stdio.h>
void main(void){
    int *p1, *p2;
    int a, b, c;
    a = 3;
    b = 5;
    c = 7;
    p1 = &c;
    p2 = &a;
    printf("a是%d，b是%d, c是%d\n", a, b, c);
    printf("&a是%x，&b是%x, &c是%x\n", &a, &b, &c);
    printf("*p1是%d，*p2是%d\n", *p1, *p2);
    printf("&p1是%x，&p2是%x\n", &p1, &p2);
    printf("p1是%x，p2是%x\n", p1, p2);
}
