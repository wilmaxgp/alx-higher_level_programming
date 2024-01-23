#include <main.h>

/**
 * print_python_list - prints information about Python lists
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element))
            print_python_bytes(element);
        else if (PyFloat_Check(element))
            print_python_float(element);
    }
}

/**
 * print_python_bytes - prints information about Python bytes
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
    for (i = 0; i < size + 1 && i < 10; ++i)
        printf(" %02x", str[i]);
    printf("\n");
}

/**
 * print_python_float - prints information about Python float
 * @p: PyObject pointer to a Python float object
 */
void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
