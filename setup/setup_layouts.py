
def initialize():
    global background_image
    global container
    global screen

    background_image = PhotoImage(file=os.path.join(assets_folder, 'setup-background.gif'))
    container = Label(screen, image=background_image)
    container.config(image=background_image)
    container.img = background_image  # avoid garbage collection

    

# screen.protocol("WM_DELETE_WINDOW", on_closing) # bind a function to close button
# screen.mainloop()


