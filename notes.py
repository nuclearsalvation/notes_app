import csv
import datetime

def make_note(note_head, note_main, id):
    note = list()
    note.append(id)
    note.append(note_head)
    note.append(note_main)
    date_note = datetime.datetime.now()
    note.append(date_note.strftime('%Y-%m-%d %H:%M'))
    return note

def read_note(file_path, id):
        with open(file_path, 'r',encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile,delimiter=';')
            for row in spamreader:
                if (row[0] == str(id) or (row[1] == id)):
                     print(row)

def read_notes(file_path, date1, date2):
     with open(file_path, 'r',encoding="utf-8") as csvfile:
          spamreader = csv.reader(csvfile, delimiter=';')
          for row in spamreader:
               if (datetime.datetime.strptime(row[-1], '%Y-%m-%d %H:%M') > datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M')) and (datetime.datetime.strptime(row[-1], '%Y-%m-%d %H:%M') < datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M')):
                    print(row)

def append_note(file_path, note):
     with open(file_path, 'a', newline='',encoding="utf-8") as csvfile:
          spamwriter = csv.writer(csvfile,delimiter=';')
          spamwriter.writerow(note)

def remove_note(file_path, string):
     csvfile = open(file_path, 'r',encoding="utf-8")
     spamreader = csv.reader(csvfile,delimiter=';')
     spamreader_list = list()
     for row in spamreader:
          spamreader_list.append(row)

     csvfile.close()
     csvfile = open(file_path,'w',newline='',encoding="utf-8")
     spamwriter = csv.writer(csvfile, delimiter=';')
     for row in spamreader_list:
          if ((row[0] != string and row[0] != str(string)) and row[1] != string):
               spamwriter.writerow(row)
     csvfile.close()

def main():
     file_path = 'output.csv'
     flag = True
     while (flag == True):
          print('Список команд')
          print('0 - выйти')
          print('1 - показать заметки в пределах дат')
          print('2 - показать одну заметку')
          print('3 - удалить заметку')
          print('4 - написать заметку')
          print('5 - отредактировать заметку')
          answer = input('выберите действие ')
          if (answer == '0'):
               flag = False
          elif (answer == '1'):
               date_one = input('дата 1 ')
               date_two = input('дата 2 ')
               read_notes(file_path, date_one, date_two)
          elif (answer == '2'):
               search = input('id или заголовок ')
               read_note(file_path, search)
          elif (answer == '3'):
               search = input('id или заголовок ')
               remove_note(file_path, search)
          elif (answer == '4'):
               head = input('заголовок ')
               id = input('id ')
               msg = input('тело заметки ')
               append_note(file_path, make_note(head, msg, id))
          elif (answer == '5'):
               id = input('id ')
               remove_note(file_path, id)
               head = input('заголовок ')
               msg = input('тело заметки ')
               append_note(file_path, make_note(head, msg, id))
          else:
               pass


main()