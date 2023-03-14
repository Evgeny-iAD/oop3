import color_text
import list_tree
import worker as w
import departament as d
import incorporated as i

class SetPersona(w.Worker):
    def __init__(self, workUserName, workAge):
        super().__init__()
        self.workUserName = workUserName
        self.workAge = workAge

    def __str__(self):
        return f'{self.workPosition}: {self.workUserName}  {self.workAge} лет'

    def userPosition(self, user_pos):
        self.workPosition = user_pos

def addPersonToDepart(person, position, dep, olddep):
    listPosition = dep.posListUser
    if position in listPosition:
        person.workPosition = position
        olddep.removeUserWork(person)
        dep.addUserWork(person)
    else: print('Нет такой должности в отделе ')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    corp = i.Incorporated('ООО "Рога и копыта"')  #Организация
    noDepPer = d.Departament(color_text.out_blue('Безымянный'))   #Отдел
    Dep1 = d.Departament(color_text.out_blue('Отдел навигации')) #Отдел
    Dep2 = d.Departament(color_text.out_blue('Вычислительный отдел')) #Отдел
    Dep3 = d.Departament(color_text.out_blue('Мечтательный отдел')) #Отдел
    corp.addDepWork(noDepPer)
    corp.addDepWork(Dep1)
    corp.addDepWork(Dep2)
    corp.addDepWork(Dep3)
    noDepPer.addPosWork('Без должности')
    Dep1.addPosWork('Начальник отдела') #Должность
    Dep1.addPosWork('Зам начальника') #Должность
    Dep1.addPosWork('Оператор') #Должность
    Dep2.addPosWork('Начальник отдела')  # Должность
    Dep3.addPosWork('Начальник мечтательного отдела') #Должность
    Dep3.addPosWork('Философ') #Должность
    Dep3.addPosWork('Мыслитель') #Должность

    valera = SetPersona('Валера', 18)
    stepan = SetPersona('Степан', 28)
    trinety = SetPersona('Тринети', 23)
# /
    noDepPer.addUserWork(valera)
    noDepPer.addUserWork(stepan)
    noDepPer.addUserWork(trinety)

    corp.getIncoListDep()
    print(f'\n{color_text.out_yellow("Список сотрудников отдела:")} {noDepPer.depName}')
    noDepPer.getDeptListUser()
    print(f'\n{color_text.out_yellow("Список должностей отдела:")} {Dep1.depName}')
    Dep1.getDeptListPos()
    print(f'\n{color_text.out_yellow("Список должностей отдела:")} {Dep3.depName}')
    Dep3.getDeptListPos()
    print(f'\n')

    addPersonToDepart(valera, 'Начальник мечтательного отдела', Dep3, noDepPer)
    addPersonToDepart(stepan, 'Философ', Dep3, noDepPer)
    print(f'\n{color_text.out_yellow("Список сотрудников отдела:")} {Dep3.depName}')
    Dep3.getDeptListUser()

    print(f'\n{color_text.out_red("Проверка на удаления из старого отдела:")} {noDepPer.depName}')
    noDepPer.getDeptListUser()
    print(f'\n')

    list_tree.tree_v2(corp.corpName, corp.corpDept)