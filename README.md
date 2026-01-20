# Hospital Patient Data Analysis using NumPy

A Python-based data analysis project demonstrating the power of **NumPy** for handling multidimensional arrays, performing statistical analysis, and data preprocessing.

## 📊 Project Overview
This project simulates a hospital dataset containing records for 20 patients. Each patient record includes:
* **Age** (Years)
* **Blood Pressure** (mmHg)
* **Heart Rate** (bpm)
* **Hospital Stay Duration** (Days)

The goal is to perform basic and advanced data manipulation tasks using purely NumPy functions.

## 🚀 Features & Tasks
The script performs the following operations:
1.  **Data Generation:** Creates a $20 \times 4$ random dataset within specific physiological ranges.
2.  **Statistical Analysis:** * Calculates average age.
    * Identifies BP extremes (Min/Max).
    * Filters patients based on specific health metrics (e.g., Heart Rate > 100).
3.  **Data Preprocessing:**
    * Normalizes features to a $0-1$ scale using Min-Max scaling:
        $$X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$$
    * Sorts data based on specific criteria (Age).
4.  **Advanced Operations:**
    * Horizontal stacking (`hstack`) to add a "Hospital Charges" column.
    * Binary file persistence using `.npy` format.

## 🛠️ Requirements
* Python 3.x
* NumPy

## 📖 How to Use
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/hospital-data-analysis.git](https://github.com/your-username/hospital-data-analysis.git)