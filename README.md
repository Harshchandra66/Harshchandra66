# Business Data Management Capstone Project: Risk Management Strategy

## Overview 📊
This project aims to optimize **risk management** in financial trading by implementing and analyzing three different **Value at Risk (VaR)** methods and performing backtesting on a trading strategy. The goal is to assess potential **risk exposures** and improve decision-making with **data-driven insights**.

---

## Project Structure 🛠

### Stage 1: VaR - Historical Method 📉
- **Objective:** Estimate risk based on historical return distributions.
- **Approach:** Identify the 5th percentile of returns to calculate potential losses at a specified confidence level.

### Stage 2: VaR - Monte Carlo Simulation 🎲
- **Objective:** Simulate thousands of random market scenarios to calculate VaR.
- **Approach:** Incorporate extreme market events and randomness into the risk model for dynamic estimation.

### Stage 3: VaR - Parametric Method 📏
- **Objective:** Assume normally distributed returns to calculate VaR efficiently.
- **Approach:** Use the mean and standard deviation of returns to estimate potential risk exposure.

### Stage 4: Backtesting the Trading Strategy 🔄
- **Objective:** Test the developed strategy against historical data to evaluate its effectiveness.
- **Approach:** Use performance metrics like **Sharpe ratio**, **maximum drawdown**, and **profitability** to assess **risk-adjusted returns**.
