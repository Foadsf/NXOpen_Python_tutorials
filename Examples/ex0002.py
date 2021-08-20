# ex0002.py
import NXOpen

def main(): 
    listing_window = NXOpen.Session.GetSession().ListingWindow
    
    listing_window.Open()
    listing_window.WriteFullline("Hello world!")
    listing_window.Close()

if __name__ == '__main__':
    main()