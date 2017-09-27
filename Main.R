library(ggplot2)
library(gridExtra)
library(forecast)

setwd("C:/Users/Sii/Desktop/IDK/MachineLearningPy/HouseMovingContest")

#Data input
train_data = read.csv("train.csv", header = T, stringsAsFactors = F)
test_data = read.csv("test.csv", header = T, stringsAsFactors = F)
predict_data = read.csv("sample_submit.csv", header = F, stringsAsFactors = F)

#plot the train data
y_plot =
  ggplot()+
  geom_line(aes(x = 1:length(train_data$y), y = train_data$y))

client_plot =
  ggplot()+
  geom_line(aes(x = 1:length(train_data$client), y = train_data$client))

close_plot =
  ggplot()+
  geom_line(aes(x = 1:length(train_data$close), y = train_data$close))

price_am_plot =
  ggplot()+
  geom_line(aes(x = 1:length(train_data$price_am), y = train_data$price_am))

price_pm_plot =
  ggplot()+
  geom_line(aes(x = 1:length(train_data$price_pm), y = train_data$price_pm))

grid.arrange(y_plot, client_plot, close_plot)
grid.arrange(y_plot, price_am_plot, price_pm_plot)

#Regression analysis
y_lm = lm(y ~ price_am + price_pm, data = train_data)
y_lm_predict = test_data$price_am * y_lm$coefficients[2] + test_data$price_pm * y_lm$coefficients[3] + y_lm$coefficients[1]
predict_data$V2 = y_lm_predict

#Time series analysis
start_date = which(train_data$datetime == "2013-08-01")
y_ts = ts(train_data$y[start_date:2101], frequency = 365) #from 2011
y_decompose = decompose(y_ts)
#nomal test for the random element of time series data
ks.test(y_decompose$random, "pnorm")
#t test for the random element of time series data
t.test(y_decompose$random, mu = 0)
#ks.test(y_decompose$random, "pt", 1, 2)

y_trend = y_decompose$trend
y_seasonal = y_decompose$seasonal
y_random = y_decompose$random

cor(y_trend[which(y_trend != "NA")], train_data$price_pm[which(y_trend != "NA")])
cor(y_trend[which(y_trend != "NA")], train_data$price_am[which(y_trend != "NA")])
cor(y_seasonal[which(y_seasonal != "NA")], train_data$price_pm[which(y_seasonal != "NA")])

#lm & ts



#test
data_for_hw = y_ts
#data_for_hw = ts(data_for_hw[which(data_for_hw != 0)], frequency = 365)
#data_for_hw = ts(data_for_hw, frequency = 30)
y_predict_model = HoltWinters(data_for_hw, alpha = 0.01)
y_predict = forecast.HoltWinters(y_predict_model, h = 365)
#plot.forecast(y_predict)
predict_data$V2 = y_predict$mean

#Arima
data_for_arima = y_ts
y_arima_model = auto.arima(data_for_arima, max.p = 20, max.q = 20,seasonal = T)
y_predict = predict(y_arima_model, n.ahead =  365)
predict_data$V2 = y_predict$pred

#output result
ggplot()+
  geom_line(aes(x = 1:length(train_data$y), y = train_data$y), color = "blue")+
  geom_line(aes(x = (length(train_data$y) + 1):(length(train_data$y) + 365), y = predict_data$V2), color = "red")

write.table(predict_data, "submit_1.csv", row.names = F, col.names = F, quote = F, sep = ",")



