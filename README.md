we want to find the global maximum of { F(x) = x^2 + 2x }  function in range [0,30] in this problem

the desired solution is using genetics algorithm is as follows :
  First, select a random population from the desired interval and then continue the algorithm until the termination condition is reached.
  
  
this algorithm includes implementation of separate methods for random generation of the initial population (by obtaining the population size), selection of parents and selection of survivors according to fitness, mutation and recombination in single-point, two-point and uniform methods.


this algorithm receives program parameters including population size, mutation probability, recombination probability, recombination type and the maximum number of loop repetitions (as a termination condition) in an input file, respectively, in separate lines.
