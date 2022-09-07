library(permanova)
path <- "/home/ababjac/School/UTK/Grad/Research/beetle-pathology-project/data/"
wtb <- read.csv(paste(path, "wtb-dist-noheaders.csv", sep=""), header=FALSE)
wtb_labels <- read.csv(paste(path, "wtb-labels-noheaders.csv", sep=""), header=FALSE)
wtb_labels <- as.factor(wtb_labels)

wtb_p <- PERMANOVA::PERMANOVA(wtb, wtb_labels)

