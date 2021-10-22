# The required packages
packages = c("BradleyTerry2", "qvcalc", "readxl")

# check package if loaded, if not, install and load
package.check <- lapply(
  packages,
  FUN = function(x) {
    if (!require(x, character.only = TRUE)) {
      install.packages(x, dependencies = TRUE)
      library(x, character.only = TRUE)
    }
  }
)

# reading the data from BT_ranking.xlsx, which is already the format fitting to Bradley_Terry Model.
BT_ranking <- read_excel("./data/BT_ranking.xlsx")

# The data of player1 and player2 in the BT_ranking are converted into a form suitable for BTm analysis.
# And cbind these 2 columns with BT_ranking data
BT_ranking$p1 <- factor(BT_ranking$player1, levels=unique(c(BT_ranking$player1, BT_ranking$player2))) 
BT_ranking$p2 <- factor(BT_ranking$player2, levels=unique(c(BT_ranking$player1, BT_ranking$player2))) 

# Compute the standard Bradley-Terry model.
btmodel<- BTm(cbind(win1,win2),player1 = p1,player2 = p2,id="player_",data=BT_ranking)
summary(btmodel)

# We have some biased estimations because of extreme situations, so we apply the update function to reduce the effect of bias.
bt_update<-update(btmodel,br=TRUE)

# Estimating the latent scores of each player.
bt_abi<-BTabilities(bt_update)
# Taking the exponential form of the latent scores for standardization.
bt_odds<-exp(bt_abi[,"ability"])
bt_odds[order(bt_odds)]

# Computing a table to summarize the revised latent scores and standard errors.
bt<-cbind(bt_odds,bt_abi[,"s.e."])
colnames(bt)<-c("ability","s.e.")
write.table (bt, file ="./result/rankinglist.csv", sep =",", row.names =TRUE, col.names = TRUE, quote =TRUE)

# Computing a figure showing intervals of latent scores basd on quasi standard errors
bt.qv<-qvcalc(bt_abi)
plot(bt.qv)
