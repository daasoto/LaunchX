def main():
    open("/path/to/mars.jpg")
    try:
        configuracion = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()