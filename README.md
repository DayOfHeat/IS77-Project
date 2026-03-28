# Analysis of UK Benefits Fraud Against Labor Data

## Contributors

- Joshua Watson

- Michael Eannone

## Summary

[]

## Data Profile

[]

## Data Quality

### Accuracy

Given that the data is all numerical, we can be assured of syntactic accuracy in the fraud data. The fraud data was collected based on the DWP's audits of benefits claimants, which means that we cannot easily verify the accuracy of the data, as the individual audits are not public and we do not have the legal authority to conduct our own.

For the labor data, it too is all numerical, so syntactic accuracy is not a concern. Labor data is a much more heavily studied field than benefits fraud, so there are other independent surveys we could compare the data against. The data is collected via survey, so we can expect that some amount of people will lie, which could effect the accuracy of the data, especially given that people are more likely to lie to hide they are unemployed, so there probably isn't an equal amount of lying across all years. We could independently conduct our own survey to get 2026 data, but we would have to rely on existing data to verify past years.

### Completeness

The fraud data is rife with x's, w's, and z's representing data unavailable, no data found in sample, and not applicable, respectively. Unfortunately, 'x', which is the most ambiguous missing value, is also the most common. The reason for data labeled 'x' being missing can be for multiple reasons, as evidenced by Universal Credit. Universal Credit, a social security program, started in 2013 (Department for Work & Pensions), yet the data set is missing data from 2015 and earlier, with all years being labeled with just 'x'. Data before 2013 should be labeled as not applicable and we should consider 2013-2015 as missing, but there is no way to know that without outside research. This same issue applies to several other programs, making it hard to tell how truly complete the data is. Fortunately, 'w' clearly means the data is missing and thus incomplete and 'z' that the data is not applicable, which we can consider as complete. While not strictly missing, the fraud data for the Disability Living Allowance rounds to 0 every year, so in effect we have no data for it.

The labor data is complete in its entirety for all the data we are using, though it is missing data on labor disputes during the pandemic and some metrics have a year-on-year percent change that is missing because can't be calculate for for the first year data is collected.

### Consistency

Both data sets underwent changes in collection methodology. For the benefits fraud data, the data collection method changed in 2019 and how underpayments were classified changed in 2022. For this project, the 2022 change isn't relevant, but care should be taken went comparing data from before and after 2019. Most of the data is numerical, so the formatting is generally consistent, but for the x's, w's, and z's for missing values, sometimes characters were accidentally uppercase instead of the standard lowercase.

For the labor data, the data was re-weighted based on an updated population estimate in 2024. This change was retroactively applied to data from 2019 onward, but not to earlier years, with the ONS citing "time constraints". This change will also require us to be careful when using data from before and after 2019, which happens to correspond with the changes in the fraud data.

### Timeliness

The fraud data is overall very timely for this project as it has data as recent as 2025 and it published on an annual basis. It has data as far back as 2006, which will be useful for long term analysis. The only issue is that certain programs didn't exist for or otherwise don't have data for that full time period. The changes in collection methodology limits the utility of the more recent data, making that aspect of timeliness less impactful.

The labor data is published monthly and was updated in February 2026 with data up to December 2025, making it also very recent. The labor data goes as far back as 1971 for certain unemployment data, though most of the data only goes back to the 90s. Both of those are further back than the fraud data, so it will be plenty sufficient to compare 
with benefits fraud trends.

## Data Cleaning

[]

## Findings

[]

## Future Work

[]

## Reproducing

[]

## References

Department for Work & Pensions. (8 May 2015). *2010 to 2015 government policy: welfare reform*. GOV.UK. https://www.gov.uk/government/publications/2010-to-2015-government-policy-welfare-reform/2010-to-2015-government-policy-welfare-reform#appendix-1-government-policy-on-universal-credit-an-introduction