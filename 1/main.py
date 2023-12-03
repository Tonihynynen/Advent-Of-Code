
def main():
    file_name = "input.txt"
    with open(file_name, "r") as file:
        totals = []
        for line in file:
            linevalue = ""
            first = 0;
            last = 0;
            # ----->
            for char in line:
                if char.isnumeric():
                    first = char
                    break
            # <-------
            for char in line[::-1]:
                if char.isnumeric():
                    last = char
                    break
            linevalue = f"{first}{last}"
            totals.append(int(linevalue))
        answer = sum(totals)
        print(answer)  

if __name__ == "__main__":
    main()


    