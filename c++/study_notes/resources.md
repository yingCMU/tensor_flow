1. [google c++ style](https://google.github.io/styleguide/cppguide.html#Namespaces)

## concepts
1. memory access
Python does not pass primitives as references. As a result, adder receives a copy of i and i remains unchanged outside the function.

To be fair, the way Python handles arguments is perfectly reasonable. But what's happening behind the scenes is not perfectly obvious from the syntax alone.

C++, on the other hand, makes you decide how you'd like to treat function arguments. It also gives you control over how you'd like to access objects in memory, whether that's by simply referring to their address in memory or by their actual value.

## common reference:
1. #ifndef Directive
it allows for conditional compilation. The preprocessor determines if the provided macro does not exist before including the subsequent code in the compilation process.
`#ifndef macro_definition`
The #ifndef directive must be closed by an #endif directive.
2. class header file: http://www.cppforschool.com/tutorial/separate-header-and-implementation-files.html
3. pointers
&: every memory location has its address defined which can be accessed using ampersand (&) operator which denotes an address in memory:
`int  var1; cout << &var1 << endl;`
A pointer is a variable whose value is the address of another variable.  Like any variable or constant, you must declare a pointer before you can work with it. The general form of a pointer variable declaration is −
`type *var-name;`
```
int  *ip;        // pointer variable
ip = &var;       // store address of var in pointer variable
cout << *ip << endl;
```
4. [Function Reference Parameters](http://www.fredosaurus.com/notes-cpp/functions/refparams.html)
[The call by reference method](https://www.tutorialspoint.com/cplusplus/cpp_function_call_by_reference.htm)
Reference parameters are useful in two cases:
Change values. Use a reference parameter when you need to change the value of an actual parameter variable in the call. When a function computes only one value it is considered a better style to return the value with the return statement. However, if a function produces more than one value, it is common to use reference parameters to return values, or a combination of the return value and reference parameters.
Efficiency. To pass large structures more efficiently. This is especially common for passing structs or class objects. If no changes are made to the parameter, it is should be declared const.
Reference parameters pass an address, not a value
When you declare a reference parameter, the function call will pass the memory address of where the actual parameter, instead of copying the parameter value into the formal parameter.
Declare reference parameters with a &
To indicate a reference parameter, an ampersand (&) is written in the function prototype and header after the parameter type name. For example,
void assign(int& to, int from) {
    to = from;  // Will change the actual parameter in the call.
}
has two parameters, to is a reference parameter as indicated by the ampersand, and from is a value parameter. This ampersand must be in both the prototype and the function header.
Example - Swap (bad solution)
Let's say you want to exchange the values in two arguments.
int a = 5;
int b = 10;

swap(a,b);
// If we want a=10 and b=5 as the result, how do we write the function?
Here's an example that does NOT work correctly, altho there is no error message.
```
void swap(int x, int y) {  // BAD BAD BAD BAD BAD BAD BAD
    int temp = x; // temp is a local variable
    x = y;        // changes only local copy
    y = temp;     // changes only local copy
}
```
Because x and y are value parameters, like local variables, changes to them have no effect on the calling functions arguments a and b.

## To do:
1. header filer usage and why
