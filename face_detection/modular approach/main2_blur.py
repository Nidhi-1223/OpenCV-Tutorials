import detector_blur
import tkinter
import PIL
from PIL import ImageTk


#Declaring the main application window
app = tkinter.Tk()
app.title("**Face Detection")

#Header text
textLabel = tkinter.Label(app, text="Face blur")
textLabel.pack()

#The image level that refreshes over and over
imageLabel = tkinter.Label(app)
imageLabel.pack()


#the logic to refresh the label
def showFrame():
    #getting image array from detector
    img = detector_blur.detect()     #detector file mein detect function
    #converting image array to Pillow image object
    frame = PIL.Image.fromarray(img)
    #creating tkinter image object and changing label's image
    imgtkinter = ImageTk.PhotoImage(frame)
    imageLabel.imgtk = imgtkinter
    imageLabel.configure(image=imgtkinter)
    imageLabel.after(150, showFrame)

showFrame()
app.mainloop()