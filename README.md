# Surfs Up Data Analysis

## Overview of Analysis

The purpose of this analysis is to compare temperature statistics from June and December for the Hawaiian island of Oahu, which will help determine the viability of W. Avy's surf/ice cream shop business model for this location.

### Resources used in this analysis
- SQLite db file - ***hawaii.sqlite***

---

## Results

  - **December has a mean tempature difference from June of -3.9 degrees.**
    - June mean temp - 74.9
    - December mean temp - 71.0
  
  - **The maximum temperatures vary by only 2 degrees.**
    - June max temp - 85.0
    - December max temp - 83.0

  - **The minimum temperature has a higher variability of 8 degrees.**
    - June min temp - 64.0
    - December min temp - 56.0

---

## Summary

Using the above data comparison, it can be determined that daytime high temperature variation should not greatly affect the sales of the shop, but that the lower minimum temperatures during the winter months may decrease the morning/evening sales of ice cream. Overall though, the uniformity of weather in Oahu implies that the shop could maintain enough traffic to sustain itself year-round.

### Additional queries for future analysis

- **June/December rainfall queries** -- run queries to compare precipitation totals for the two months to help get a feel for the weather pattern differences between summer and winter.
    - ```session.query(Measurement.prcp).filter(extract('month', Measurement.date) == '06').all()```
    - ```session.query(Measurement.prcp).filter(extract('month', Measurement.date) == '12').all()```

- **Monthly weather analysis for staffing** - run a query to retrieve temperature and precipitation amounts, and group them by month to help see what months will probably require more labor hours in the budget.
  - ```session.query(Measurement.date, Measurement.tobs, Measurement.prcp).group_by(func.strftime('%m', Measurement.date)).all() ```