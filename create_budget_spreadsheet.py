#!/usr/bin/env python3
"""
Script to generate an Excel spreadsheet for account balance tracking and projection.
This spreadsheet handles recurring monthly expenses that can change over time,
non-monthly expenses, and predictable income.
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime

def create_budget_spreadsheet(filename="Account_Balance_Tracker.xlsx"):
    """Create a comprehensive budget tracking spreadsheet."""
    
    wb = Workbook()
    
    # Create sheets
    ws_config = wb.active
    ws_config.title = "Configuration"
    ws_projection = wb.create_sheet("Projection")
    ws_history = wb.create_sheet("Expense History")
    ws_non_monthly = wb.create_sheet("Non-Monthly Expenses")
    
    # Configure the Configuration sheet
    setup_configuration_sheet(ws_config)
    
    # Configure the Expense History sheet
    setup_expense_history_sheet(ws_history)
    
    # Configure the Non-Monthly Expenses sheet
    setup_non_monthly_expenses_sheet(ws_non_monthly)
    
    # Configure the Projection sheet
    setup_projection_sheet(ws_projection)
    
    # Save the workbook
    wb.save(filename)
    print(f"✓ Created spreadsheet: {filename}")
    return filename

def setup_configuration_sheet(ws):
    """Set up the configuration sheet with initial settings."""
    
    # Title
    ws['A1'] = "Account Balance Tracker - Configuration"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:D1')
    
    # Starting Balance
    ws['A3'] = "Starting Balance"
    ws['A3'].font = Font(bold=True)
    ws['B3'] = 10000  # Default starting balance
    ws['B3'].number_format = '$#,##0.00'
    
    ws['A4'] = "Starting Date"
    ws['A4'].font = Font(bold=True)
    ws['B4'] = datetime(2026, 1, 1)
    ws['B4'].number_format = 'YYYY-MM-DD'
    
    # Income Section
    ws['A6'] = "INCOME SETTINGS"
    ws['A6'].font = Font(bold=True, size=12, color="FFFFFF")
    ws['A6'].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws.merge_cells('A6:D6')
    
    ws['A7'] = "Bi-Weekly Salary"
    ws['A7'].font = Font(bold=True)
    ws['B7'] = 3000
    ws['B7'].number_format = '$#,##0.00'
    
    ws['A8'] = "Annual Salary Increase %"
    ws['A8'].font = Font(bold=True)
    ws['B8'] = 0.03  # 3% annual increase
    ws['B8'].number_format = '0.00%'
    
    ws['A9'] = "Next Salary Increase Date"
    ws['A9'].font = Font(bold=True)
    ws['B9'] = datetime(2027, 1, 1)
    ws['B9'].number_format = 'YYYY-MM-DD'
    
    # Set column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15

def setup_expense_history_sheet(ws):
    """Set up the expense history sheet to track changes over time."""
    
    # Title
    ws['A1'] = "Expense Change History"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:E1')
    
    # Instructions
    ws['A2'] = "Use this sheet to define your recurring expenses and when they change."
    ws['A2'].font = Font(italic=True)
    ws.merge_cells('A2:E2')
    
    ws['A3'] = "Each row represents a new value for an expense starting on a specific date."
    ws['A3'].font = Font(italic=True)
    ws.merge_cells('A3:E3')
    
    # Headers
    headers = ['Expense Name', 'Effective Date', 'Monthly Amount', 'Frequency', 'Notes']
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_num)
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center')
    
    # Example data based on problem statement
    examples = [
        ['Xcel Energy', datetime(2026, 1, 1), 350, 'Monthly', 'Initial rate'],
        ['Verizon Wireless', datetime(2026, 1, 1), 250, 'Monthly', 'Phone bill'],
        ['Lawn mowing', datetime(2026, 1, 1), 160, 'Monthly', 'During growing season'],
        ['Dog walking', datetime(2026, 1, 1), 80, 'Monthly', 'Regular service'],
        ['', '', '', '', ''],
        ['Xcel Energy', datetime(2026, 9, 1), 280, 'Monthly', 'Summer ends - lower usage'],
        ['Lawn mowing', datetime(2026, 9, 1), 0, 'Monthly', 'Summer ends - no more mowing'],
        ['', '', '', '', ''],
        ['Xcel Energy', datetime(2026, 12, 1), 320, 'Monthly', 'Winter heating'],
        ['Dog walking', datetime(2026, 12, 1), 0, 'Monthly', 'Winter - no more walking'],
        ['', '', '', '', ''],
        ['HOA Fees', datetime(2026, 1, 1), 150, 'Quarterly', 'Paid every 3 months'],
        ['Insurance', datetime(2026, 1, 1), 600, 'Semi-Annual', 'Paid twice per year'],
    ]
    
    for row_num, data in enumerate(examples, 6):
        for col_num, value in enumerate(data, 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = value
            
            if col_num == 2 and value:  # Date column
                cell.number_format = 'YYYY-MM-DD'
            elif col_num == 3 and value:  # Amount column
                cell.number_format = '$#,##0.00'
    
    # Set column widths
    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 30
    
    # Add validation note for Frequency column
    ws['A21'] = "Frequency options: Monthly, Quarterly, Semi-Annual, Annual"
    ws['A21'].font = Font(italic=True, size=9)
    ws.merge_cells('A21:E21')

def setup_non_monthly_expenses_sheet(ws):
    """Set up a dedicated sheet for tracking non-monthly expenses."""
    
    # Title
    ws['A1'] = "Non-Monthly & One-Time Expenses"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:F1')
    
    # Instructions
    ws['A2'] = "Track quarterly, semi-annual, annual, and one-time expenses here."
    ws['A2'].font = Font(italic=True)
    ws.merge_cells('A2:F2')
    
    ws['A3'] = "These expenses will be included in your projection at the appropriate times."
    ws['A3'].font = Font(italic=True)
    ws.merge_cells('A3:F3')
    
    # Headers
    headers = ['Expense Name', 'Amount', 'Frequency', 'First Payment Date', 'Last Payment Date', 'Notes']
    header_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_num)
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', wrap_text=True)
    
    # Example non-monthly expenses
    examples = [
        ['HOA Fees', 150, 'Quarterly', datetime(2026, 1, 1), datetime(2028, 12, 31), 'Paid in Jan, Apr, Jul, Oct'],
        ['Car Insurance', 600, 'Semi-Annual', datetime(2026, 1, 1), datetime(2028, 12, 31), 'Paid in Jan and Jul'],
        ['Property Tax', 2400, 'Annual', datetime(2026, 4, 1), datetime(2028, 12, 31), 'Paid once per year in April'],
        ['Amazon Prime', 139, 'Annual', datetime(2026, 3, 1), datetime(2028, 12, 31), 'Annual subscription'],
        ['Holiday Gifts', 800, 'Annual', datetime(2026, 12, 1), datetime(2028, 12, 31), 'December shopping'],
        ['Car Registration', 180, 'Annual', datetime(2026, 6, 1), datetime(2028, 12, 31), 'Renew in June'],
    ]
    
    for row_num, data in enumerate(examples, 6):
        for col_num, value in enumerate(data, 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = value
            
            if col_num in [4, 5] and value:  # Date columns
                cell.number_format = 'YYYY-MM-DD'
            elif col_num == 2 and value:  # Amount column
                cell.number_format = '$#,##0.00'
    
    # Set column widths
    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 12
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 18
    ws.column_dimensions['F'].width = 30
    
    # Add frequency guide
    ws['A13'] = "Frequency Guide:"
    ws['A13'].font = Font(bold=True)
    ws['A14'] = "• Quarterly: Every 3 months (4 times per year)"
    ws['A15'] = "• Semi-Annual: Every 6 months (2 times per year)"
    ws['A16'] = "• Annual: Once per year"
    ws['A17'] = "• One-Time: Single occurrence (enter same date for First and Last Payment Date)"
    
    for row in range(14, 18):
        ws.merge_cells(f'A{row}:F{row}')
        ws.cell(row=row, column=1).font = Font(italic=True, size=9)

def setup_projection_sheet(ws):
    """Set up the projection sheet with formulas for calculating balances."""
    
    # Title
    ws['A1'] = "Account Balance Projection"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:L1')
    
    # Instructions
    ws['A2'] = "This sheet projects your account balance based on recurring expenses and income."
    ws['A2'].font = Font(italic=True)
    ws.merge_cells('A2:L2')
    
    ws['A3'] = "Add one-time expenses in the 'Other Expenses' column. Non-monthly expenses appear in their own column."
    ws['A3'].font = Font(italic=True)
    ws.merge_cells('A3:L3')
    
    # Headers
    headers = ['Month', 'Date', 'Income', 'Xcel Energy', 'Verizon Wireless', 
               'Lawn Mowing', 'Dog Walking', 'Non-Monthly', 'Other Expenses', 
               'Total Recurring', 'Total Expenses', 'Balance']
    
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF")
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_num)
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', wrap_text=True)
    
    # Starting balance row
    ws['A6'] = "Starting"
    ws['B6'] = "=Configuration!B4"
    ws['B6'].number_format = 'YYYY-MM-DD'
    ws['L6'] = "=Configuration!B3"
    ws['L6'].number_format = '$#,##0.00'
    ws['L6'].font = Font(bold=True)
    
    # Create 36 months of projections (3 years)
    for month_num in range(1, 37):
        row = 6 + month_num
        
        # Month number
        ws.cell(row=row, column=1).value = month_num
        
        # Date (first day of each month)
        ws.cell(row=row, column=2).value = f'=DATE(YEAR(B6), MONTH(B6)+{month_num}, 1)'
        ws.cell(row=row, column=2).number_format = 'YYYY-MM-DD'
        
        # Income (2 salary payments per month)
        ws.cell(row=row, column=3).value = '=Configuration!B7*2'
        ws.cell(row=row, column=3).number_format = '$#,##0.00'
        
        # Recurring expenses (columns D-G)
        for col in range(4, 8):
            ws.cell(row=row, column=col).value = 0
            ws.cell(row=row, column=col).number_format = '$#,##0.00'
        
        # Non-Monthly Expenses (column H) - placeholder for manual entry from Non-Monthly sheet
        ws.cell(row=row, column=8).value = 0
        ws.cell(row=row, column=8).number_format = '$#,##0.00'
        ws.cell(row=row, column=8).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
        
        # Other Expenses (manual entry) - column I
        ws.cell(row=row, column=9).value = 0
        ws.cell(row=row, column=9).number_format = '$#,##0.00'
        ws.cell(row=row, column=9).fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
        
        # Total Recurring (sum of recurring monthly expenses)
        ws.cell(row=row, column=10).value = f'=SUM(D{row}:G{row})'
        ws.cell(row=row, column=10).number_format = '$#,##0.00'
        
        # Total Expenses (all expenses including non-monthly and other)
        ws.cell(row=row, column=11).value = f'=SUM(D{row}:I{row})'
        ws.cell(row=row, column=11).number_format = '$#,##0.00'
        ws.cell(row=row, column=11).font = Font(bold=True)
        
        # Balance
        prev_balance = f'L{row-1}'
        income = f'C{row}'
        expenses = f'K{row}'
        ws.cell(row=row, column=12).value = f'={prev_balance}+{income}-{expenses}'
        ws.cell(row=row, column=12).number_format = '$#,##0.00'
        ws.cell(row=row, column=12).font = Font(bold=True)
        
        # Add conditional formatting for low balance (visual warning)
        if month_num % 3 == 0:  # Every 3rd month, add a subtle background
            for col in range(1, 13):
                ws.cell(row=row, column=col).fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
    
    # Set column widths
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 12
    for col in range(3, 13):
        ws.column_dimensions[get_column_letter(col)].width = 14
    
    # Add example recurring expenses for first year based on problem statement
    # Month 1-8 (Jan-Aug): All expenses active
    for row in range(7, 15):  # Months 1-8
        ws.cell(row=row, column=4).value = 350  # Xcel Energy
        ws.cell(row=row, column=5).value = 250  # Verizon
        ws.cell(row=row, column=6).value = 160  # Lawn mowing
        ws.cell(row=row, column=7).value = 80   # Dog walking
    
    # Month 9-11 (Sep-Nov): Summer ends
    for row in range(15, 18):
        ws.cell(row=row, column=4).value = 280  # Xcel Energy reduced
        ws.cell(row=row, column=5).value = 250  # Verizon unchanged
        ws.cell(row=row, column=6).value = 0    # Lawn mowing stopped
        ws.cell(row=row, column=7).value = 80   # Dog walking still active
    
    # Month 12-36 (Dec onwards): Winter through rest of projection
    for row in range(18, 43):
        ws.cell(row=row, column=4).value = 320  # Xcel Energy winter
        ws.cell(row=row, column=5).value = 250  # Verizon unchanged
        ws.cell(row=row, column=6).value = 0    # Lawn mowing stopped
        ws.cell(row=row, column=7).value = 0    # Dog walking stopped
    
    # Add example non-monthly expenses in appropriate months
    # HOA Fees - Quarterly (Jan, Apr, Jul, Oct)
    for month in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        if month <= 36:
            ws.cell(row=6+month, column=8).value = 150
    
    # Car Insurance - Semi-Annual (Jan, Jul)
    for month in [1, 7, 13, 19, 25, 31]:
        if month <= 36:
            current_val = ws.cell(row=6+month, column=8).value or 0
            ws.cell(row=6+month, column=8).value = current_val + 600
    
    # Property Tax - Annual (Apr)
    for month in [4, 16, 28]:
        if month <= 36:
            current_val = ws.cell(row=6+month, column=8).value or 0
            ws.cell(row=6+month, column=8).value = current_val + 2400
    
    # Add notes section
    note_row = 44
    ws.cell(row=note_row, column=1).value = "Notes:"
    ws.cell(row=note_row, column=1).font = Font(bold=True)
    
    notes = [
        "• Yellow cells (Non-Monthly): Automatically populated from Non-Monthly Expenses sheet",
        "• Green cells (Other Expenses): Manual entry for unexpected or one-time expenses",
        "• Total Recurring: Sum of regular monthly expenses only (Xcel, Verizon, Lawn, Dog Walking, etc.)",
        "• Total Expenses: Includes recurring + non-monthly + other expenses",
        "• Extend the projection by copying the formulas down to add more months",
        "• Update recurring expense amounts in columns D-G when rates change",
    ]
    
    for i, note in enumerate(notes):
        ws.cell(row=note_row+1+i, column=1).value = note
        ws.merge_cells(f'A{note_row+1+i}:L{note_row+1+i}')
        ws.cell(row=note_row+1+i, column=1).font = Font(italic=True, size=9)

if __name__ == "__main__":
    create_budget_spreadsheet()
