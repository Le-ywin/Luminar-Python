

weather = input("Sir, is it raining now? ")

weather = weather.lower()

if weather == "yes":

    second = input("Sir, is it windy now? ")

    if second == "yes" or weather == "Yes" or weather == "YES":

        print("It is too windy for an umbrella.")

    else:

        print("Take an umbrella.")

else:

    print("Enjoy your day")