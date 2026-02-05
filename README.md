# Disneyland Reviews Analysis System

A Python-based data analysis application that processes and visualises customer reviews from Disneyland parks around the world.

This project was developed for the **QHO444 – Problem Solving Through Programming** module at Solent University.  
It demonstrates data processing, modular design, visualisation with Matplotlib, and Object-Oriented Programming principles.

---

## 📌 Overview

The system loads a large CSV dataset of Disneyland reviews and allows users to:

- Explore review data interactively
- Filter reviews by park and location
- Calculate statistics and averages
- Generate charts and visual insights
- Export aggregated results in multiple formats

The application runs using a simple **text-based menu interface (TUI)**.

---

## ✨ Features

### Data Import
- Loads reviews from a CSV file
- Displays total number of records loaded

### View Data
- Display all reviews for a specific park
- Count reviews by park and reviewer location
- Calculate average rating by year
- Calculate average score per park by location

### Visualisation
- Pie chart: review distribution per park
- Bar chart: top 10 reviewer locations by rating
- Bar chart: monthly average ratings

### Data Export (OOP)
- Export aggregated statistics
- Supported formats:
  - TXT
  - CSV
  - JSON

---

## 🧠 Technologies Used

- Python 3
- CSV module
- Matplotlib
- Git & GitHub
- Object-Oriented Programming (OOP)

  ## 🏗 Project Structure
  disneyland_reviews.csv Dataset file

main.py → Controls program flow and menus
tui.py → Handles all user input/output
process.py → Data filtering and calculations
visual.py → Charts and visualisations
exporter.py → OOP-based export system


### Module Responsibilities

**main.py**
- Entry point of the program
- Manages navigation and integration of modules

**tui.py**
- Text User Interface
- Handles prompts, menus, and validation

**process.py**
- Data loading
- Filtering and aggregation
- Statistical calculations

**visual.py**
- Generates charts using Matplotlib

**exporter.py**
- Implements OOP export system
- Uses inheritance and polymorphism

---

## ▶️ How to Run

1. Install Python 3
2. Install dependencies
3. Run the program

## 👤 Author

Ionut Ungureanu  
BSc (Hons) Computer Science  
Solent University

