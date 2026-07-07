from turtle import Turtle, Screen
import pandas as pd
screen = Screen()
screen.title("US STATE GAME")
screen.addshape("blank_states_img.gif")
my_turtle = Turtle()
my_turtle.shape("blank_states_img.gif")
df_csv=pd.read_csv("50_states.csv")
df=pd.DataFrame(df_csv)

df["state"]=df["state"].str.lower()

state=50
while state:
    get_state_from_user=screen.textinput(title="Get State from user",prompt="Enter a state")
    if get_state_from_user is not None:
        get_state_from_user = get_state_from_user.lower()
    else:
        break
    get_state_from_user=get_state_from_user.lower()

    #print(get_state_from_user)
    if get_state_from_user in df["state"]:
        my_turtle.goto(df["x"][state], df["y"][state])
        print(get_state_from_user)
        my_turtle.write(get_state_from_user, font=("Arial", 20, "bold"))


    state=state-1

screen.mainloop()
#screen.exitonclick()
