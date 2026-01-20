# Smart Attendance System with Attendance Intelligence Dashboard

This project is a complete **end-to-end Student Attendance Intelligence System**.
It does more than just mark students present or absent. It turns raw classroom data into **useful insights** for teachers and administrators.

It brings together:

* **Computer Vision (Face Recognition)**
* **Structured Data Storage**
* **Automated Reporting**
* **Visual Analytics (Tableau)**

to convert everyday attendance events into **actionable academic intelligence**.

---

## 🔍 The Problem

In most colleges and schools:

* Attendance is recorded, but rarely analyzed
* Trends are invisible
* At-risk students are noticed too late
* Decisions are reactive instead of data-driven

Teachers usually ask:

> “What is today’s attendance?”

This system helps answer deeper questions:

* Is attendance improving or getting worse over time?
* Which students are becoming risky?
* In which subjects is the problem happening?
* Who needs immediate academic attention?

The goal is to convert attendance from a **record-keeping task** into a **decision-support system**.

---

## 🏗️ How the System Works

```
Camera
   ↓
Python + OpenCV (Face Recognition)
   ↓
Structured Attendance Logs (Excel)
   ↓
Automated Reports + Visual Analytics
   ↓
Tableau Dashboards (KPIs, Risk, Trends)
```

---

## 🧠 Layer 1: Smart Attendance System (Operational Layer)

Built in Python using:

* OpenCV + Face Recognition
* Tkinter (GUI)
* Pandas
* Excel-based storage

### What it does

* Detects and recognizes faces in real time
* Enrolls students and generates face encodings
* Marks attendance automatically
* Prevents duplicate entries in the same session
* Stores subject-wise daily attendance
* Generates monthly attendance reports
* Shows a project timeline using a Gantt chart
* Provides a simple GUI for classroom use

Each attendance entry is stored as:

> Date + Subject + Student ID + Name + Class + Time

This event-level structure is similar to how real production systems store logs.

---

## 📊 Layer 2: Attendance Intelligence System (Analytics Layer)

Built using:

* Excel (as an intermediate dataset)
* Tableau Public / Desktop

### What the analytics provide

* Overall Attendance KPI
* Monthly and long-term trends
* Student-level attendance percentages
* Risk categories:

  * Safe
  * At Risk
  * Critical
* Subject-wise root cause analysis
* Student drill-down views
* Class and subject filters
* Early-warning indicators

This layer turns raw logs into **early-warning academic intelligence**.

---

## 🗂️ Project Structure

```
Smart-Attendance-System/
├── src/
│   ├── Dashboard.py        # Main GUI controller
│   ├── enroll.py           # Student face enrollment
│   ├── recognize.py        # Face recognition + attendance marking
│   ├── utils.py            # Student data loader
│   ├── report.py           # Monthly report generator
│   ├── graph.py            # Gantt chart visualization
│   └── view_attendance.py  # Attendance viewer
│
├── data/                   # Attendance logs and student data
├── screenshots/            # Application screenshots
├── Tableau Analysis/       # Tableau dashboards and analytics layer
├── requirements.txt.txt
└── README.md
```

---

## 🚀 How to Run

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt.txt
```

### Step 2: Run the Application

```bash
cd src
python Dashboard.py
```

### Step 3: Typical Workflow

1. Enroll students using the webcam
2. Capture face samples
3. Generate encodings
4. Start face recognition
5. Attendance is marked automatically
6. Generate reports using `report.py`
7. Analyze data in Tableau

---

## 📈 Using the Analytics (Tableau)

1. Open files from:

```
Tableau Analysis/
```

2. Connect Tableau to attendance Excel files in:

```
data/
```

3. Use filters:

* Subject
* Class
* Student

4. Analyze:

* Attendance percentage
* Risk categories
* Trends over time

---

## 💼 Real-World Value

This system helps institutions:

* Detect disengagement early
* Prevent last-minute attendance crises
* Focus faculty effort where it matters
* Track engagement across semesters
* Make data-driven academic decisions

Instead of only *seeing* attendance, stakeholders can:

* Understand patterns
* Predict risk
* Take timely action

---

## 🛠️ Skills Demonstrated

* Computer Vision (Face Recognition)
* GUI Application Development (Tkinter)
* Event-level Data Modeling
* Data Cleaning & Aggregation
* KPI Design
* Time-Series Analysis
* Risk Segmentation
* Automated Reporting
* Tableau Dashboard Design
* Business-Oriented Analytics Thinking

---

## 📌 In One Line

This project shows how raw operational data from a computer vision system can be transformed into a **complete analytics pipeline**, bridging the gap between **engineering** and **data-driven academic decision making**.
