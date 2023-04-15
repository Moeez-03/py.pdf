import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the XML file
tree = ET.parse('company.xml')
root = tree.getroot()

# Create a PDF file
c = canvas.Canvas("Assignment2.pdf", pagesize=letter)

# Set the font and font size
c.setFont("Helvetica", 12)

# Iterate over the XML data and add it to the PDF
for division in root.findall('Division'):
    c.drawString(100, 700, f"Division: {division.attrib['DNAME']} ({division.attrib['DID']})")
    c.drawString(100, 675, f"Location: {division.attrib['LOCATION']}")
    
    for project in division.findall('Project'):
        c.drawString(100, 625, f"Project: {project.attrib['PNAME']} ({project.attrib['PID']})")
        c.drawString(125, 605, f"Budget: {project.attrib['BUDGET']}")
        c.drawString(125, 565, "Employees:")
        
        employees = project.findall('Employee')
        num_employees = len(employees)
        
        for i, employee in enumerate(employees):
            y_offset = 520 - 30*i
            c.drawString(150, y_offset-10, f"- {employee.attrib['ENAME']} ({employee.attrib['EID']})")
            c.drawString(175, y_offset-80, f"Office: {employee.attrib['OFFICE']}")
            c.drawString(175, y_offset-150, f"Birthdate: {employee.attrib['BIRTHDATE']}")
            c.drawString(175, y_offset-220, f"Salary: {employee.attrib['SALARY']}")
            c.drawString(175, y_offset-290, f"Division: {employee.attrib['DID']}")
            
            c.drawString(125, y_offset-360, "Assignments:")
            for assign in employee.findall('Assign'):
                c.drawString(150, y_offset-380, f"- {assign.attrib['EID']} assigned {assign.attrib['PID']} assigned {assign.attrib['HOURS']} hours")
        
        # Add a page break after each project
        c.showPage()

# Save the PDF file
c.save()
