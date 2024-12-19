from application import Application


if __name__ == "__main__":
    app = Application()

    while app.running:
        app.update()
        app.render()

    app.exit()
