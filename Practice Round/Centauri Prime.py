# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    bob = 'Bob'
    alice = 'Alice'
    nobody = 'nobody'
    
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    if kingdom[-1] in vowels:
        ruler = alice
    elif kingdom[-1] == 'y' or kingdom[-1] == 'Y':
        ruler = nobody
    else:
        ruler = bob
    
    return ruler

def main():
  # Get the number of test cases
  T = int(input())
  for t in range(T):
    # Get the kingdom
    kingdom = input()
    print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))

if __name__ == '__main__':
  main()
