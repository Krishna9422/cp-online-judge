https://github.com/Krishna9422/cp-online-judgeimport sys

def game_result(n):
    cont = 0
    while n > 1:
        cont += 1
        if cont % 2 == 1:
            n = (n + 8) // 9
        else:
            n = (n + 1) // 2

    return "Stan wins." if cont % 2 == 1 else "Ollie wins."

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == 1:
            print("Stan wins.")
            continue
        print(game_result(n))

if __name__ == "__main__":
    main()
