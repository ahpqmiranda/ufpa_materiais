#=
julia_strings:
- Julia version: 
- Author: alana
- Date: 2022-10-20
=#
# strings are defined with double quotes
# like variables, strings can contain any unicode character
s1 = "The quick brown fox jumps over the lazy dog α,β,γ"
println(s1)
#> The quick brown fox jumps over the lazy dog α,β,γ

# println adds a new line to the end of output
# print can be used if you dont want that:
print("this")
#> this
print(" and")
#> and
print(" that.\n")
#> that.

# chars are defined with single quotes
c1 = 'a'
println(c1)
#> a
# the ascii value of a char can be found with Int():
println(c1, " ascii value = ", Int(c1))
#> a ascii value = 97
println("Int('α') == ", Int('α'))
#> Int('α') == 945

# so be aware that
println(Int('1') == 1)
#> false

# strings can be converted to upper case or lower case:
s1_caps = uppercase(s1)
s1_lower = lowercase(s1)
println(s1_caps, "\n", s1_lower)
#> THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG Α,Β,Γ
#> the quick brown fox jumps over the lazy dog α,β,γ

# sub strings can be indexed like arrays:
# (show prints the raw value)
show(s1[11]); println()
#> 'b'

# or sub strings can be created:
show(s1[1:10]); println()
#> "The quick "

# end is used for the end of the array or string
show(s1[end-10:end]); println()
#> "dog α,β,γ"

# julia allows string Interpolation:
a = "welcome"
b = "julia"
println("$a to $b.")
#> welcome to julia.

# this can extend to evaluate statements:
println("1 + 2 = $(1 + 2)")
#> 1 + 2 = 3

# strings can also be concatenated using the * operator
# using * instead of + isn't intuitive when you start with Julia,
# however people think it makes more sense
s2 = "this" * " and" * " that"
println(s2)
#> this and that

# as well as the string function
s3 = string("this", " and", " that")
println(s3)
#> this and that