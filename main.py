"""Case-study #7 Generation of sentences
Developers:
Batenev P.A., Grigorev A.E., Dolgih N.A.
"""


def file_read(txt_file):
    """ Read text from the file and return list. """
    with open(txt_file) as f_in:
        return f_in.read().split()


def text_preparation(text):
    """ Removes extra characters and spaces. """
    signs = [')', '(', '^', '%', '#', '$', ';', ':', '"', '=', '+', '-', '_', '–']
    for i in range(len(text)):
        if text[i][-1] in signs:
            text[i] = text[i][:-1]
        else:
            text[i] = text[i]
    for i in signs:
        a = ' i'
        if a in text:
            text.replace(a, i)
    return text


def str_to_list():
    """ Делит текст на слова и загоняет их в список. """
    # TODO


def list_to_dict():
    """ Преобразует список из str_to_list в словарь звеньев и связей. """
    # TODO


def start_words():
    """ Вытаскивает из списка str_to_list стартовые слова и загоняет их в отдельный список. """
    # TODO


def text_generator():
    """ Generates crazy text. """
    # TODO


def main():
    """ Main function. """
    txt_file = input()
    text = text_preparation(file_read(txt_file))
    print(text)


if __name__ == '__main__':
    main()

