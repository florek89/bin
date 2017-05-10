
# Wprowadzenie danych
while True:
    var = 1
    var2 = 1
    try:
        x_input = input("Enter a number and -after space- numeral system (2 or 10): ")
        x = x_input.split()
        # Sprawdzenie czy podano więcej zmiennych niż dwie
        if len(x) > 2:
            var = 0
            print("Too much variables!")

        if var == 1:
            x2_input = int(x[0])
            x3_input = int(x[1])
            test = x[0]

            score = ""
            temp = str(x2_input)
            power = 0
            number = 0
            binar_numbers = (1, 0)
            # Sprawdzenie czy podano poprawny system liczbowy
            if x3_input != 2 and x3_input != 10:
                    print("Wrong numeral system!")
            else:
                # Konwertowanie z systemu dziesiętnego na binarny
                if x3_input == 10:

                    if x2_input > 0:
                        for i in range(x2_input):
                            if x2_input != 0:
                                score = str(x2_input % 2) + score
                                x2_input = x2_input // 2

                        # while x2_input > 0:
                        #         score = str(x2_input % 2) + score
                        #         x2_input = x2_input // 2

                        number_of_chars = "-"*len(score)
                        print(" /----"+ number_of_chars+"--\ ")
                        print(" |", score, "|", 2,  "|")
                        print(" \--"+number_of_chars+"----/ ")
                    else:
                        print("The ", x2_input, "is lower than 0")
                # Konwertowanie z systemu binarnego na dziesiętny
                elif x3_input == 2:
                    # Sprawdzenie czy użytkownik wprowadził cyfry inne niż 0 & 1 dla systemu binarnego
                    for index in test:
                        if index != "0" and index != "1":
                            var2 = 0
                    if var2 == 0:
                        print("Wrong number - type again")

                    if var2 == 1:
                        for bit in range(len(temp)):
                            bit = int(temp[-1])
                            number = number + bit * 2 ** power
                            power += 1
                            temp = temp[:-1]
                        # while len(temp) > 0:
                        #     bit = int(temp[-1])
                        #     number = number + bit * 2 ** power
                        #     power += 1
                        #     temp = temp[:-1]
                        number = str(number)
                        number_of_chars = "-"*len(number)
                        print(" /---" + number_of_chars + "----\ ")
                        print(" |", number, "|", 10, "|")
                        print(" \---" + number_of_chars + "----/ ")
    # A kiedy wprowadzisz wszystko inne, oprócz tego o co prosi program:
    except ValueError:
        print("Wrong sign. Use a numbers only next time.")
    except IndexError:
        print("Ooooops! Try again --> NUMBER + <SPACE> + NUMERAL SYSTEM (2 or 10)")

