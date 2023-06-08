set.seed(123)
var1 = rnorm(100,50,2.5)
var1[3] = var1[3]+20
var1[50] = var1[50]-20
boxplot(var1[-c(3,50)], horizontal = TRUE, col = "green" , outline = FALSE)
?boxplot
fivenum(var1)
summary(var1)
 
