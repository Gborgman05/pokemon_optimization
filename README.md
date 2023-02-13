# pokemon_optimization
Scripts used to find the "best" pokemon team
Trying to solve the problem of a good pokemon team formulating in terms of constraint satisfaction where constraint is as follows:

1. 6 pokemon are allowed
2. Each pokemon can have up to 2 types
3. Each pokemon has to be a legitimate pokemon, i.e. even if a hypothetical type combo was needed, if no pokemon satified that it would be invalid
4. The team must have a super-effective type against all single-types in the entire game


## Conclusions

- fighting types are required as normal only weak to them
- fire types were expected to be seen, but actually not used in most teams
