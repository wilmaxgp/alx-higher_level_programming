#include "102-python.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int type;
    char *value;
} string;

void print_python_string(PyObject *p)
{
    string *str = (string *)p;

    printf("[.] string object info\n");

    if (str->type != 1)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("  type: compact ");
    if (str->value[0] & 0x80)
        printf("unicode object\n");
    else
        printf("ascii object\n");

    printf("  length: %d\n", str->type);
    printf("  value: %s\n", str->value);
}
