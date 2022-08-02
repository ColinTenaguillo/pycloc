#include <stdio.h>
/*
This is a multi-line comment
The blanks in multi-line comment are counted as Blanks

// Test single line comment in multiline comment, should not be counted twice.
*/

int main() {
    /// This is a comment line
    printf ("Hello, world!"); // Code+Comment line together counted as Code.
    return 0;
}