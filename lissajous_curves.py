import numpy as np
import matplotlib.pyplot as plt

def lissajous_para_eq(A=1,B=1,a=1,b=1):
    """
    Argument: lissajous(Amplitude of x, Amplitude of y, Frequency of x, Frequency of y).
                The parameters are set to a default value of 1
                The proper parameter argument can be provided when the function is called
    Return: Returns the parametric values (X and Y) of the Lissajous parametric equation over
                the domain interval of [-pi , pi]
                inside a list 
    """
    # defining the time interval (the domain interval of the parametric equations)
    t = np.linspace(-np.pi,np.pi,500)

    x = A * np.sin((a*t)+(np.pi/2))
    y = B * np.sin(b*t)

    return [x,y]

if __name__ == '__main__': # test and usage example
    prompts = ['insert the amplitude of the X parametric equation (A): ',
               'insert the frequency of the X parametric equation (a): ',
               'insert the amplitude of the y parametric equation (B): ',
               'insert the frequency of the y parametric equation (b): ']
    parameters = []
    for i in prompts:
        while(True):
            user_input = input(i)
            try:
                parameter = float(user_input)
                parameters.append(parameter)
                break
            except:
                print("input parameter was incorrect",
                      "\nMake sure to enter a number")
    para_values = lissajous_para_eq(parameters[0],parameters[2],parameters[1],parameters[3])
    x = para_values[0]
    y = para_values[1]
    plt.plot(x,y)
    plt.title("Lissajous Curve")
    plt.grid()
    plt.show()