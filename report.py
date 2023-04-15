import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Load the XML file
tree = ET.parse('company.xml')
root = tree.getroot()

# Create a PDF file
c = canvas.Canvas("company.pdf", pagesize=letter)

# Set the font and font size
c.setFont("Helvetica", 12)

# Iterate over the XML data and add it to the PDF
for division in root.findall('Division'):
    c.drawString(100, 700, f"Division: {division.attrib['DNAME']} ({division.attrib['DID']})")
    c.drawString(100, 675, f"Location: {division.attrib['LOCATION']}")
    c.drawString(100, 625, "Projects:")
    for project in division.findall('Project'):
        c.drawString(125, 580, f"- {project.attrib['PNAME']} ({project.attrib['PID']})")
        c.drawString(150, 560, f"Budget: {project.attrib['BUDGET']}")
        c.drawString(150, 520, "Employees:")
        for employee in project.findall('Employee'):
            c.drawString(175, 450, f"- {employee.attrib['ENAME']} ({employee.attrib['EID']})")
            c.drawString(200, 420, f"Office: {employee.attrib['OFFICE']}")
            c.drawString(200, 390, f"Birthdate: {employee.attrib['BIRTHDATE']}")
            c.drawString(200, 340, f"Salary: {employee.attrib['SALARY']}")
            c.drawString(200, 300, f"Division: {employee.attrib['DID']}")
            
        c.drawString(100, 265, "Assignments:")
        for assign in project.findall('Assign'):
            c.drawString(125, 220, f"- {assign.attrib['EID']} assigned {assign.attrib['PID']} assigned {assign.attrib['HOURS']} hours")

    # Add a page break
    c.showPage()

# Save the PDF file
c.save()
