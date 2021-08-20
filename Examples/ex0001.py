# ex0001.py
import NXOpen.UF

def main(): 
    NXOpen.UF.UFSession.GetUFSession().Ui.DisplayMessage("Hello World!", 1)

if __name__ == '__main__':
    main()