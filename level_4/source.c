#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *a = "A";
char *b = "B";
char *c = "C";
char *d = "D";
char *e = "E";
char *f = "F";
char *g = "G";
char *h = "H";
char *i = "I";
char *j = "J";
char *k = "K";
char *l = "L";
char *m = "M";
char *n = "N";
char *o = "O";
char *p = "P";
char *q = "Q";
char *r = "R";
char *s = "S";
char *t = "T";
char *u = "U";
char *v = "V";
char *w = "W";
char *x = "X";
char *y = "Y";
char *z = "Z";
char *uu = "_";

int main () {
  srand(time(NULL));
  int r = rand() % 100000;

  puts("Guess a number:");

  int n;
  scanf ("%d",&n);

  if(r == n) {
    char out[16];
    strcpy(out, y);
    strcat(out, o);
    strcat(out, u);
    strcat(out, uu);
    strcat(out, m);
    strcat(out, a);
    strcat(out, d);
    strcat(out, e);
    strcat(out, uu);
    strcat(out, i);
    strcat(out, t);
    puts(out);
  }

  return 0;
}
