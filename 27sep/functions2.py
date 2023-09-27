def func(a, b, c=10, d=11):
    print(a, b, c, d)


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 4)

func(c='c', a='a', d='d', b='b')
func(1, 2, d=4)