#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);
    printf("  first 10 bytes:");

    for (i = 0; i < size && i < 10; i++)
    {
        printf(" %02x", (unsigned char)string[i]);
    }

    printf("\n");
    fflush(stdout);
}

/**
 * print_python_list - Prints info about Python lists
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        return;
    }

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
    }

    fflush(stdout);
}


