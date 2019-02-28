# deerioscraper

I was assigned the task: monitoring the catalog of sales sites deer.io/catalog, collecting updated data, parsing the collected data into a table, visualizing the data obtained.
After exploring possible options, I decided to implement this project using python with scrapy framework. 
The main problem encountered during the work was the output data format, which is a table. Due to the lack of experience with this framework, the data had to be converted using a separate function.
Data collection every 15 minutes was implemented using the built-in Windows taskschd.msc.

# To Do
 1. Rewrite the spider function to parse better quality data scturcture.
 2. Visualize data with the matplotlib framework.
 3. Find the way to perform the task without using Windows Task Scheduler.

# What I've learned:
  * Base knowledge about scrapy framework
  * Formating dissatisfied data sctructure with python
  * Parsing data to csv with additional objects
