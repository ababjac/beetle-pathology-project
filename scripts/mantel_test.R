library(ape)
#help("mantel.test")

DIR <- "/home/ababjac/School/UTK/Grad/Research/beetle-pathology-project/data/imputed/"
OUT <- file("/home/ababjac/School/UTK/Grad/Research/beetle-pathology-project/data/mantel-results-fillKNN-asymmetric.txt")
OMIT <- c(8, 19, 23, 24, 25, 31, 36, 41, 44, 45, 46, 47, 52)


output <- c()
for(i in 1:55){
  if(i %in% OMIT) {
    next
  }
  
  if(i < 10){
    count <- paste("0", toString(i), sep='')
  }
  else{
    count <- toString(i)
  }
  
  filename <- paste(DIR, "GM", count, sep='')
  
  path = read.csv(paste(filename, "-path.txt", sep=''))
  tree = read.csv((paste(filename, "-tree.txt", sep='')))
  
  diag(path) <- diag(tree) <- 0
  
  t <- mantel.test(path, tree)
}

writeLines(output, OUT)
close(OUT)
