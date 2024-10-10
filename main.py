#Testing file for confirming codespaces are functional
import picture

def drawimage():
    canvas = picture.new_picture(400, 300)  #Create a blank, 400x300 picture
    picture.set_pen_width(8)

    # Draw O
    picture.set_outline_color("black")
    picture.set_fill_color("#A6192E")
    picture.draw_filled_rectangle(40,20,150,200)

    picture.set_fill_color("white")
    picture.draw_filled_oval(115,120,40,60)

    # Draw C
    picture.set_fill_color("#FFC72C")
    picture.draw_filled_chord(315,120,100,70,290)

    picture.set_outline_color("white")
    picture.set_fill_color("white")
    picture.draw_filled_circle(315,120,60)

    picture.set_outline_color("black")
    picture.draw_arc(315,120,60,55,305)

    # Draw line
    picture.set_outline_color("aquamarine")
    picture.set_position(40,260)
    picture.set_direction(-45)

    # Text
    picture.set_outline_color((0,0,0))
    picture.draw_text(120,275,"Save/Display", 24)

    return canvas

def drawimage2():
    canvas = picture.new_picture(400, 300)  #Create a blank, 400x300 picture
    picture.set_pen_width(8)

    # Draw O
    picture.set_outline_color("black")
    picture.set_fill_color("#A6192E")
    picture.draw_filled_rectangle(40,20,150,200)

    picture.set_fill_color("white")
    picture.draw_filled_oval(115,120,40,60)

    # Draw C
    picture.set_fill_color("#FFC72C")
    picture.draw_filled_chord(315,120,100,70,290)

    picture.set_outline_color("white")
    picture.set_fill_color("white")
    picture.draw_filled_circle(315,120,60)

    picture.set_outline_color("black")
    picture.draw_arc(315,120,60,55,305)

    # Draw line
    picture.set_outline_color("aquamarine")
    picture.set_position(40,260)
    picture.set_direction(-45)

    # Text
    picture.set_outline_color((0,0,0))
    picture.draw_text(120,275,"Run test", 24)

    return canvas


def main():
    flag = True

    while flag:
        flag = False
        print("Testing for CIT to confirm codespaces are working correctly.")
        print("Select the option you want to run")
        print("1. Run all tests")
        print("2. Run 'save' test")
        print("3. Run 'display' test")
        print("4. Run 'run' test")
        print("Note you cannot run 'display' after you have run 'run', you will need to restart the program")
        selection = input("Selection: ")
        if selection == "1":
            #testing save
            image = drawimage()
            print()
            print("testing save")
            picture.delay(500)
            picture.save_picture("Image.png")

            #testing display
            image = drawimage()
            print()
            print("testing display")
            picture.delay(500)
            picture.display()
            close = input("Hit enter to close")

            #testing run
            image = drawimage2()
            print()
            print("testing run")
            picture.delay(500)
            print("Close the tab in the graphics window to end.")
            picture.run()
            
        elif selection == "2":
            image = drawimage()
            print("testing save")
            picture.save_picture("Image.png")
        elif selection == "3":
            image = drawimage()
            print("testing display")
            picture.delay(500)
            picture.display()
            close = input("Hit enter to close")
        elif selection == "4":
            image = drawimage2()
            print("testing run")
            picture.delay(500)
            print("Close the tab in the graphics window to end.")
            picture.run()
            
        else:
            print("Not an option, please try again")
            flag = True

main()