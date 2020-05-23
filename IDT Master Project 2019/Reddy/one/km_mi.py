def miles():
    kilometers = float(input("Enter value in kilometers"))
    # This is our conversion factor
    conv_fac = 0.621371
    # calculation of miles
    miles = kilometers * conv_fac
    print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))
