def rocket_launch(fuel, atronauts):
    if astronauts*100<fuel:
        print("Lunch Successful!")
        return "Launch Successful"
    else:
        print("insufficient fuel")
        return "insufficient fuel"
    
rocket_launch(500, 3)
