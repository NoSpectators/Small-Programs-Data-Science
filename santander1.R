#install.packages("R.utils")
#install.packages("arulesViz")
library("arulesViz")
library("arules")
library("R.utils")
library("boot")


#nL <- countLines("train_ver2.csv");nL
#lines <- 20000
#df <- read.csv("train_ver2.csv", header=F, skip = nL-lines)
#head(df);dim(df)
#train2 = write.csv(df,"train2.csv")
df2 <- read.csv("train2.csv")
df2 <- df2[,-1]
head(df2);dim(df2)
prod2 <- df2[,25:48]
head(prod2); dim(prod2)
View(prod2)

#write.csv(prod,"products.csv")
#write.csv(prod,"products2.csv")
n <- c('Savings Account','Guarantees','Current Accounts',
       'Derivada','Payroll Account','Junior', 'Mas Particular',
       'particular','particular Plus','Short-term deposits',
       'Medium-term deposits','Long-term deposits', 'e-account',
       'Funds', 'Mortgage','Pensions1','Loans','Taxes','Credit Card',
       'Securities','Home Account','Payroll', 'Pensions2','Direct Debit')
names(prod2) <- n
head(prod2,1)
#write.csv(prod2,"products3.csv")

transaction_data <- read.csv("santander3.csv",sep=",",header=F)
View(transaction_data)
#association rules/market basket analysis
#can't open as a csv because this file doesn't have lined up rows & cols
#so we need to use arules packages
#install.packages("arules")
#require(arules)
Bank2 <- read.transactions("santander3.csv",sep=",")
summary(Bank2)
#total number of cells in sparse matrix =
16785*16
#now multiply total cells by density
(16785*16)*(0.07491436)
#of the roughly 268,560 cells in sparse matrix, there are roughly
#20119 that are not empty (have a 1 in the cell)
#now we go a little deeper
inspect(Bank2[1:3])#inspect first 3 transactions
#look at the support
itemFrequency(Bank2[,1])
#the first item (Credit Card) alphabetically occurs < .02% of the transactions
#to put a number on it, .008459934 * 16785
.008459934*16785 #about 142 transactions
#now look at first 6 items alphabetically
itemFrequency(Bank2[,1:6])
#now look at a plot
itemFrequencyPlot(Bank2,support=.01)
#show top 5 items
itemFrequencyPlot(Bank2, topN=5)
itemFrequencyPlot(Bank2, topN=10)
#find confidence 
#confidence is a measure of the proportion of transactions where the presence of an item
#or a set of items results in the presence of another item or set of items
#example: if i buy items A, B, how likely is it I buy item C?
m1 <- apriori(Bank2)#this yields no rules b/c the default minimums too stringent (.1 for support, .8 for confidence)
m1 <- apriori(Bank2,parameter=list(support=0.003,confidence=0.9,minlen=2))
m1
summary(m1)
inspect(m1[1:2])#look at first 2

#lift is how much more likely an item is to be purchased
#with another item than by itself
#let's sort the rules
inspect(sort(m1,by="lift")[1:4])#top 4 rules by lift
inspect(sort(m1,by="lift")[4:10])#4 thru 10 rules by lift
inspect(sort(m1,by="lift")[1:10]) #top 10 rules by lift
inspect(sort(m1,by="lift")[1:length(m1)])

#subsetting--looking for specific items in rules
e_account_rules <- subset(m1, items %in% "e-account")
inspect(e_account_rules)

#visualizations
plot(m1)#scatterplot

#interactive
plot(m1, measure=c("support", "lift"), shading="confidence", interactive=TRUE)

#matrix-based visualizations
m1_matrix <- m1[quality(m1)$confidence > 0.8]

#plot of matrix visualization
plot(m1_matrix, method="matrix", measure="lift")

#reorder rows and columns such that rules with similar values of interest measure are presented closer together
plot(m1_matrix, method="matrix", measure="lift", control=list(reorder=TRUE))

#use 3d bars instead of rectangles
plot(m1_matrix, method="matrix3D", measure="lift")

#reorder rows and columns such that rules with similar values of interest measure are presented closer together
plot(m1_matrix, method="matrix3D", measure="lift", control=list(reorder=TRUE))

#use color hue
plot(m1_matrix, method="matrix", measure=c("lift", "confidence"))

#reorder again
plot(m1_matrix, method="matrix", measure=c("lift", "confidence"),
      control=list(reorder=TRUE))
#grouped rules
plot(m1_matrix, method="grouped") #all of them

#grouped, reordered
plot(m1_matrix, method="grouped", control=list(k=5)) #only 5 rules

#interactive version of grouped, reordered
plot(m1_matrix, method="grouped", interactive=TRUE)

#graph based visualization
plot(m1, method="graph")


#graph of itemsets
plot(m1, method="graph", control=list(type="itemsets"))

#parallel coordinates plot
plot(m1, method="paracoord")

