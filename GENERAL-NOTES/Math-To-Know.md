
## Bitwise Shifting

    0   << 1    ===> 0 
    1   << 1    ===> 2
    2   << 1    ===> 4 
    3   << 1    ===> 6
    ....
    12  << 1    ===> 24
    13  << 1    ===> 26
    ....


    Number  << 1   ===> Number * 2      ----?  2^1
    Number  << 2   ===> Number * 4      ----?  2^2
    Number  << 3   ===> Number * 8      ----?  2^3
    Number  << 4   ===> Number * 16     ----?  2^4
    .....
    Number  << theNumberShifter   ==>  Number * ( 2^theNumberShifter)
    
    -------------------------------
    
