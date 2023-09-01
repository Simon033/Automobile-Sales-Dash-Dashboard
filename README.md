# Visualization Dashboard using Dash for Automobile Sales
Created a dashboard using Dash to visualize Automobile Sales data during recession periods, and non recession period.

### Objective
The objective was to analyze the historical trends in automobile sales during recession periods, and non recession period. The goal is to provide insights into how the sales of XYZAutomotives, a company specializing in automotive sales, were affected during times of recession.

My personal goal was to understand recession periods better and also demonstrate my dashboarding skills.

## The dashboard is created using `Plotly` and `Dash`. 

### Components of the report items
The dashboard mainly represents two main reports:-
- Yearly Automobile Sales Statistics
- Regression Period Statistics

##### Yearly Automobile Sales Statistics
- Yearly Average Automobile sales using line chart for the whole period.
For the chosen year provide,
- Total Monthly Automobile sales using line chart.
- Average Monthly Automobile sales of each vehicle type using bar chart.
- Total Advertisement Expenditure for each vehicle using pie chart

##### Recession Period Statistics
- Average Automobile sales using line chart for the Recession Period using line chart.
- Average number of vehicles sold by vehicle type using bar chart
- Total expenditure share by vehicle type during recession usssing pie chart
- Effect of unemployment rate on vehicle type and sales using bar chart

### Dataset
**Data :** [historical_automobile_sales.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv)

#### Dataset Variables for your reference
The dataset includes the following variables
- Date: The date of the observation.
- Recession: A binary variable indicating recession perion; 1 means it was recession, 0 means it was normal.
- Automobile_Sales: The number of vehicles sold during the period.
- GDP: The per capita GDP value in USD.
- Unemployment_Rate: The monthly unemployment rate.
- Consumer_Confidence: A synthetic index representing consumer confidence, which can impact consumer spending and automobile purchases.
- Seasonality_Weight: The weight representing the seasonality effect on automobile sales during the period.
- Price: The average vehicle price during the period.
- Advertising_Expenditure: The advertising expenditure of the company.
- Vehicle_Type: The type of vehicles sold; Supperminicar, Smallfamiliycar, Mediumfamilycar, Executivecar, Sports.
- Competition: The measure of competition in the market, such as the number of competitors or market share of major manufacturers.
- Month: Month of the observation extracted from Date.
- Year: Year of the observation extracted from Date.

### Insigts Gained
- Sales Decline: During a recession, there is indeed a noticeable decline in overall automobile sales. This can be attributed to reduced consumer confidence, economic uncertainty, and tighter budgets.
- Vehicle Types: he analysis reveals significant variations in the sales of different vehicle types. Notably, sales of 'Sports' and 'Executive' cars experience a substantial decline during recession periods. In contrast, 'medium family cars' and 'small cars' exhibit more resilience, likely due to their affordability and practicality.
- Promotions and Incentives: An interesting finding is the shift in advertising strategies during recession periods. To maintain sales, automakers tend to emphasize the promotion of cheaper and more economical car models, catering to the budget-conscious consumers. In contrast, during non-recession periods, there's a greater focus on marketing luxury and sports cars, aligning with consumer preferences for more extravagant purchases.
- Consumer Behavior: During economic downturns, consumers tend to prioritize practicality, fuel efficiency, and reliability when making automotive choices, contributing to the observed trends.

### Conclusion
This project has not only provided valuable insights into recessionary trends in automobile sales but has also been a significant learning journey in harnessing the capabilities of Dash for data visualization. Dash's versatility in creating interactive and dynamic dashboards has allowed me to effectively convey complex data in an engaging manner.

Through this project, I've gained proficiency in Dash, mastering the art of creating interactive plots and charts, handling user interactions, and designing visually appealing dashboards. The experience of working with Dash has deepened my technical skills and broadened my understanding of how to leverage data visualization as a powerful tool for storytelling.

