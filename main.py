from user import whoopUser

email = ""
password = ""
user = whoopUser(email, password)

#get all cycle data
# cycles_data = user.get_cycles_df()

#get all workouts
# workout_data = user.get_workouts_df()

# get sports
# sports_data = user.get_sports()

#get heart rate data for one day
# start_end ={
#         'start': '2020-12-10T00:00:00.000Z',
#         'end': '2020-12-11T00:00:00.000Z'
#     }
# hr_data = user.get_heart_rate_df(params=start_end)

#get all sleep data
sleep_data = user.get_sleeps_df()

if __name__ == "__main__":
    sleep_data.to_csv('sleeps.csv')
    # for sport in sports_data:
    #     print(f"{sport['id']}, {sport['name']}")
    # print(str(workout_data))