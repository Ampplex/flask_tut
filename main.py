# for(int = 0; i < 10; i++){
#     printf("%d", i);
# }

# for i in range(11):
#     if i > 3:
#         print("Greater than 3")
#     else:
#         print(i)

# int lst[3] = {1, 2, 3};

# lst = [1,2, 'a', 'hello']
# print(type(lst[1]))

# int greet(){
#     printf("Good evening");
# }

# int main() {
#     greet();
#     return 0;
# }

def greet():
    print("Good evening!")



def calc(num1, num2, op):
    if op == "+":
        print(num1+num2)
    elif op == '-':
        print(num1-num2)

    elif op =='*':
        print(num1*num2)
    elif op == '/':
         print(num1/num2)
    else:
        print("Invalid operator")

def temp():

    try:
        a = {"name": "hello world"}
    except:
        print("invalid syntax")
    
    print("The function is still getting exected")

if __name__ == '__main__':
    # greet()
    # print(add(3,5))
    # calc(10, 5, '%')

    # obj = {'sddf': 3, 'name': 'harry', 'obj2': {'number': 23, 'place': 'Pune'}}

    # print(obj['obj2'])

    # temp()

    lst2 = [1,2,3]

    lst2.append(56)
    lst2.append(23)

    print(lst2)

    lst2.pop()
    lst2.pop()

    print(lst2)