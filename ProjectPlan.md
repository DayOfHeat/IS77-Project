# Overview

The goal of this project is to analyze UK benefits fraud data along side UK labor data to observe any trends between the labor market and benefits fraud. We plan to compare labor statistics such as unemployment and pay levels over time with benefits fraud levels to in order to find out what economic conditions drive more fraud so we can propose potential solutions to reduce the fraud. We will be using official UK data from the DWP and ONS and analyze it with Python.

# Team

Josh - Fraud Detection Specialist

As a fraud detection specialist, Josh will be taking the lead on all work that is related to the UK benefits fraud dataset. Josh will be responsible for ensuring that the fraud data is correctly structured and ready to be analyzed as well as making sure to help integrate it with Michael’s economic data so that the two sources can be looked at side by side. Josh will also take charge of the exploratory analysis and work to identify patterns and correlations between fraud levels and economic conditions. Josh will also play a key role in wrapping up the project and combining the team’s collective work into one cohesive final report which will summarize the findings and provide potential avenues for future research.


Michael - Economic Specialist

As an economic specialist, Michael will be responsible for overseeing all aspects of the project when it comes to the UK labor market data. By taking this role, Michael will ensure that economic indicators such as unemployment rates and wage levels are accurately represented and are able to be clearly communicated during the analysis. Outside of the data itself, Michael will also be responsible for translating the team’s findings into meaningful and digestible visual/written outputs, creating the various charts and graphs which will help bring the data together, as well as presenting our team’s conclusions and the real world implications of the research. Michael’s work will serve to bridge the gap between the raw economic data and the findings/story of the team.

## Research Questions

The question we want to answer using our data is if levels of benefits fraud (in both absolute terms and as a percentage of benefits paid) correlates with poor economic conditions (high unemployment, low average wages, et cetera). Our theory is that a worse economy will drive more people into desperate conditions where they may engage in fraud. If it does, this could show the UK government that they need to either invest more in the DWP during times of economic hardship to stop the fraud or consider increasing benefits to reduce the pressure to commit fraud to survive. If we find no change or that there is more fraud during good economic times, this could be a sign that the fraud is more systemic and driven by personal gain rather than desperation. If this were the case, it could justify taking measures to reduce fraud, such as requiring more documentation to receive benefits, knowing that it probably isn't desperate families committing the fraud to survive.

# Datasets

The first data set we will be using is the Department for Work and Pensions (DWP)'s [Fraud and Error in the Benefit System](https://www.gov.uk/government/statistics/fraud-and-error-in-the-benefit-system-financial-year-2024-to-2025-estimates) data available on gov.uk in the form of an `.xslx` file. This is the official government data on benefits fraud and is available under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The over/under payment data is collected by taking a random sample of benefit claims. The claimant provides additional proof and then is assessed. The DWP then determines the cause of the discrepancy as fraud, claimant error, or official error. The sample is then used to estimate total over/under payments. The data set includes data from as far back at 2006 on over/underpayments broken down by client type (type of claim) as a percentage and number, comparative 2025 vs 2024 statistics broken down by demographics and by individual expenses, and net government loss from overpayment since 2010.

The second data set we will be using is UK Office of National Statistics (ONS)'s [Summary of Labour Market Statistics](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/summaryoflabourmarketstatistics). This is the official government data on the UK labor market and is also available under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The data is from the ONS's Labour Force Survey, taken monthly since 1998. It contains data on unemployment rates, economic inactivity rates, and average pay rates broken down by sector and age groups. It also features data on average hours works and has some comparative statistics to other European countries for 2025. 

The way these two data sets work together is through time. The benefits data time frame is fully contained within the labor data so, with some work, the two data sets can be synthesized together to follow trends.

# Timeline

- **Data formatting & cleaning**: Loading the data from each spreadsheet into Python and turning it into a well formatted, usable form like DataFrames. Responsibilities: Fraud Data: Josh, Labor Data: Michael

- **Data integration:** Combine data frames from each data set to each other by joining them over the time data column. May also require reformatting the time columns of each data set to be of the same granularity. Responsibility: Josh

- **Data analysis:** Perform exploratory data analysis to find trends in the fraud and labor data sets. Responsibility: Josh

- **Data visualization:** Create graphs and other visual to present the data nicely. Responsibility: Michael

- **Report findings:** Explain conclusions drawn from the data and the potential implications of them.  Responsibility: Michael

- **Finish report:** Produce the summary of our findings, describe future research, and other miscellaneous remaining portions of the report. Responsibility: Josh





# Constraints

One major challenge on this project will be converting the data onto a usable format. Both data sets are excel spreadsheets that are not formatted in a matter conducive to importing into Python. In addition to not being in a tidy data format, it also contains various one-off inconsistencies, such as the inclusion of the original and revised 2024 benefits data, which will require manual intervention. 

There are also some changes to how the data was collected throughout the time span of each data set. For the benefits data, the method for collecting the data changed in 2019 and how underpayments were classified changed in 2022, so each of these will need to be considered when drawing analysis. For the labor data, the data was re-weighted based on updated population estimates in 2024, which was applied retroactively to data from 2019 onward, but not earlier years due to "time constraints".

Another limitation of the data is that the benefits data only provides demographic data for 2024 and 2025. If we had access to the demographic data for all years, we could combine that with the economic demographic data to draw further analysis about economic trends and benefits fraud.

One constraint in terms of our data for the project is the lack of non-employment economic indicators. We don't have GDP or cost of living data which could allow us to make a better assessment of what good and bad economic times are.

# Gaps

One knowledge gap we have right now is the best way to make the data usable. Both data sets came in the form of excel spreadsheets, which, while perfectly easy to import into Python, will require a lot of manual work to get the data from, at least based on our current understanding. If there is an easier tool to use to get the data properly extracted and made usable by Python, it would be a massive time-saver for the project. 

Another gap is how to handle the changing in data collection methodologies throughout the data. Due to the nature of the analysis, we want to look at a long range of years, but the methodology changes will make that difficult. Worse, the changes are mostly in more recent years, which are naturally the most informative years to look if we want the data to be useful today. Any help in terms of how to handle these changes would be appreciated. Would it be better to only use years that have the same method, to use all years but qualify our conclusions, or to do separate analyses for each chunk of years that used a given method.

A final gap is that we couldn't find any information on when the interim status report and final project would be due, so we weren't able to assign specific dates to our timeline. 
