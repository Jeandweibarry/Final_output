import tkinter as tk
import sqlite3

import Inside_the_app

#con = sqlite3.connect("D:\\Users\\Jeff Bayhon\\Downloads\\employee_personal_info.db")
#cursor = con.cursor()

import guiclass

gui_design2 = guiclass.employee_personal_info()

root = tk.Tk()
root.geometry('1000x1500')
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# COMMANDS --------------------------------------------------------------------------------------------------------------------------------------------------------

def Search_data():
    #GET EMPLOYEE DATA
    employee_number = employee_numbertxt.get()
    print(employee_number)
    cursor.execute(f"SELECT * FROM basic_info WHERE employee_number = {employee_number}")
    employee = cursor.fetchone()
    if employee:
        Departmenttxt.insert(0, employee[8])
        firstnametxt.insert(0, employee[0])
        middlenametxt.insert(0, employee[1])
        surnametxt.insert(0, employee[2])
        civilstatustxt.insert(0, employee[7])
        qualified_dependent_statustxt.insert(0, employee[10])
        paydatetxt.insert(0, employee[12])
        employee_statustxt.insert(0, employee[11])
        designationtxt.insert(0, employee[9])

    con.close()

    print("Data transfered...")

def Gross_Income():
    income1 = float(Rate_hour1txt.get()) * float(No_Hours1txt.get())
    income2 = float(Rate_hour2txt.get()) * float(No_Hours2txt.get())
    income3 = float(Rate_hour3txt.get()) * float(No_Hours3txt.get())
    grossincome = income1 + income2 + income3

    Income1txt.insert(0, income1)
    Income2txt.insert(0, income2)
    Income3txt.insert(0, income3)
    Gross_incometxt.insert(0, grossincome)

def Net_Income():
    gross_income = float(Gross_incometxt.get())
    #SSS contribution computation
    if gross_income < 4250:
        sss_contribution = 180
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 4250 and gross_income <= 4749.99:
        sss_contribution = 202.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 4750 and gross_income <= 5249.99:
        sss_contribution = 225.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 5250 and gross_income <= 5749.99:
        sss_contribution = 247.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 5750 and gross_income <= 6249.99:
        sss_contribution = 270.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 6250 and gross_income <= 6749.99:
        sss_contribution = 292.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 6750 and gross_income <= 7249.99:
        sss_contribution = 315.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 7250 and gross_income <= 7749.99:
        sss_contribution = 337.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 7750 and gross_income <= 8249.99:
        sss_contribution = 360.0
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 8250 and gross_income <= 8749.99:
        sss_contribution = 382.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 8750 and gross_income <= 9249.99:
        sss_contribution = 405.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 9250 and gross_income <= 9749.99:
        sss_contribution = 427.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 9750 and gross_income <= 10249.99:
        sss_contribution = 450.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 10250 and gross_income <= 10749.99:
        sss_contribution = 472.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 10750 and gross_income <= 11249.99:
        sss_contribution = 495.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 11250 and gross_income <= 11749.99:
        sss_contribution = 517.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 11750 and gross_income <= 12249.99:
        sss_contribution = 540.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 12250 and gross_income <= 12749.99:
        sss_contribution = 562.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 12750 and gross_income <= 13249.99:
        sss_contribution = 585.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 13250 and gross_income <= 13749.99:
        sss_contribution = 607.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 13750 and gross_income <= 14249.99:
        sss_contribution = 630.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 14250 and gross_income <= 14749.99:
        sss_contribution = 652.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 14750 and gross_income <= 15249.99:
        sss_contribution = 675.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 15250 and gross_income <= 15749.99:
        sss_contribution = 697.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 15750 and gross_income <= 16249.99:
        sss_contribution = 720.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 16250 and gross_income <= 16749.99:
        sss_contribution = 742.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 16750 and gross_income <= 17249.99:
        sss_contribution = 765.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 17250 and gross_income <= 17749.99:
        sss_contribution = 787.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 17750 and gross_income <= 18249.99:
        sss_contribution = 810.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 18250 and gross_income <= 18749.99:
        sss_contribution = 832.50
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 18750 and gross_income <= 19249.99:
        sss_contribution = 855.00
        sss_contritxt.insert(0, sss_contribution)
    elif gross_income >= 19250 and gross_income <= 19749.99:
        sss_contribution = 877.50
        sss_contritxt.insert(0, sss_contribution)
    else:
        sss_contribution = 900.00
        sss_contritxt.insert(0, sss_contribution)

    #PhilHealth contribution computation
    if gross_income == 10000:
        PhilHealth_contri = 450.00
        philhealth_contritxt.insert(0, PhilHealth_contri)
    elif gross_income >= 1000.01 and gross_income <= 89999.99:
        PhilHealth_contri = gross_income * 0.0450
        philhealth_contritxt.insert(0, PhilHealth_contri)
    else:
        PhilHealth_contri = 4050.00
        philhealth_contritxt.insert(0, PhilHealth_contri)

    Pagibig_contri = 100
    pagibig_contritxt.insert(0, Pagibig_contri)

    #Income Tax contribution computation
    if 0.00 < gross_income <=10417.00:
        withholding_tax = 0
        incometax_contritxt.insert(0, withholding_tax)
    elif 10417.00 < gross_income <= 16666.00:
        over = gross_income - 10417.00
        withholding_tax = 0 + (over * 0.15)
        incometax_contritxt.insert(0, withholding_tax)
    elif 16666.00 < gross_income <= 33332.00:
        over = gross_income - 16667.00
        withholding_tax = 937.50 + (over * 0.2)
        incometax_contritxt.insert(0, withholding_tax)
    elif 33332.00 < gross_income <= 83332.00:
        over = gross_income - 33333.00
        withholding_tax = 4270.70 + (over * 0.25)
        incometax_contritxt.insert(0, withholding_tax)
    elif 83332.00 < gross_income <= 333332.00:
        over = gross_income - 83333.00
        withholding_tax = 16770.70 + (over * 0.3)
        incometax_contritxt.insert(0, withholding_tax)
    else:
        over = gross_income - 333333.00
        withholding_tax = 91770.70 + (over * 0.35)
        incometax_contritxt.insert(0, withholding_tax)

#COMPUTATIONS
    sssloan = float(sss_loantxt.get())
    pagibigloan = float(pagibig_loantxt.get())
    facultydeposit = float(faculty_savings_deposittxt.get())
    facultyloan = float(faculty_savings_loantxt.get())
    salaryloan = float(salary_loantxt.get())
    otherloan = float(other_loantxt.get())

    otherdeduc = sssloan + pagibigloan + facultydeposit + facultyloan + salaryloan + otherloan

    totaldeduc = sss_contribution + PhilHealth_contri + Pagibig_contri + withholding_tax + otherdeduc
    total_deductxt.insert(0, totaldeduc)

    #COMPUTATION FOR NET INCOME
    netincome = gross_income - totaldeduc
    Net_incometxt.insert(0, netincome)

def Clear_data():
    employee_numbertxt.delete(0, 'end')
    Departmenttxt.delete(0, 'end')
    Rate_hour1txt.delete(0, 'end')
    No_Hours1txt.delete(0, 'end')
    Income1txt.delete(0, 'end')
    Rate_hour2txt.delete(0, 'end')
    No_Hours2txt.delete(0, 'end')
    Income2txt.delete(0, 'end')
    Rate_hour3txt.delete(0, 'end')
    No_Hours3txt.delete(0, 'end')
    Income3txt.delete(0, 'end')
    Gross_incometxt.delete(0, 'end')
    Net_incometxt.delete(0, 'end')
    firstnametxt.delete(0, 'end')
    middlenametxt.delete(0, 'end')
    surnametxt.delete(0, 'end')
    civilstatustxt.delete(0, 'end')
    qualified_dependent_statustxt.delete(0, 'end')
    paydatetxt.delete(0, 'end')
    employee_statustxt.delete(0, 'end')
    designationtxt.delete(0, 'end')
    sss_contritxt.delete(0, 'end')
    philhealth_contritxt.delete(0, 'end')
    pagibig_contritxt.delete(0, 'end')
    incometax_contritxt.delete(0, 'end')
    sss_loantxt.delete(0, 'end')
    pagibig_loantxt.delete(0, 'end')
    faculty_savings_deposittxt.delete(0, 'end')
    faculty_savings_loantxt.delete(0, 'end')
    salary_loantxt.delete(0, 'end')
    other_loantxt.delete(0, 'end')
    total_deductxt.delete(0, 'end')


    self.regulardeduc = float(self.sss_contritxt.get()) + float(self.philhealth_contritxt.get()) + float(
    self.pagibig_contritxt.get()) + float(self.incometax_contritxt.get())
    self.otherdeduc = float(self.sss_loantxt.get()) + float(self.pagibig_loantxt.get()) + float(
    self.faculty_savings_deposittxt.get()) + float(self.faculty_savings_loantxt.get()) + float(
    self.salary_loantxt.get()) + float(self.other_loantxt.get())

def Save_data():


    regulardeduc = float(sss_contritxt.get()) + float(philhealth_contritxt.get()) + float(pagibig_contritxt.get()) + float(incometax_contritxt.get())
    otherdeduc = float(sss_loantxt.get()) + float(pagibig_loantxt.get()) + float(faculty_savings_deposittxt.get()) + float(faculty_savings_loantxt.get()) + float(salary_loantxt.get()) + float(other_loantxt.get())

    employee_number = employee_numbertxt.get()
    basic_income = Income1txt.get()
    hononarium_income = Income2txt.get()
    other_income = Income3txt.get()
    gross_income = Gross_incometxt.get()
    regular_deduction = regulardeduc.get()
    other_deduction = otherdeduc.get()
    total_deduction = total_deductxt.get()
    net_income = Net_incometxt.get()

    query1 = """INSERT INTO income_tbl (employee_number, basic_income, hononarium_income, other_income, gross_income, regular_deduction, other_deduction, total_deduction, net_income) VALUES(?,?,?,?,?,?,?,?,?)"""

    query1inp = (employee_number, basic_income, hononarium_income, other_income, gross_income, regular_deduction, other_deduction, total_deduction, net_income)

    con.execute(query1, query1inp)

    con.commit()
    con.close()
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

#CANVAS ------------------------------------------------------------------------------------------------------------------------------------
main_frame = gui_design2.create_canvas(0, 0)

# FRAME -----------------------------------------------------------------------------------------------------------------
frame1 = gui_design2.create_frames(main_frame, 30, 120, 'light pink',930, 1000)

#PICTURE / BACKGROUND -----------------------------------------------------------------------------------------------------------------
# picture = gui_design2.picture(frame1,50, 80,200,200, 'C:\\Users\\Stan Lee\\Downloads\\Profile.jpg')

#Title
titleheading = gui_design2.label2(main_frame,370, 10, ' PAYROLL',35, 'bold')

frameheading = gui_design2.label2(frame1,50, 30, 'EMPLOYEE PERSONAL INFO:',15, 'bold')

#Buttons
searchbutton = gui_design2.create_button(frame1,Search_data,300, 340, 'Search', 'yellow', 12, 1, 7)

grossbutton = gui_design2.create_button(frame1,Gross_Income,500, 850, 'Gross Income', '#0CC0DF', 12, 1, 8)
netbutton = gui_design2.create_button(frame1,Net_Income,590, 850, 'Net Income', '#0CC0DF', 12, 1, 8)
savebutton = gui_design2.create_button(frame1,'',680, 850, 'Save', 'teal', 9, 1, 8)
updatebutton = gui_design2.create_button(frame1,'',750, 850, 'Update', 'teal', 10, 1, 8)
newbutton = gui_design2.create_button(frame1,Clear_data,825, 850, 'New', 'yellow', 8, 1, 8)

#Labels (1st column)
employee_numberlbl = gui_design2.label1(frame1,50, 310, 'Employee Number')
Search_Employeelbl = gui_design2.label1(frame1,50, 340, 'Search Employee')
Departmentlbl = gui_design2.label1(frame1,50, 370, 'Department')

Basic_Incomelbl = gui_design2.label4(frame1,50, 410, 'Basic Income')

Rate_hour1lbl = gui_design2.label1(frame1,50, 450, 'Rate_hour')
No_Hours1lbl = gui_design2.label1(frame1,50, 480, 'No. of hours/Cut off')
Income1lbl = gui_design2.label1(frame1,50, 510, 'Income/Cut off')

Hononarium_Incomelbl = gui_design2.label4(frame1,50, 550, 'Hononarium Income')

Rate_hour2lbl = gui_design2.label1(frame1,50, 590, 'Rate_hour')
No_Hours2lbl = gui_design2.label1(frame1,50, 620, 'No. of hours/Cut off')
Income2lbl = gui_design2.label1(frame1,50, 650, 'Income/Cut off')

Other_Incomelbl = gui_design2.label4(frame1,50, 690, 'Other Income')

Rate_hour3lbl = gui_design2.label1(frame1,50, 730, 'Rate_hour')
No_Hours3lbl = gui_design2.label1(frame1,50, 760, 'No. of hours/Cut off')
Income3lbl = gui_design2.label1(frame1,50, 790, 'Income/Cut off')

Summary_Incomelbl = gui_design2.label4(frame1,50, 830, 'Summary Income')

Gross_incomelbl = gui_design2.label1(frame1,50, 870, 'Gross Income')
Net_incomelbl = gui_design2.label1(frame1,50, 900, 'Net Income')


#Labels(2nd column)

firstnamelbl = gui_design2.label1(frame1,500, 40, 'First Name')
middlenamelbl = gui_design2.label1(frame1,500, 70, 'Middle Name')
surnamelbl = gui_design2.label1(frame1,500, 100, 'Surname')
civilstatuslbl = gui_design2.label1(frame1,500, 130, 'Civil Status')
qualified_dependent_statuslbl = gui_design2.label1(frame1,500, 160, 'Qualified Dependent Status')
paydatelbl = gui_design2.label1(frame1,500, 190, 'Paydate')
employee_statuslbl = gui_design2.label1(frame1,500, 220, 'Employee Status')
designationlbl = gui_design2.label1(frame1,500, 250, 'Designation')

regular_deductionslbl = gui_design2.label4(frame1,500, 300, 'Regular Deductions')

sss_contrilbl = gui_design2.label1(frame1,500, 350, 'SSS Contribution')
philhealth_contrilbl = gui_design2.label1(frame1,500, 380, 'PhilHealth Contribution')
pagibig_contrilbl = gui_design2.label1(frame1,500, 410, 'Pag Ibig Contribution')
incometax_contrilbl = gui_design2.label1(frame1,500, 440, 'Income Tax Contribution')

other_deductionslbl = gui_design2.label4(frame1,500, 490, 'Other Deductions')

sss_loanlbl = gui_design2.label1(frame1,500, 540, 'SSS Loan')
pagibig_loanlbl = gui_design2.label1(frame1,500, 570, 'Pag Ibig Loan')
faculty_savings_depositlbl = gui_design2.label1(frame1,500, 600, 'Faculty Savings Deposit')
faculty_savings_loanlbl = gui_design2.label1(frame1,500, 630, 'Faculty Savings Loan')
salary_loanlbl = gui_design2.label1(frame1,500, 660, 'Salary Loan')
other_loanlbl = gui_design2.label1(frame1,500, 690, 'Other Loan')

deduction_summarylbl = gui_design2.label4(frame1,500, 740, 'Deduction Summary')

total_deduclbl = gui_design2.label1(frame1,500, 790, 'Total Deductions')


#textbox(1st column)

employee_numbertxt = gui_design2.textbox1(frame1,300, 310, 20)

Departmenttxt = gui_design2.textbox1(frame1,300, 370, 20)
Rate_hour1txt = gui_design2.textbox1(frame1,300, 450, 20)
No_Hours1txt = gui_design2.textbox1(frame1,300, 480, 20)
Income1txt = gui_design2.textbox1(frame1,300, 510, 20)
Rate_hour2txt = gui_design2.textbox1(frame1,300, 590, 20)
No_Hours2txt = gui_design2.textbox1(frame1,300, 620, 20)
Income2txt = gui_design2.textbox1(frame1,300, 650, 20)
Rate_hour3txt = gui_design2.textbox1(frame1,300, 730, 20)
No_Hours3txt = gui_design2.textbox1(frame1,300, 760, 20)
Income3txt = gui_design2.textbox1(frame1,300, 790, 20)
Gross_incometxt = gui_design2.textbox1(frame1,300, 870, 20)
Net_incometxt = gui_design2.textbox1(frame1,300, 900, 20)


#2nd Column

firstnametxt = gui_design2.textbox1(frame1,750, 40, 18)
middlenametxt = gui_design2.textbox1(frame1,750, 70, 18)
surnametxt = gui_design2.textbox1(frame1,750, 100, 18)
civilstatustxt = gui_design2.textbox1(frame1,750, 130, 18)
qualified_dependent_statustxt = gui_design2.textbox1(frame1,770, 160, 16)
paydatetxt = gui_design2.textbox1(frame1,750, 190, 18)
employee_statustxt = gui_design2.textbox1(frame1,750, 220, 18)
designationtxt = gui_design2.textbox1(frame1,750, 250, 18)

sss_contritxt = gui_design2.textbox1(frame1,750, 350, 18)
philhealth_contritxt = gui_design2.textbox1(frame1,750, 380, 18)
pagibig_contritxt = gui_design2.textbox1(frame1,750, 410, 18)
incometax_contritxt = gui_design2.textbox1(frame1,750, 440, 18)

sss_loantxt = gui_design2.textbox1(frame1,750, 540, 18)
pagibig_loantxt = gui_design2.textbox1(frame1,750, 570, 18)
faculty_savings_deposittxt = gui_design2.textbox1(frame1,750, 600, 18)
faculty_savings_loantxt = gui_design2.textbox1(frame1,750, 630, 18)
salary_loantxt = gui_design2.textbox1(frame1,750, 660, 18)
other_loantxt = gui_design2.textbox1(frame1,750, 690, 18)

total_deductxt = gui_design2.textbox1(frame1,750, 790, 18)


root.resizable(False, False)
root.mainloop()
