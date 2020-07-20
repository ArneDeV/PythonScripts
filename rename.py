import os

def main():
    path = "C:\\Users\\Arne\\OneDrive\\Afbeeldingen\\Camera-album"
    gewenste_folder = input("Geef path waar foto's moeten komen? (Deel na camera-Album): ")
    # bestandsnaam = input("Hoe moeten de bestanden heten")

    new_path = os.path.join(path, gewenste_folder)
    print(new_path)

    if os.path.exists(new_path):
        # * Folder bestaat al in dit geval
        print("Folder bestaat al, geen nieuwe aangemaakt!")
    else:
        # * Folder bestaan nog niet
        print("Nieuwe folder aanmaken... ")
        print("Folder aangemaakt!")
        os.mkdir(os.path.join(path, gewenste_folder))

    i = 1

    for filename in os.listdir(path):
        path_file = os.path.join(path, filename)
        new_path_file = os.path.join(new_path, filename)
        if not os.path.isdir(path_file):
            print(f'Verplaatsen van {filename}')
            os.rename(path_file, new_path_file)
        i += 1
    print(f"\n\nAlle bestanden zijn verplaatst naar {new_path}")



if __name__ == "__main__":
    main()


# "C:\Users\Arne\OneDrive\Afbeeldingen\Camera-album\Thailand 2019"