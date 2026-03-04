# Overview

The goal of this project is to analyze UK benefits fraud data along side UK labor data to observe any trends between the labor market and benefits fraud. We plan to compare labor statistics such as unemployment and pay levels over time with benefits fraud levels. [Expand]

# Team

Josh will be in charge of [X,Y,Z]

Michael will be in charge of [A,B,C]

## Research Questions







# Datasets

The first data set we will be using is the Department for Work and Pensions (DWP)'s [Fraud and Error in the Benefit System](https://www.gov.uk/government/statistics/fraud-and-error-in-the-benefit-system-financial-year-2024-to-2025-estimates) data available on gov.uk in the form of an `.xslx` file. This is the official government data on benefits fraud and is available under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The over/under payment data is collected by taking a random sample of benefit claims. The claimant provides additional proof and then is assessed. The DWP then determines the cause of the discrepancy as fraud, claimant error, or official error. The sample is then used to estimate total over/under payments. The data set includes data from as far back at 2006 on over/underpayments broken down by client type (type of claim) as a percentage and number, comparative 2025 vs 2024 statistics broken down by demographics and by individual expenses, and net government loss from overpayment since 2010.

The second data set we will be using is UK Office of National Statistics (ONS)'s [Summary of Labour Market Statistics](https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/datasets/summaryoflabourmarketstatistics). This is the official government data on the UK labor market and is also  available under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). The data is from the ONS's Labour Force Survey, taken monthly since 1998. It contains data on unemployment rates, economic inactivity rates, and average pay rates broken down by sector and age groups. It also features data on average hours works and has some comparative statistics to other European countries for 2025.  

The way these two data sets work together is through time. The benefits data time frame is fully contained within the labor data so, with some work, the two data sets can be synthesized together to follow trends.

# Timeline





# Constraints

One major challenge on this project will be converting the data onto a useable format. Both data sets are excel spreadsheets that are not formatted in a matter conducive to importing into Python. In addition to not being in a tidy data format, it also contains various one-off inconsistencies, such as the inclusion of the original and revised 2024 benefits data, which will require manual intervention. 

There are also some changes to how the data was collected throughout the time span of each data set. For the benefits data, the method for collecting the data changed in 2019 and how underpayments were classified changed in 2022, so each of these will need to be considered when drawing analysis. For the labor data, the data was re-weighted based on updated population estimates in 2024, which was applied retroactively to data from 2019 onwards, but not earlier years due to "time constraints".

Another limitation of the data is that the benefits data only provides demographic data for 2024 and 2025. If we had access to the demographic data for all years, we could combine that with the economic demographic data to draw further analysis about economic trends and benefits fraud.

# Gaps