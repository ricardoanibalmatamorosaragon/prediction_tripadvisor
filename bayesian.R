setwd("C:/Users/ricar/OneDrive/Desktop/prediction_tripadvisor")
library(caret)
library(bnlearn)
library(readr)
#ult_views <- read_csv("csv/ult_views.csv")
ult_views <- read_csv("csv/ult_views_sentimental.csv")
sub.dataset=subset(ult_views, select =c("value","room","location","clean","check","service","target"))
set.seed(3033)
intrain <- createDataPartition(y = sub.dataset$target, p= 1, list =FALSE)
trainset <- sub.dataset[intrain,]
trainset[["target"]] = factor(trainset[["target"]])
trainset[["value"]] = factor(trainset[["value"]])
trainset[["room"]] = factor(trainset[["room"]])
trainset[["location"]] = factor(trainset[["location"]])
trainset[["clean"]] = factor(trainset[["clean"]])
trainset[["check"]] = factor(trainset[["check"]])
trainset[["service"]] = factor(trainset[["service"]])
#trainset[["business"]] = factor(trainset[["business"]])

set.seed(3033)
bn_df <- data.frame(trainset)

res <- hc(bn_df)

plot(res)
fittedbn <- bn.fit(res, data = bn_df)
print(fittedbn$target)

test_evidence <- read_csv("csv/test_not_target.csv")
value <- test_evidence['value']
room <- test_evidence['room']
location <- test_evidence['location']
clean <- test_evidence['clean']
check <- test_evidence['check']
service <- test_evidence['service']
value_list <- value[[1]]
room_list <- room[[1]]
location_list <- location[[1]]
clean_list <- clean[[1]]
check_list <- check[[1]]
service_list <- service[[1]]

lista <- vector("list", 14162)
probs <- vector("list",14162)
#index
i <- 1
for(item in clean_list){
  result <- cpquery(fittedbn, event = (target=="good"), evidence = ( value==value_list[i] & room==room_list[i] & 
    location==location_list[i] & clean ==clean_list[i] & check ==check_list[i] & service==service_list[i]) )
  probs[[i]] <- result
  if(result < 1-result){
    lista[[i]] <- 'bad'
  }else{
    lista[[i]] <- 'good'
  }
  
  i <- i +1
}
test_evidence$target <- unlist(lista)
test_evidence$target <- as.factor(test_evidence$target)

test_evidence$probGood <- unlist(probs)
test_evidence$probGood <- as.factor(test_evidence$probGood)
write.csv(test_evidence,'./csv/views_target_r_sentiment.csv',row.names = FALSE)


