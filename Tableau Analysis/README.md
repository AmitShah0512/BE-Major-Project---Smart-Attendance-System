# Attendance Intelligence System – Early Risk Detection Using Tableau

Most colleges record attendance every day, but that data is rarely *used*.
Problems are usually discovered only at exam time, when it’s already too late.

I built this system to change that.

This project converts raw attendance logs into an interactive analytics dashboard that helps faculty and administrators **identify at-risk students early**, understand *why* they are at risk, and take timely action.

---

## Why This Project Exists

In a typical classroom:

* Attendance is stored, but not analyzed
* Faculty cannot easily see long-term patterns
* At-risk students are noticed too late
* Decisions are reactive, not proactive

I wanted to turn attendance into a **decision system**, not just a record.

So instead of asking:

> “What is today’s attendance?”

This system answers:

* Is attendance improving or declining over time?
* Which students are becoming risky?
* In which subjects is the problem happening?
* Who needs immediate attention?

---

## Data & System Overview

The data comes from my **Smart Attendance System** (Python + OpenCV).

Each row represents one lecture:

> “On this date, for this subject, this student was Present or Absent.”

Fields used:

* Date
* Student ID
* Student Name
* Class
* Subject
* Status (Present / Absent)

The dataset contains around **6 months of real attendance data** (Jan–Jun).

Tools used:

* Python – attendance generation
* Excel – intermediate storage
* Tableau – analytics and dashboarding

This event-level structure is the same way real companies store logs and activity data.

---

## What I Built

This is not just a dashboard. It is a **decision-support system**.

It includes:

* A true **Overall Attendance KPI**
  (calculated from raw events, not averages of averages)

* A **Monthly Trend View**
  to show whether engagement is improving or declining

* **Dynamic Risk Classification**

  * Safe
  * At Risk
  * Critical
    (based on a configurable threshold)

* **Subject-wise Root Cause Analysis**
  so we know *why* a student is at risk

* **Interactive Drill-down**
  Click a student → instantly see their subject-wise breakdown

* **Role-based Filters**
  Class and Subject filters so the same system works for:

  * HOD
  * Faculty
  * Admin

* **Action Recommendations**

  * Immediate Intervention
  * Monitor & Counsel
  * No Action Needed

The goal is simple:
Turn passive logs into **actionable intelligence**.

---

## Real-World Value

This system helps institutions:

* Detect at-risk students early
* Focus faculty effort where it matters
* Prevent last-moment exam crises
* Make data-driven academic decisions

Instead of just *seeing* attendance, stakeholders can now:

* Track trends across the semester
* Spot risk before it becomes failure
* Understand why a student is struggling
* Take targeted action

---

## How to Use

1. Open the `.twbx` file in Tableau
2. Ensure the data files are present in `/data`
3. Use:

   * The attendance threshold slider
   * Class and Subject filters
   * Click a student to drill down

---

## Skills Demonstrated

* Event-level data modeling
* KPI design and validation
* Time-series analysis
* Risk segmentation
* Interactive dashboard design
* Business-oriented analytics thinking

---

This project shows how raw operational data can be transformed into a **real decision system**, not just charts.
