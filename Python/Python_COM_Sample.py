import win32com.client

o = win32com.client.Dispatch("Excel.Application")
o.Visible = 1
o.Workbooks.Add()
o.Cells(1,1).Value = "Hello"