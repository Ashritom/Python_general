def vowels():
    count=0
    x=str(input('enter a word: '))
    for char in x:
        if char in 'aeiouAEIOU': 
           count=count+1
    return count
def main():
    print(vowels())
main()
