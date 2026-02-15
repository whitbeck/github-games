# Account Balance Tracker Spreadsheet

## Overview

This Excel spreadsheet helps you track and project your account balances with support for:
- **Recurring monthly expenses** that can change over time
- **Historical tracking** without messing up past values
- **Non-monthly expenses** (quarterly, semi-annual, annual)
- **Predictable income** (bi-weekly salary with annual adjustments)
- **One-time or variable expenses**

## File Structure

The spreadsheet contains three main sheets:

### 1. Configuration Sheet
This sheet contains your initial settings:
- **Starting Balance**: Your account balance when you begin tracking
- **Starting Date**: The date you begin your projection
- **Income Settings**:
  - Bi-Weekly Salary amount
  - Annual salary increase percentage
  - Date of next salary increase

### 2. Expense History Sheet
This is the **key to handling expense changes without messing up historical values**.

**How it works:**
- Each row represents a change to a recurring expense
- When an expense amount changes, add a new row with:
  - Expense Name (same as before)
  - Effective Date (when the change starts)
  - New Monthly Amount
  - Frequency (Monthly, Quarterly, Semi-Annual, Annual)
  - Notes (optional description)

**Example from the problem statement:**

| Expense Name | Effective Date | Monthly Amount | Frequency | Notes |
|--------------|----------------|----------------|-----------|-------|
| Xcel Energy | 2026-01-01 | $350 | Monthly | Initial rate |
| Verizon Wireless | 2026-01-01 | $250 | Monthly | Phone bill |
| Lawn mowing | 2026-01-01 | $160 | Monthly | During growing season |
| Dog walking | 2026-01-01 | $80 | Monthly | Regular service |
| | | | | |
| Xcel Energy | 2026-09-01 | $280 | Monthly | Summer ends - lower usage |
| Lawn mowing | 2026-09-01 | $0 | Monthly | Summer ends - no more mowing |
| | | | | |
| Xcel Energy | 2026-12-01 | $320 | Monthly | Winter heating |
| Dog walking | 2026-12-01 | $0 | Monthly | Winter - no more walking |

**This approach preserves historical data** - past months show the amounts that were actually in effect at that time.

### 3. Projection Sheet
This sheet shows your month-by-month account balance projection:

**Columns:**
- **Month**: Sequential month number
- **Date**: First day of each month
- **Income**: Calculated based on bi-weekly salary (2 payments per month)
- **Recurring Expense Columns**: One column per recurring expense category
- **Other Expenses**: Manual entry for one-time or unpredicted expenses
- **Total Expenses**: Sum of all expenses for the month
- **Balance**: Running balance (previous balance + income - expenses)

## How to Use

### Initial Setup
1. Open the **Configuration** sheet
2. Set your starting balance and date
3. Enter your bi-weekly salary amount
4. Set your expected annual raise percentage and date

### Adding Recurring Expenses
1. Go to the **Expense History** sheet
2. Add a row for each recurring expense with its initial amount
3. Use the same expense name for all future changes to that expense

### Tracking Expense Changes
When an expense changes (like the examples in the problem statement):
1. Go to the **Expense History** sheet
2. Add a new row with:
   - Same expense name
   - New effective date
   - New amount (use $0 to stop an expense)
   - Keep the same frequency
   - Add a note explaining the change

### Adding Non-Monthly Expenses
For quarterly, semi-annual, or annual expenses:
1. Add them to the **Expense History** sheet
2. Set the Frequency to: Quarterly, Semi-Annual, or Annual
3. The projection will account for these less frequent charges

### Manual Adjustments
Use the **Other Expenses** column in the **Projection** sheet for:
- One-time purchases
- Variable expenses not covered by recurring items
- Emergency expenses
- Any costs that don't fit the recurring pattern

### Customization
To add more expense categories:
1. Add a new column in the **Projection** sheet
2. Update the Total Expenses formula to include the new column
3. Add corresponding entries in the **Expense History** sheet

## Example Scenario

Following the problem statement:

**Initial State (January 2026):**
- Xcel Energy: $350/month
- Verizon Wireless: $250/month  
- Lawn mowing: $160/month
- Dog walking: $80/month
- **Total**: $840/month

**Summer Ends (September 2026):**
- Xcel Energy: $280/month (decreased)
- Verizon Wireless: $250/month (unchanged)
- Lawn mowing: $0/month (stopped)
- Dog walking: $80/month (unchanged)
- **Total**: $610/month

**Winter Arrives (December 2026):**
- Xcel Energy: $320/month (increased for heating)
- Verizon Wireless: $250/month (unchanged)
- Lawn mowing: $0/month (still stopped)
- Dog walking: $0/month (stopped)
- **Total**: $570/month

Each period's historical data is preserved, and the projection automatically uses the correct amounts for each time period.

## Tips

1. **Review Monthly**: Check your projection against actual expenses and adjust as needed
2. **Update Regularly**: When you know about upcoming changes, add them to the Expense History
3. **Use Notes**: Document why expenses changed - this helps with future planning
4. **Extend the Timeline**: Copy formulas down to project further into the future
5. **Keep Backups**: Save copies periodically to preserve your financial history

## Regenerating the Spreadsheet

If you need to recreate the spreadsheet from scratch:

```bash
python3 create_budget_spreadsheet.py
```

This will generate a fresh `Account_Balance_Tracker.xlsx` file with the default template.

## Technical Details

- Created with Python and openpyxl library
- Compatible with Excel, Google Sheets, and LibreOffice Calc
- Uses formulas for automatic calculations
- Formatted for easy reading and data entry
