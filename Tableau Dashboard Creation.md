# Start

This document summarizes the thought process and details of creating a Tableau Dashboard for visualizing US COVID statistics during the 2020 calendar year.

# 

![]("\Pictures\FinalDashboard.PNG")

# Notes: 

Before I started playing with data, I start with these questions:
1. How are states handling COVID?
   * Which states are doing well/poorly?
   * How are case numbers changing?
0. Who am I designing this dashboard for?
   * Data science professionals?
      * More aware of what metrics are important
   * Average American?


## Important Data Metrics:
* Total number of cases.
   * Case count / state population.
      * Lets you know state efficiency at handling COVID.
   * Case count 

## Average American:
* How bad is it now?
   * Total number of cases.
* How bad will it be?
   * Case count acceleration?
   * Boolean "Getting Better" or "Getting Worse".
   * Weekly percent change ?

## Data Scientist:
* How bad is it now?
* How bad will it be?
   * Case 



# Design:
* Map of US that has buttons to show: Cases, Deaths, Deadliness.
* Play button to show progression over time.
* Data box to show 


# Level 1 User:
* How bad was COVID?
* Animation of elapsing time.
   * Fast timeline of play.
* Ticker for Total Cases, Deaths, and Deadliness (Deaths/Cases)
   * Pie Chart for visually showing the same thing?
      * This gives an instant "proportions viewpoint" for a non-numbers person.
      * Redundant information helps drive home point.
* Minimizes number of interactive options or slicers that they can touch.
* Map graphic because maps are cool and recognizable.

# Holistic View of how COVID progressed: 
* Focus is on the timeline: How did COVID unfold in 2020.
* Target audience is CDC looking back on how they did for 2020.
   * Useful for estimating peak load (on hospitals) during a pandemic.
   * Percentage of infected population could provide insight into why it was low/high.
* This means:
   * Cumulative case load (as opposed to new cases per day).
   * Time series data (as opposed to just a bar graph) - likely a line chart.
* Figure out if there were specific events that caused higher than normal spikes.

## Takeaway:
* Here are the states that did well in Prevalence, Deadliness.

# Things I did:
* Plan out the scope of what I was trying to show (target audience).
   * Information that I would want to see that I hadnt before.
* Spent a lot of time in the data before ever reaching Tableau.
   * Derived new fields for new cases/deaths from cumulative numbers.
   * Noticed that sometimes the number of deaths decreased...
      * This could be a misreport, or a data error.
      * Corrected this to zero for the purpose of the excercise.