model <- c("Logistic","Naive Bayes", "RF","XGBoost","CNN","LSTM")
Accuracies <- c(63.83,54.03,55.33, 36.37, 58.04, 60.84)
avg_accuracy_model <- as.data.frame(cbind(model, Accuracies))
ggplot(avg_accuracy_model, aes(model, Accuracies)) + geom_bar(stat="identity")


category <- c("Politics","Sports","Technology","Entertainment" )

accuracy <- data.frame(t(cbind(rbind(rep("Logistic",4),category),
                   rbind(rep("Naive Bayes",4),category),
                   rbind(rep("RF",4),category),
                   rbind(rep("XGBoost",4),category))))

accuracy$acc <- c(74,50,77,52,60,57,63,34,61,44,51,66,47,28.99,41,27)

ggplot(accuracy, aes(fill=category, y=acc, x=V1)) + 
  geom_bar(position="dodge", stat="identity")

