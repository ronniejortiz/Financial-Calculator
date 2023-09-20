#Opening Menu
print("What are you looking to find?")
print("\n Options:\n \n (1)PV, (2)FV, (3)Return, (4)Levered Beta, (5)Unlevered Beta, (6)DDM, (7)Expected Growth, (8)Terminal Value \n")
choice = str(input())

def main(choice): 
  # PV Calculation
  if choice == "PV" or choice == "1":
    n = float(input("What is the number of time periods: "))
    i = float(input("What is the interest rate (%): "))/100
    fv = float(input("What is the future value: "))
    pmt = float(input("What is the payment: "))
  
    def pv_val(n, i, fv, pmt):
      fv_val = (fv / ((1 + i) ** n))
      pmt_val = pmt * ((1-(1/((1 + i) ** n)))/i)
      total_val = fv_val + pmt_val
      return total_val
  
    if n >= 0 and i >= 0 and fv >= 0 and pmt >= 0:
      print("The present value is: $", round(pv_val(n, i, fv, pmt),2))
    else:
      print("Invalid input")
  
  # FV Calculation
  elif choice == "FV" or choice == "2":
    n = float(input("What is the number of time periods: "))
    i = float(input("What is the interest rate (%): "))/100
    pv = float(input("What is the present value: "))
    pmt = float(input("What is the payment: "))
    
    def future_val(n, i, pv, pmt):
      pv_val = (pv * ((1 + i) ** n))
      pmt_val = pmt * ((((1 + i) ** n)-1)/i)
      return pv_val + pmt_val
  
    if n >= 0 and i >= 0 and pv >= 0 and pmt >= 0:
      print("The future value is: $", round(future_val(n, i, pv, pmt)))
    else:
      print("Invalid input")
  
  # I/Y Calculation
  elif choice == "Return" or choice == "3":
    n = float(input("What is the number of time periods: "))
    pv = float(input("What is the present value: "))
    fv = float(input("What is the future value: "))
    
    def interest_rate(n, pv, fv):
      i_val = ((fv/pv) ** (1 / n))-1
      return i_val * 100
  
    if n >= 0 and pv >= 0 and fv >= 0:
      print("The rate of return is: ", round(interest_rate(n, pv, fv),1),"%")
    else:
      print("Invalid input")
  
  #Levered Beta Calculation
  elif choice == "Levered Beta" or choice == "4":
    un_beta = float(input("What is the unlevered beta: "))
    tax_rate = float(input("What is the tax rate (%): "))
    de = float(input("What is the debt-to-equity ratio: "))
    
    def levered_beta(un_beta, tax_rate, de):
      levered_beta = (1 + ((1 - (tax_rate / 100)) * de)) * un_beta
      return levered_beta
      
    if un_beta >= 0 and tax_rate >= 0 and de >= 0:
      print("The levered beta is: ", round(levered_beta(un_beta, tax_rate, de),2))
    else:
      print("Invalid input")
  
  #Unlevered Beta Calculation
  elif choice == "Unlevered Beta" or choice == "5":
    levered_beta = float(input("What is the levered beta: "))
    tax_rate = float(input("What is the tax rate (%): "))
    de = float(input("What is the debt-to-equity ratio: "))
    
    def unlevered_beta(levered_beta, tax_rate, de):
      unlevered_beta = levered_beta / ((1 + ((1 - (tax_rate / 100)) * de)))
      return unlevered_beta
      
    if levered_beta >= 0 and tax_rate >= 0 and de >= 0:
      print("The unlevered beta is: ", round(unlevered_beta(levered_beta, tax_rate, de),2))    
    else:
      print("Invalid input")
  
  #DDM Calculation
  elif choice == "DDM" or choice == "6":
    div = float(input("What is the current dividend: $"))
    div_growth = float(input("What is the dividend growth rate (%): "))
    wacc = float(input("What is the WACC (%): "))
    
    def ddm(div, div_growth, wacc):
      valuation = ((1 + (div_growth / 100)) * div) / ((wacc - div_growth) / 100)
      return valuation
      
    if div_growth >= 0 and wacc >= 0:
      print("The stock is worth: $", round(ddm(div, div_growth, wacc),2))
    else:
      print("Invalid input")
  
  #Expected Growth Calculation
  elif choice == "Expected Growth" or choice == "7":
    retention = float(input("What is the retention rate (%): "))
    roe = float(input("What is the ROE (%): "))
    delta_roe = float(input("What is the change in ROE (%): "))
    
    def expected_growth(retention, roe, delta_roe):
      expected_growth = (retention * (roe/100)) + delta_roe
      return expected_growth
      
    if retention >= 0 and roe >= 0:
      print("The expected growth is: ", round(expected_growth(retention, roe, delta_roe),2),"%")
    else:
      print("Invalid input.")
  
  #Terminal Value Calculation
  elif choice == "Terminal Value" or choice == "8":
    cf = float(input("What is the final cash flow: $"))
    g = float(input("What is the growth rate (%): "))
    wacc = float(input("What is the WACC (%): "))
    years = float(input("How many years away is the TV: "))
    
    def terminal_value(cf, g, wacc, years):
      terminal_value = ((cf * (1 + (g / 100))) / ((wacc - g) / 100)) / ((1 + (wacc / 100)) ** years)
      return terminal_value
      
    if g >= 0 and wacc >= 0 and years >= 0:
      print("\nThe terminal value is: $", round(terminal_value(cf, g, wacc, years),2))    
    else:
      print("Invalid input.")

main(choice)
print("\nStart again? Y/N")
choice = input()
if choice == "Y" or choice == "y":
  print("\n Options:\n \n (1)PV, (2)FV, (3)Return, (4)Levered Beta, (5)Unlevered Beta, (6)DDM, (7)Expected Growth, (8)Terminal Value \n")
  choice = input()
  main(choice)
else:
  print("Goodbye!")
  quit()