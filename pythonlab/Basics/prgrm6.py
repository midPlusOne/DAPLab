#usage of args and kwargs
print("Using *args")
def func1(*args):
    sum = 0
    for i in args:
        sum += i
    print("Sum of [",*args,"]: ",sum)

func1(1,2,3)
func1(1,2,3,4,5,6,7,8,9)


print("\nUsing **kwargs")
def func2(**kwargs):
    for key,val in kwargs.items():
        print("%s == %s"%(key,val))
        
func2(first_name = "John",middle_name="Doe",last_name="Gi")