import os


def list_images_files(directory):
    image_file = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".gif"):
                image_file.append(os.path.join(root, file))

        for dir in dirs:
            image_file.extend(list_images_files(os.path.join(root, dir)))

    return image_file


if __name__ == '__main__':
    with open('images.txt', 'w') as f:
        for index, name in enumerate(list_images_files('2 Química Experimental/RELATÓRIO 7/')):
            f.write(f'\n{index}) name: {name}\n')

        f.close()


