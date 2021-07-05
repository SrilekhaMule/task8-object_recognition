#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:blue;" >Details</h1>')
    print('''<pre>
    License No : 2015007259
    Make : BABA HYUNDAI 
    Registration Date : 1/12/2011
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine Number : IVK3N1734538
    Chassis Number : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:blue;" >Vehicle information</h1>')
    print("No data available for this number...")
    print("</body>")
