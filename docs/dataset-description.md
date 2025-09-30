# Student Performance and Alcoholism Dataset

## Overview

The file student-lpor.csv contains data from a research study conducted by Fabio Pagnotta and Hossain Mohammad Amran, Università Di Camerino – UNICAM. This research was carried out with high school students and includes numerous social and gender-related variables, as well as grades in the Portuguese Language subject.

## Research Objective

The study aims to introduce a new variable that classifies students as alcoholic or not, and identify which variables are predictors of this new response variable.

## Context

The data was obtained from a survey conducted with high school students, providing extensive social and gender information, as well as grades in the Portuguese Language subject.

## Source Information

- **Authors**: P. Cortez and A. Silva
- **Publication**: "Using Data Mining to Predict the Performance of High School Students"
- **Conference**: Proceedings of 5th Future Business Technology Conference (FUBUTEC 2008)
- **Details**: pp. 5-12, Porto, Portugal, April 2008, EUROSIS
- **ISBN**: 978-9077381-39-7
- **Research Team**: Fabio Pagnotta, Hossain Mohammad Amran (Università Di Camerino - UNICAM)

## Variable Descriptions

| Variable   | Description                     | Type        | Values                                          |
| ---------- | ------------------------------- | ----------- | ----------------------------------------------- |
| school     | Student's school                | Binary      | GP - Gabriel Pereira, MS - Mousinho da Silveira |
| sex        | Student's gender                | Binary      | F - female, M - male                            |
| age        | Student's age                   | Numeric     | 15 to 22                                        |
| address    | Type of home address            | Binary      | U - urban, R - rural                            |
| famsize    | Family size                     | Binary      | LE3 - ≤3, GT3 - >3                              |
| Pstatus    | Parents' cohabitation status    | Binary      | T - living together, A - apart                  |
| Medu       | Mother's education level        | Categorical | 0 - none to 4 - higher education                |
| Fedu       | Father's education level        | Categorical | 0 - none to 4 - higher education                |
| Mjob       | Mother's job                    | Nominal     | teacher, health, services, at_home, other       |
| Fjob       | Father's job                    | Nominal     | teacher, health, services, at_home, other       |
| reason     | Reason for choosing school      | Nominal     | home, reputation, course, other                 |
| guardian   | Student's guardian              | Nominal     | mother, father, other                           |
| traveltime | Home-to-school travel time      | Interval    | 1 (<15 min) to 4 (>1 hour)                      |
| studytime  | Weekly study time               | Interval    | 1 (<2 hrs) to 4 (>10 hrs)                       |
| schoolsup  | Extra educational support       | Binary      | yes, no                                         |
| famsup     | Family educational support      | Binary      | yes, no                                         |
| paid       | Private lessons                 | Binary      | yes, no                                         |
| activities | Extracurricular activities      | Binary      | yes, no                                         |
| nursery    | Attended preschool              | Binary      | yes, no                                         |
| higher     | Wants higher education          | Binary      | yes, no                                         |
| internet   | Internet access at home         | Binary      | yes, no                                         |
| romantic   | In romantic relationship        | Binary      | yes, no                                         |
| famrel     | Quality of family relationships | Categorical | 1 (very bad) to 5 (excellent)                   |
| freetime   | Free time after school          | Categorical | 1 (very low) to 5 (very high)                   |
| goout      | Time spent with friends         | Categorical | 1 (very low) to 5 (very high)                   |
| Dalc       | Weekday alcohol consumption     | Categorical | 1 (very low) to 5 (very high)                   |
| Walc       | Weekend alcohol consumption     | Categorical | 1 (very low) to 5 (very high)                   |
| health     | Current health status           | Categorical | 1 (very bad) to 5 (very good)                   |
| absences   | Number of school absences       | Numeric     | 0 to 93                                         |

## Academic Performance Variables

| Variable | Description           | Type    | Range   |
| -------- | --------------------- | ------- | ------- |
| G1       | First semester grade  | Numeric | 0 to 20 |
| G2       | Second semester grade | Numeric | 0 to 20 |
