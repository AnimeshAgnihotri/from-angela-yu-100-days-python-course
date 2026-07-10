from turtle import Turtle, Screen
import pandas as pd
import time

screen = Screen()
screen.setup(width=450, height=450)
screen.title("India Map Game")
screen.addshape("indiamap.gif")
my_turtle = Turtle()
my_turtle.shape("indiamap.gif")
#dict_state={"states": [], "xcor": [], "ycor": []}
# def get_state_coordinate(x,y):
#     user_state=input("enter your state name")
#     dict_state["states"].append(user_state)
#     dict_state["xcor"].append(x)
#     dict_state["ycor"].append(y)
#
#     print(dict_state)

game=True
states_csv=pd.read_csv("indian_states_and_coordinates.csv")
states_csv["states"]=states_csv["states"].str.title()
count=0
guess_list=[]
while game:
    time.sleep(0.7)
    get_input=screen.textinput(title=f"current score {count}/35",prompt="choose a state ")
    if get_input is not None:
        get_input=get_input.title()
    if get_input in states_csv["states"].values:
        get_input=get_input.title()
        if get_input in guess_list:
            continue
        else :
            guess_list.append(get_input)
            count+=1
            my_turtle_2=Turtle()
            my_turtle_2.hideturtle()
            my_turtle_2.penup()
            my_turtle_2.shape("arrow")
            my_turtle_2.speed("slowest")
            single_state_detail=states_csv[states_csv["states"] == get_input]
            xcor=single_state_detail["xcor"].iloc[0]
            ycor=single_state_detail["ycor"].iloc[0]
            my_turtle_2.goto(xcor,ycor)
            my_turtle_2.write(get_input,font=("Arial",10,"normal"))
            #guess_list.append(get_input)



    elif get_input is None:
        game=False
        missed_state=set(states_csv["states"].values)-set(guess_list)
        print(pd.DataFrame(missed_state, columns=["missed states"]))
        print(f"current score {count}/35   {pd.DataFrame(guess_list, columns=["guessed states"])}")



screen.listen()
#screen.onscreenclick(get_state_coordinate)

screen.mainloop()
#screen.exitonclick()