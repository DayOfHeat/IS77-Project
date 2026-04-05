# Progress Update

## Data formatting & cleaning

Both the fraud data and the labour data are completely import and ready for use. Fraud data had missing values handled, which the labor data didn't need. They can be found in `project.ipynb`.

## Data integration

Both data sets were integrated together by matching time periods together. The fraud data was in years and the labor data was in three month rolling averages, so we took the labor data and group it into years to combine with the fraud data. This can be found in `project.ipynb`

## Finish report

The data quality section of the report was written and can be found in `README.md`. A title was selected for the project and contributors were listed in the report. The rest of the report remains to be done.

# Timeline Update

Going into the status report, we didn't have any dates set, but now that we do we have been keeping pace. We currently are ahead of schedule with the 'data formatting & cleaning' and 'data integration' steps done and the data analysis and data visualization steps started. We originally only planned to do the report portion of the project once all the data was analyzed and visualized, but we ended up starting it early with the data quality section already done. Due to increasing business at the end of the school year, we opted to keep our current timeline in place rather than move it forward.

# Project Plan Changes

Now that we have the proper due dates, the timeline has dates for each objective to be finished by. A note on missing values was also added to the formatting and cleaning timeline item. The gaps section had the parts about not know the project due dates and not knowing the best way to import excel data removed, as now we have due dates and the data is fully imported.

# Challenges

Working around the excel format of the data was a major challenge. Especially for the fraud data, the excel sheets were formatted in a way that was nice for human readability, but which resulted in a lot of headaches and having to repeatedly make minor tweaks when mistakes were found. We used a different method for each dataset that matched its structure. For the fraud data we used pandas `read_excel` function and wrote code that was manually adapted to the structure due to various one-off visual markers in the data which were nice for human readability but annoying for machine readability. Because the labor data was already formatted in uninterrupted tables, we used xlrd and regular expressions to parse the data automatically from each sheet.

Another challenge we dealt with was deciding how to deal with the large quantity of missing values in the fraud data. As we discuss in our `README.md`, a large amount of w's, x's, and z's representing "no data found in sample", "data unavailable", and "not applicable". We made the decision to take the z's, which are intentionally missing, and x's which are unknown missing values, though usually because a certain program doesn't exist or hasn't existed long enough to have data yet, and treat them all as 0. This is relatively consistent with the reality, as there is no fraud for programs that don't exist, and also works well for graphing. We didn't think it was appropriate to impute anything for these values since they often represented programs simply not existing yet. For w's, we did decide to impute values because w's were known areas were data was missing for a certain year. We decided to use the scikit learn's KNN imputer of each program's fraud to impute the missing values because trends in the fraud data were generally just stable rises in fraud, so we figured that using k=2 and uniforms weights to just continue the slope between the two nearest points would make the most sense.

Another challenge with the labor data was that it was spread across 28 sheets and each one was formatted differently. Some of the sheets had multiple header rows stacked on top of each other, some stored dates as numbers instead of readable text, and others had footnote text mixed in with the actual data rows. In order to handle all of this without writing completely separate code for every sheet,a parser that could be adjusted depending on the sheet was built. 5 sheets ended up being left out entirely, with 3 only having metadata text and the other 2 had their data removed by ONS and moved to a different dataset.

# Contributions

## Joshua Watson

I wrote the code for importing the fraud data from the excel file and prepared it for use. I also wrote the data quality portion of the report. I added due dates to the project plan's timeline now that we have the project due date. I integrated the two data set together.

## Michael Eannone

I wrote the code for importing the labor data from the Excel file and got it ready to use. The labor data was spread across 22 different sheets and each one was formatted a little differently, so I used xlrd and regular expressions to parse them automatically instead of writing separate code for each sheet. I also helped write this status report update.
