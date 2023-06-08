fifa_players = read.csv('Fifa_23_Players_Data.csv')
print(fifa_players)
# Basic scatter plot
x = fifa_players$Finishing
y = fifa_players$ST.Rating 
graphics.off()

plot(x, y, main = "Main title",
     xlab = "Finishing", ylab = "ST.Rating",
     pch = 19, frame = FALSE)
modelr = lm(y~x)
abline(modelr, col = "red")
summary(modelr)
cor(y,x)
position = table(fifa_players$Club.Position)
par(bg="yellow")
barplot(table(fifa_players$Club.Position),xlab = "position")
graphics.off()
RealMadrid = fifa_players[fifa_players$Club.Name == "Real Madrid CF",]
x = RealMadrid$Finishing
y = RealMadrid$ST.Rating
plot(x, y, main = "Main title",
     xlab = "overall", ylab = "Value.in.Euro.",
     pch = 19, frame = FALSE)
cor(x,y)
