


# Program gra "Quiz". Zadanie użykownika to odpowiedzieć na kilka pytań.

#dane - krotka

questions = (
    ("Ile dni ma rok 2025", "365"),
    ("Kto jest najważniejszy na statku?", "kapitan"),
    ("Co przychodzi po nocy?", "dzień"),
    ("Co przychodzi po burzy?", "słońce"),
)




#logia - funkcja

def play_game(question_number = 1):

    print("Witaj w grze! masz kilka pytań do skarbu")
    print("Aby zdobyć skarb (beczka rumu!) musisz odpowiedzieć na wybraną przez siebie liczbę pytania")



    succes = "brawo, odpowiedź prawidłowa!"
    failure = "No niestety i nici ze skarbu :("

    for i in range(question_number): 
        user_answer = input(questions[i][0] + " Twoja odpowiedź: ")
        if questions[i][1] == user_answer:
            print(succes)
        else:
            print(failure)
            return 

    

    print("brawo wygrałeś beczke rumu, Gratulacje!")

game_number = int(input("Na ile pytań chcesz odpowiedzieć? Od 1 do 4: "))
play_game(game_number)

