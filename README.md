# Home Loan Repayment Calculator

A web-based dashboard to simulate home loan repayment schedules, track additional payments, and visualize principal vs interest breakdowns over time.

## Features

- **Loan Parameter Input** — Configure initial loan amount, start date, tenure (in months), current outstanding balance, and annual interest rate
- **EMI Calculation** — Automatically computes monthly EMI using standard amortization formula
- **Repayment Schedule** — Generates a detailed month-by-month amortization table with EMI, principal, interest, extra payments, and remaining balance
- **Additional Payments** — Record one-time or recurring extra payments toward your loan principal
- **Recurring Payment Frequencies** — Supports Monthly, Quarterly, Half-Yearly, and Yearly recurring additional payments
- **Impact Analysis** — Shows interest saved and months reduced when additional payments are made
- **Interactive Charts** — Four visualizations powered by Chart.js:
  - **Principal vs Interest (Stacked Bar)** — Monthly breakdown of each EMI
  - **Cumulative Principal & Interest (Line)** — Running totals over time
  - **Overall Breakdown (Doughnut)** — Total principal vs total interest ratio
  - **Outstanding Balance (Area)** — Declining balance curve over the loan tenure

## Loan Summary Dashboard

The summary section displays key metrics at a glance:

| Metric | Description |
|--------|-------------|
| Monthly EMI | Fixed monthly installment amount |
| Total Interest | Total interest payable on remaining balance |
| Total Payment | Sum of principal + interest over remaining tenure |
| Interest Saved | Interest saved due to additional payments |
| Loan End Date | Projected loan closure date |
| Months Saved | Number of months reduced by extra payments |

## How to Use

### 1. Open the App

Simply open `index.html` in any modern web browser. No server, build tools, or dependencies to install.

```bash
# Or serve locally with Python
python -m http.server 8080
# Then open http://localhost:8080
```

### 2. Enter Loan Details

Fill in your loan parameters:
- **Initial Loan Amount** — The original sanctioned loan amount
- **Loan Start Date** — When the loan was disbursed
- **Tenure (Months)** — Total loan tenure in months
- **Current Outstanding Amount** — Present outstanding principal balance
- **Annual Interest Rate (%)** — Current annual interest rate

Click **Calculate Schedule** to generate the repayment plan.

### 3. Record Additional Payments

To simulate the impact of extra payments:
1. Select a **Payment Date**
2. Enter the **Additional Payment Amount**
3. Choose a **Frequency**:
   - **One-time** — Single lump-sum payment
   - **Monthly** — Recurring every month from the selected date
   - **Quarterly** — Recurring every 3 months
   - **Half-Yearly** — Recurring every 6 months
   - **Yearly** — Recurring every 12 months
4. Click **Add Payment**

The schedule, charts, and summary will automatically recalculate to reflect the impact.

## Default Configuration

The app comes pre-loaded with sample loan data:

| Parameter | Value |
|-----------|-------|
| Initial Loan Amount | INR 40,00,000 |
| Loan Start Date | 15 March 2017 |
| Tenure | 312 months |
| Outstanding Amount | INR 30,26,195 |
| Interest Rate | 8.25% |
| EMI Due Date | 23rd of each month |

## Tech Stack

- **HTML5 / CSS3 / JavaScript** — Single-file, zero-dependency app
- **Chart.js** (CDN) — For interactive chart visualizations
- **Responsive Design** — Works on desktop and mobile browsers

## Version History

### v1.2.0
- Added **dark/light theme toggle** with smooth transitions
- Theme preference persisted in localStorage across sessions
- Charts adapt colors (text, gridlines, legends) to match selected theme
- CSS variable-based theming for consistent styling

### v1.1.0
- Added **recurring additional payments** with frequency options (Monthly, Quarterly, Half-Yearly, Yearly)
- Changed tenure input to **months** for finer control
- Set EMI due date to the **23rd of each month**

### v1.0.0
- Initial release with EMI calculator, amortization schedule, one-time additional payments, and 4 interactive charts

## License

MIT License — free to use, modify, and distribute.
