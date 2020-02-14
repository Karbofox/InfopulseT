#Task 1
s = '11-3.0'
if s.count('-') == 1 and s[0] == '-':
    s = s[1:]
if s.count('.') == 1:
    s = s.replace('.','')
print('Task #1')
print('Is string \"',s,'\"',' a number?',' -',s.count('-') == 0 and s.count('.') == 0 and s.isnumeric(),'\n')

#Task 2
s1 = '   3.\n    4\t  2 1'
print('Task #2')
print(s1.count(' '),'space(s) is(are) in string:\"',s1,'\"','\n')

#Task 3
s2 = ' nfnf.dsf.'
print('Task #3')
print(s2.count('.'),'dots(.) is(are) in string:\"',s2,'\"','\n')

#Task 4
s3 = 'Homework'
s3 = ' '*46 + s3 + ' '*46
print('Task #4')
print('The result string is:', s3,'\n')

#Task 5
import string
s4 = 'Great news, everyone!\n What today?'
print('First letter capitalized: ',s4.title())
