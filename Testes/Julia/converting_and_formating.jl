#=
converting_and_formating:
- Julia version: 
- Author: alana
- Date: 2022-10-20
=#
# strings can be converted using float and int:
e_str1 = "2.718"
e = parse(Float64, e_str1)
println(5e)
#> 13.59
num_15 = parse(Int, "15")
println(3num_15)
#> 45

# numbers can be converted to strings and formatted using printf
using Printf
@printf "e = %0.2f\n" e
#> e = 2.72
# or to create another string sprintf
e_str2 = @sprintf("%0.3f", e)

# to show that the 2 strings are the same
println("e_str1 == e_str2: $(e_str1 == e_str2)")
#> e_str1 == e_str2: true

# available number format characters are f, e, a, g, c, s, p, d:
# (pi is a predefined constant; however, since its type is
# "MathConst" it has to be converted to a float to be formatted)
@printf "fix trailing precision: %0.3f\n" float(pi)
#> fix trailing precision: 3.142
@printf "scientific form: %0.6e\n" 1000pi
#> scientific form: 3.141593e+03
@printf "float in hexadecimal format: %a\n" 0xff
#> float in hexadecimal format: 0xf.fp+4
@printf "fix trailing precision: %g\n" pi*1e8
#> fix trailing precision: 3.14159e+08
@printf "a character: %c\n" 'α'
#> a character: α
@printf "a string: %s\n" "look I'm a string!"
#> a string: look I'm a string!
@printf "right justify a string: %50s\n" "width 50, text right justified!"
#> right justify a string:                    width 50, text right justified!
@printf "a pointer: %p\n" 100000000
#> a pointer: 0x0000000005f5e100
@printf "print an integer: %d\n" 1e10
#> print an integer: 10000000000