import os, time

SEPARATOR = 50 * "—"

def clear_screen():
    print("\033[H\033[J")


def win_rate():
    print(SEPARATOR)
    
    try:
        total_matches = float(input("[•] Your Current Match Total (Example 90): "))
        current_win_rate = float(input("[•] Your Current Total Win Rate (Example 67.5): "))
        target_win_rate = float(input("[•] The Total Win Rate You Want (Example 80): "))

        current_wins = total_matches * (current_win_rate / 100)
        required_wins = (target_win_rate * total_matches - current_wins * 100) / (100 - target_win_rate)

        print(f"{SEPARATOR}\n[•] You Need {round(required_wins)} Match Without Lose\n[•] To Get {target_win_rate}% Win Rate.")
        input(f"{SEPARATOR}\n[✓] Press Enter to return to the menu ")
        
    except ValueError:
        print(f"{SEPARATOR}\n[✗] Invalid Input! Please Enter A Valid Number.")
    except Exception as e:
        print(f"{SEPARATOR}\n[✗] An Error Occurred: {e}")


def main():
    while True:
        time.sleep(1.5)
        clear_screen()
        
        print(SEPARATOR)
        print("\t~WIN RATE CALCULATOR BY EL KHAIRU😍~")
        print(SEPARATOR)
        print("[•] Github : https://github.com/ellkhairu")
        print("[•] Date   :", time.strftime("%d/%m/%Y"))
        print("[•] Time   :", time.strftime("%H:%M %Z"))
        print(SEPARATOR)
        
        print("[1] Calculate Win Rate")
        print("[0] Exit")
        
        selected_program = input("[•] Select Program: ")
        if selected_program == "1":
            win_rate()
        elif selected_program == "0":
            clear_screen()
            break
        else:
            print("[✗] Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()