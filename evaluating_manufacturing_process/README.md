---
runme:
  id: 01JYYES6Z45H1NV3JQ24ZWD5PC
  version: v3
---

# 📊 Statistical Process Control (SPC) in SQL
![manufacturing gears](manufacturing.jpg)

## Overview

This project implements **Statistical Process Control (SPC)** using SQL to monitor quality in a manufacturing process. The focus is on detecting anomalies in product dimensions (specifically height) to ensure high-quality production.

SPC is a proven method that uses statistical limits to determine whether a process is behaving consistently. This solution applies rolling calculations to define **Upper Control Limits (UCL)** and **Lower Control Limits (LCL)** and flags any measurements that fall outside the acceptable range.

---

## Dataset

**Table Name**: `manufacturing_parts`

| Column Name | Description                         |
| ----------- | ----------------------------------- |
| item\_no    | Unique identifier for the item      |
| length      | Length of the item                  |
| width       | Width of the item                   |
| height      | Height of the item (target value)   |
| operator    | Machine/operator producing the item |

---

## Objective

* Monitor item **height** to detect deviations from normal process behavior
* Calculate **rolling average and standard deviation** for each machine (operator)
* Compute **UCL and LCL** dynamically
* Flag items **outside control limits** for review

---

## SQL Logic Summary

The project uses:

* `WINDOW` functions for rolling aggregates
* `ROW_NUMBER()` to ensure a valid window of observations
* Nested queries to apply SPC logic
```

---

## Key Results

* Flagged out-of-control measurements in real-time
* Provided consistent quality thresholds per operator
* Enabled data-driven decisions to adjust the manufacturing process

---

## Future Improvements

* Add visualization (control charts) using Power BI or Python
* Extend logic to multiple measurements (e.g., length, width)
* Build an alert dashboard for production teams

---

## Author

**Jesse Mucheke**
Data Analyst | Python • SQL • Power BI
[LinkedIn](https://www.linkedin.com/in/jesse-mucheke-496533213/) | [GitHub](https://github.com/Jmucheke)

---