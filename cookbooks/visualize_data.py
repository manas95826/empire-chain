from empire_chain.visualizer import DataAnalyzer, ChartFactory

data = """
 **Geek Room**, for the year ending [Insert Date]. The cash flow statement is divided into three sections: Operating Activities, Investing Activities, and Financing Activities.  

---

**Geek Room**  
**Cash Flow Statement**  
For the Year Ended [Insert Date]  
*(All amounts in [currency])*  

### **Cash Flow from Operating Activities:**  
- Net Income (Profit/Loss):                       **₹100,000**  
- Adjustments for:  
  - Depreciation and Amortization:              **₹20,000**  
  - Changes in Working Capital:  
    - Increase in Accounts Receivable:         **(₹10,000)**  
    - Decrease in Accounts Payable:            **(₹5,000)**  
    - Increase in Inventory:                   **(₹15,000)**  
- Other Non-Cash Adjustments:                   **₹5,000**  

**Net Cash Flow from Operating Activities:**   **₹95,000**  

---

### **Cash Flow from Investing Activities:**  
- Purchase of Equipment:                        **(₹50,000)**  
- Sale of Investments:                          **₹30,000**  
- Acquisition of Intangible Assets:             **(₹10,000)**  

**Net Cash Flow from Investing Activities:**   **(₹30,000)**  

---

### **Cash Flow from Financing Activities:**  
- Proceeds from Issuing Equity:                 **₹80,000**  
- Repayment of Borrowings:                      **(₹40,000)**  
- Payment of Dividends:                         **(₹10,000)**  

**Net Cash Flow from Financing Activities:**   **₹30,000**  

---

### **Net Increase in Cash and Cash Equivalents:**  
- **Operating Activities:**                     **₹95,000**  
- **Investing Activities:**                     **(₹30,000)**  
- **Financing Activities:**                     **₹30,000**  

**Net Cash Increase:**                          **₹95,000**  

---

### **Cash and Cash Equivalents at Beginning of Period:**  
- **₹50,000**  

---

### **Cash and Cash Equivalents at End of Period:**  
- **₹145,000**  


"""
    
analyzer = DataAnalyzer()
analyzed_data = analyzer.analyze(data)
        
chart = ChartFactory.create_chart('Bar Chart', analyzed_data)
chart.show()