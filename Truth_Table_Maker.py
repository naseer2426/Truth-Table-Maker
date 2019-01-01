#Truth Table Maker one
print("""This program will make the truth table for any boolean expression.
Variables - English Alphabets
And  .
Or  +
Not  '""")
while True:
    print()
    expr=input('Please enter the boolean expression: ')
    def remove_repeat(l):
        list_to_return=[]
        for item in l:
            if not(item in list_to_return):
                list_to_return.append(item)
        return list_to_return
    def remove_spaces(ex):
        string=''
        for letter in ex:
            if not(letter==' '):
                string+=letter
        return string

    def check_brackets(s):
        b=0
        d=0
        while (b<=len(s)-1)and(d>=0):
            if s[b]=='(':
                d+=1
            elif s[b]==')':
                d-=1
            b+=1
        if d==0:
            return True
        else:
            return False
    check=True
    while check:
        #Make list of all variables
        variables=[]
        exp=''
        for letter in expr:
            if (ord(letter)<65)or(ord(letter)>122)or(90<ord(letter)<97):
                exp+=letter
            else:
                variables.append(letter.upper())
                exp+=letter.upper()
        variables=remove_repeat(variables)
        variables.sort()

        exp=remove_spaces(exp)

        def check_expression(exp):
            if len(exp)==1:
                if not(exp in variables):
                    return False
                else:
                    return True
            elif (not(exp[-1] in variables))and(exp[-1]!='(')and(exp[-1]!=')')and(exp[-1]!="'"):
                return False
            else:
                i=0
                while i<=(len(exp)-2):
                    next_letter=exp[i+1]
                    if not(exp[i] in variables)and not(exp[i] in ['+','.','(',')',"'"]):
                        return False
                        break
                    if exp[i] in variables:
                        if (next_letter!='.')and(next_letter!='+')and(next_letter!=')')and(next_letter!="'"):
                            return False
                            break
                    if exp[i]=='+':
                        if not(next_letter in variables)and(next_letter!='('):
                            return False
                            break
                    if exp[i]=='.':
                        if not(next_letter in variables)and(next_letter!='('):
                            return False
                            break
                    if exp[i]=='(':
                        if not(next_letter in variables)and(next_letter!='('):
                            return False
                            break
                    if exp[i]==')':
                        if (next_letter!='.')and(next_letter!=')')and(next_letter!='+')and(next_letter!="'"):
                            return False
                            break
                    if exp[i]=="'":
                        if (next_letter!='+')and(next_letter!='.')and(next_letter!=')')and(next_letter!="'"):
                            return False
                            break
                    if i==(len(exp)-2):
                        return True
                        break
                    i+=1
        if not(check_expression(exp)) or not(check_brackets(exp)):
            print()
            if not(check_expression(exp)):
                expr=input('Invalid expression!. Please input the correct expression: ')
            elif not(check_brackets(exp)):
                expr=input('There is a problem in your brackets. Please input the correct expression: ')
        check=not(check_expression(exp)) or not(check_brackets(exp))
    exp2=''
    for stuff in exp:
        if stuff in variables:
            exp2+='('+stuff+')'
        else:
            exp2+=stuff
    dash_to_keep=[]
    it=0
    while it<=len(exp2)-1:
        m=0
        if exp2[it]=="'":
            it2=it
            dash_number=1
            while (exp2[it2]=="'")and(it2+1<len(exp2)-1):
                if exp2[it2+1]=="'":
                    dash_number+=1
                it2+=1
                m+=1
            if (it2+1==len(exp2)-1)and(exp2[-1]=="'"):
                dash_number+=1
                m+=2
            if dash_number%2==1:
                dash_to_keep.append(it)
        if m==0:
            it+=1
        else:
            it+=m
    exp3=''
    e=0
    while e<=len(exp2)-1:
        if e in dash_to_keep:
            exp3+="'"
        elif exp2[e]=="'":
            exp3+=''
        else:
            exp3+=exp2[e]
        e+=1
    exp2=exp3

    dash_list=[]
    n=0
    while n<=len(exp2)-1:
        if exp2[n]=="'":
            dash_list.append(n)
        n+=1
    not_list=[]
    for index in dash_list:
        if exp2[index-1]==')':
            count=1
            back=1
            while count!=0:
                if exp2[index-1-back]==')':
                    count+=1
                elif exp2[index-1-back]=='(':
                    count-=1
                back+=1
            not_list.append(index-back)

    final_exp=''
    iteration=0
    while iteration<=len(exp2)-1:
        if iteration in not_list:
            final_exp+='not'+exp2[iteration]
        elif exp2[iteration]=='.':
            final_exp+=' and '
        elif exp2[iteration]=='+':
            final_exp+=' or '
        elif exp2[iteration]=="'":
            final_exp+=''
        else:
            final_exp+=exp2[iteration]
        iteration+=1
    def boolean_to_number(b):
        if b==True:
            return '1'
        else:
            return '0'
    def number_to_boolean(num):
        if num=='1':
            return 'True'
        else:
            return 'False'
    for variable in variables:
        print(variable+'  ',end='')
    print('Output')
    for final_number in range(2**len(variables)):
        final_number=str(bin(final_number))[2:]
        if len(final_number)!=len(variables):
            final_number=((len(variables))-(len(final_number)))*'0'+final_number
        m=0
        while m<=len(final_number)-1:
            exec(variables[m]+'='+number_to_boolean(final_number[m]))
            m+=1
        exec('output='+final_exp)
        output=boolean_to_number(output)
        o=0
        while o<=len(final_number)-1:
            print(final_number[o]+'  ',end='')
            o+=1
        print('  '+output)
