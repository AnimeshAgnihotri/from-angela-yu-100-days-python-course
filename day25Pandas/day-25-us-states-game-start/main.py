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
state_list=[]
state=50
count=0
while state:
    get_state_from_user=screen.textinput(title=f"Get State from user: {count}/50",prompt=f"Enter a state, current count ")
    if get_state_from_user is not None :
        get_state_from_user = get_state_from_user.lower()


    elif not get_state_from_user:
        missed_state=set(df["state"].values)-set(state_list)
        missed_state=pd.DataFrame(missed_state,columns=["missed state"])
        print(missed_state)
        print(f"the state/s you guessed: {state_list}")
        break
    get_state_from_user=get_state_from_user.lower()

    #print(get_state_from_user)
    if get_state_from_user in df["state"].values :
        if get_state_from_user not in state_list:
            count+=1
        state_data=df[df["state"] == get_state_from_user]
        state_data_x=state_data["x"].iloc[0]
        state_data_y=state_data["y"].iloc[0]
        my_state_turtle=Turtle()
        my_state_turtle.penup()
        my_state_turtle.goto(state_data_x, state_data_y)
        #my_state_turtle.shape("circle")
        print(get_state_from_user)
        my_state_turtle.write(get_state_from_user, font=("Arial", 10, "bold"))
        state_list.append(get_state_from_user)

    state=state-1



# for practise;
# val=df[df["state"]=="new york"]
# x_val=val["x"].iloc[0]
# y_val=val["y"].iloc[0]
# print(y_val)
# #print(val)
# print(x_val)
# print(val)


screen.mainloop()
#screen.exitonclick()
