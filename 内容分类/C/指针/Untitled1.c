#include <stdio.h>
void main(void){
    int *p1, *p2;
    int a, b, c;
    a = 3;
    b = 5;
    c = 7;
    p1 = &c;
    p2 = &a;
    printf("a��%d��b��%d, c��%d\n", a, b, c);
    printf("&a��%x��&b��%x, &c��%x\n", &a, &b, &c);
    printf("*p1��%d��*p2��%d\n", *p1, *p2);
    printf("&p1��%x��&p2��%x\n", &p1, &p2);
    printf("p1��%x��p2��%x\n", p1, p2);
}
