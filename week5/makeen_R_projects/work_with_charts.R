sample_b = c(1,2,3,4,5,6,7,8)
sample_a = c(1,4,4,4,5,5,5,8)
boxplot(sample_a,sample_b,col = c(5,7),horizontal = TRUE,names = c('sampleA','sampleB'))
par(mfrow = c(1,2))
hist(sample_a)
boxplot(sample_a,sample_b,col = c(5,7),horizontal = TRUE,names = c('sampleA','sampleB'))

