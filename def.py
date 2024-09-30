x=input()
def check_password(x):
    k=0
    p=0
    l=0
    if len(x)>=10:
        for i in x:
            if i.isdigit():
                k=k+1
        if k>3:
            #print('Perfect password')
            for i in x:
                if i.isupper() :
                    p=1
            for j in x:
                if j=='!' or j=='@' or j=='#' or j=='$' or j=='%' or j=='*':
                    l=1
            if p+l==2:
                print('Perfect password')
            else:
                print('Easy peasy')
        else:
            print('Easy peasy')
    else:
        print('Easy peasy')
check_password(x)