# SAS821S Lab 1 starter analysis script
# Complete the TODO sections. This file intentionally contains no answers.

library(readr)
library(dplyr)
library(ggplot2)
library(caret)

DATA <- "02_Data"
auth <- read_csv(file.path(DATA, "ot_authentication_logs.csv"), show_col_types = FALSE)
dns <- read_csv(file.path(DATA, "ot_dns_logs.csv"), show_col_types = FALSE)
firewall <- read_csv(file.path(DATA, "ot_firewall_logs.csv"), show_col_types = FALSE)
train <- read_csv(file.path(DATA, "ot_network_flow_training.csv"), show_col_types = FALSE)
investigation <- read_csv(file.path(DATA, "ot_network_flow_investigation.csv"), show_col_types = FALSE)

# TODO 1: convert timestamp fields to POSIXct and perform data-quality checks.
# TODO 2: descriptive statistics and at least three visualisations.
# TODO 3: correlate authentication, DNS and firewall logs into a timeline.

features <- c("dst_port", "duration_sec", "src_bytes", "dst_bytes", "packets",
              "connections_2s", "serror_rate", "rerror_rate", "same_srv_rate",
              "diff_srv_rate", "hour", "is_weekend")

set.seed(821)
index <- createDataPartition(train$label, p = 0.70, list = FALSE)
train_set <- train[index, ]
test_set <- train[-index, ]

model <- glm(label ~ ., data = train_set[, c(features, "label")], family = binomial())
prob <- predict(model, newdata = test_set[, features], type = "response")
pred <- ifelse(prob >= 0.5, 1, 0)
print(confusionMatrix(as.factor(pred), as.factor(test_set$label), positive = "1"))

# TODO 4: score the investigation data and export the ten most suspicious flows.
