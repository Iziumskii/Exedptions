documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def show_document_owner(docs):
    document_number = input('Введите номер документа: ')
    got_result = False
    for document in docs:
        if document_number == document['number']:
            print(document['name'])
            got_result = True
    if got_result == False:
        print('Данные отсутствуют')


def show_shelf_number(shelfs):
    document_number = input('Введите номер документа: ')
    got_result = False
    for shelf in shelfs:
        if document_number in shelfs.get(shelf):
            print('Документ находится на полке №', shelf)
            got_result = True
    if got_result == False:
        print('Данные отсутствуют')


def show_all_documents(docs):
    for document in docs:
        print(document['type'], document['number'], document['name'])


def add_new_document(docs, shelfs):
    new_type = input('Введите тип документа: ')
    new_number = input('Введите номер документа: ')
    new_name = input('Введите имя владельца: ')
    shelf_number = input('Введите номер полки: ')
    if shelf_number in shelfs:
        docs.append({"type": new_type, "number": new_number, "name": new_name})
        shelfs[shelf_number].append(new_number)
    else:
        print('Целевая полка отсутствует, хотите создать новую?')
        answer = input('y/n: ')
        if answer == 'y':
            docs.append({"type": new_type, "number": new_number, "name": new_name})
            shelfs[add_new_shelf(directories)].append(new_number)
    # print(docs,'\n', shelfs)


def delete_document(docs, shelfs):
    document_number = input('Введите номер документа: ')
    got_result = False
    i = -1
    for document in docs:
        i += 1
        if document_number == document['number']:
            docs.pop(i)
            got_result = True
    for shelf in shelfs:
        if document_number in shelfs.get(shelf):
            shelfs[shelf].remove(document_number)
            # print(docs,'\n', shelfs)
    if got_result == False:
        print('Данные отсутствуют')


def add_new_shelf(shelfs):
    new_shelf_number = input('Введите номер полки: ')
    check_shelf = False
    for shelf in shelfs:
        if new_shelf_number == shelf:
            check_shelf = True
            break
    if check_shelf == False:
        shelfs.update({new_shelf_number: []})
    else:
        print("Такая полка уже существует")
    # print(shelfs)
    return new_shelf_number


def moves_document_on_shelf(shelfs):
    document_number = input('Введите номер документа: ')
    target_shelf_number = input('Введите номер полки: ')
    got_document = False
    for shelf in shelfs:
        if document_number in shelfs.get(shelf):
            got_document = True
            if target_shelf_number in shelfs:
                shelfs[shelf].remove(document_number)
                shelfs[target_shelf_number].append(document_number)
                break
            else:
                print('Целевая полка отсутствует, хотите создать новую?')
                answer = input('y/n: ')
                if answer == 'y':
                    shelfs[add_new_shelf(directories)].append(document_number)
                    shelfs[shelf].remove(document_number)
                break
    if got_document == False:
        print('Документ не найден')
    # print(shelfs)


def show_names_owners(docs):
    for document in docs:
        try:
            print(document['name'])
        except KeyError as e:
            print(e, 'Имя отсутствует')


def user_command_input():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            show_document_owner(documents)
        elif command == 's':
            show_shelf_number(directories)
        elif command == 'l':
            show_all_documents(documents)
        elif command == 'a':
            add_new_document(documents, directories)
        elif command == 'd':
            delete_document(documents, directories)
        elif command == 'm':
            moves_document_on_shelf(directories)
        elif command == 'so':
            show_names_owners(documents)
        elif command == 'as':
            add_new_shelf(directories)
        elif command == 'q':
            print('До свидания!')
        else:
            print('Команда не найдена!')


def program_for_working_with_documents():
    """
  p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
  s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
  l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
  a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
  d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
  m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
  as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
  so - show owners - команда, которая выводит имена всех владельцев документов.

  q - выйти из программы.

  """
    help(program_for_working_with_documents)
    user_command_input()


program_for_working_with_documents()
