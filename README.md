# NXOpen Python tutorials
a collection of NXOpen Python tutorials


## Tutorials:

### First steps:

In order to start with NX Python programing you need to prepare your NX settings. First step is to find the `Developer` tab at the top NX ribbon:



<pre>
  <center>
    <img src=".\\Pictures\\pic1_NX_developer_tab.png" width="500">
    <figcaption>Fig.1 - Find or activate the Developer tab.</figcaption>
  </center>                  
</pre>

if the tab does not exists already, right click on the top ribbon and find the `Developer` tab and activate it.

One great way to develop or learn NX Python programing is to record macros while using the GUI. By default NX saves macros in Visual Basic. To change that to Python, you need to go to `File > Preferences > User Interface`:

<pre>
  <center>
    <img src=".\\Pictures\\pic2_NX_userinterface.png" width="500">
    <figcaption>Fig.2 - Go to the User Interface Preference panel.</figcaption>
  </center>                  
</pre>

or press "<kbd>Ctrl</kbd> + 2" keyboard shortcut. Then in the `User Interface Preferences` change the `Journal Language` to Python:



<pre>
  <center>
    <img src=".\\Pictures\\pic3_NX_change_language_python.png" width="500">
    <figcaption>Fig.3 - Change the Journal Language to Python.</figcaption>
  </center>                  
</pre>


### Hello world!

Let's start with a very simple "Hello World!" example where a Message windows will show a text message (i.e., `string`).

```Python
#ex0001.py
import NXOpen.UF

def main(): 
    NXOpen.UF.UFSession.GetUFSession().Ui.DisplayMessage("Hello World!", 1)

if __name__ == '__main__':
    main()
```

to run the code you need to go to the `Developer` tab and find the `Play` button:

<pre>
  <center>
    <img src=".\\Pictures\\pic5_NX_run_code.png" width="500">
    <figcaption>Fig.4 - Find the Play button.</figcaption>
  </center>                  
</pre>

In the `Journal Manager` panel you can `Browse` to find and run the code:



<pre>
  <center>
    <img src=".\\Pictures\\pic6_NX_Journal_Manager.png" width="500">
    <figcaption>Fig.5 - Find the Play button.</figcaption>
  </center>                  
</pre>

The result will be as the picture below:

<pre>
  <center>
    <img src=".\\Pictures\\pic4_NX_message_box.png" width="500">
    <figcaption>Fig.6 - Message box window.</figcaption>
  </center>                  
</pre>



The message box window is good for alerting the using of specific issues, however the texts are not searchable or selectable. Alternatively, we could use:


```Python
#ex0002.py
import NXOpen

def main(): 
    listing_window = NXOpen.Session.GetSession().ListingWindow
    
    listing_window.Open()
    listing_window.WriteFullline("Hello world!")
    listing_window.Close()

if __name__ == '__main__':
    main()
```

and the result must be

pic6_NX_information_window

<pre>
  <center>
    <img src=".\\Pictures\\pic6_NX_information_window.png" width="500">
    <figcaption>Fig.6 - Information box window.</figcaption>
  </center>                  
</pre>