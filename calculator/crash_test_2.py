#a = list(range(0,16,2))
#squares = [x*x for x in range(0,20,2)]
#print(squares)
#c = "2+3-4"
#print(c[1])

def brackets(a):
    num_in_brackets = []
    pos_in_brackets = []
    n = 0
    for i in a:
        if i == "(":
            while i != ")":
                if i in [int,float]:
                    var = float(i)
                    num_in_brackets.append(var)
                else:
                    num_in_brackets.append(i)
                pos_in_brackets.append(n)
        n = n + 1

    print(num_in_brackets,pos_in_brackets)

if __name__ == "__main__":
    brackets(input())