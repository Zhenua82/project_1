'''Урок No16. Классы и объекты
Задание No1 Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
●top_up(X) -пополнить на X
●count_1000() -выводит сколько целых тысяч осталось в кассе
●take_away(X) -забрать X из кассы, либо выкинуть ошибку, что не достаточно денег'''
'''class Касса:

    def __init__(self, money):
        self.money = money
    
    def top_up(self, X):
        self.money += X
        return self.money
    
    def count_1000(self):
        self.count = self.money // 1000
        return f'В кассе осталось целых тысяч: {self.count}'

    def take_away(self, X):
        if self.money > X:
            self.money -= X
            return self.money
        else: return ('Операция проведена быть не может - в кассе недостаточно денег')

деньги_в_кассе = Касса(1200)
print(деньги_в_кассе.top_up(100))
print(деньги_в_кассе.count_1000())
print(деньги_в_кассе.take_away(140))       
print(деньги_в_кассе.take_away(10000))'''

'''Задание No2
Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s -количество клеточек, на которое она перемещается за ход у
этого класс есть методы:
●go_up() -увеличивает y на s
●go_down() -уменьшает y на s
●go_left() -уменьшает x на s
●go_right() -увеличивает y на s
●evolve() -увеличивает s на 1
●degrade() -уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
●count_moves(x2, y2) -возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции'''

class Черепашка:
    def __init__(self, x, y, s):
        self.horizontal = x
        self.vertical = y
        self.way = s
    
    def go_up(self):
        self.vertical += self.way
        return self.vertical
    
    def go_down(self):
        self.vertical -= self.way
        return self.vertical
    
    def go_left(self):
        self.horizontal -= self.way
        return self.horizontal
    
    def go_right(self):
        self.horizontal += self.way
        return self.horizontal
    
    def evolve(self):
        self.way += 1
        return self.way
    
    def degrade(self):
        if self.way >= 2:
            self.way -= 1
            return self.way
        else: return 'Действие невозможно, достигнут минимальный предел скорости перемещения черепахи'

    def count_moves(self, x2, y2):
        x = abs(self.horizontal - x2)
        y = abs(self.vertical - y2)
        count = 0
        list_count = []
        if max([x, y]) == 0:
            list_count.append(count)
        for i in range(1, max([x, y]) + 1):
            count = abs(i - self.way)
            ss = 0
            sss = 0
            if min([x, y]) == 0:
                while ss < max([x, y]):
                    ss += i
                    count += 1 
                if ss == max([x, y]):
                    list_count.append(count)
                else:
                    count += (ss - max([x, y])) + 1
                    list_count.append(count)
            else:
                while ss < min([x, y]):
                    ss += i
                    count += 1 
                if ss == min([x, y]):
                    count += 0
                else:
                    count += (ss - min([x, y]))
                while sss < max([x, y]):
                    sss += i
                    count += 1 
                if sss == max([x, y]):
                    list_count.append(count)
                else:
                    count += (sss - max([x, y]))
                    list_count.append(count)    
        return min(list_count)
        
череп = Черепашка(0, 0, 7)
print(череп.count_moves(2, 21))
print(f'Координаты черепа: {череп.horizontal}, {череп.vertical}')
 
'''def count_moves(self, x2, y2):
        self.horizontal = x2
        self.vertical = y2
        return f'0 (она уже там)' '''

''' def count_moves(self, x2, y2):
        x = abs(self.horizontal - x2)
        y = abs(self.vertical - y2)
        count = 0
        ss = 0
        z = min([x, y]) // 2
        if self.way > max([x, y]):
            while self.way > max([x, y]):
                self.way -= 1
                count += 1
            count += 1
            while self.way > min([x, y]):
                self.way -= 1
                count += 1
            count += 1
        if self.way <= z:
            while self.way != z:
                self.way += 1
                count += 1
            if 2 * self.way == min([x, y]):
                count += 2
            else: count += (self.way - (min([x, y]) - 2 * self.way +1))
            while ss < max([x, y]):
                ss += self.way
                count += 1
            if ss == max([x, y]):
                count += 0
            else: count += (self.way - (max([x, y]) - ss + 1))
        if self.way > z and self.way <= min([x, y]): 
                            while self.way != min([x, y]):
                                self.way += 1
                                count += 1
                            count += 1
                            while ss < max([x, y]):
                                ss += self.way
                                count += 1 
                            if ss == max([x, y]):
                                count += 0
                            else: count += (self.way - (ss - max([x, y]) + 1))
        if self.way > min([x, y]) and self.way <= max([x, y]):
                            if min([x, y]) == 0:
                                    while ss < max([x, y]):
                                        ss += self.way
                                        count += 1 
                                    if ss == max([x, y]):
                                        count += 0
                                    else: count += (self.way - (ss - max([x, y]) + 1))
                            else:
                                while self.way != min([x, y]):
                                    self.way -= 1
                                    count += 1
                                count += 1
                                while ss < max([x, y]):
                                    ss += self.way
                                    count += 1 
                                if ss == max([x, y]):
                                    count += 0
                                else: count += (self.way - (ss - max([x, y]) + 1))
        return count      
череп = Черепашка(0, 0, 2)
print(череп.count_moves(8, 10))
print(f'Координаты черепа: {череп.horizontal}, {череп.vertical}')  '''

''' def count_moves(self, x2, y2):
        self.horizontal = x2
        self.vertical = y2
        return f'0 (она уже там)'
 
        
череп = Черепашка(0, 0, 2)
print(череп.go_up())
print(череп.degrade())
print(череп.degrade())
print(череп.count_moves(8, 10))
print(f'Координаты черепа: {череп.horizontal}, {череп.vertical}')'''


'''def count_moves(self, x2: int, y2: int) -> int:
        r = self._solver(self, x2, y2)
        return 0
 
    def _solver(self, t: 'Turtle', x2: int, y2: int):
        actions = ('go_up', 'go_down', 'go_left', 'go_right', 'evolve', 'degrade')
        for i in actions:
            t2 = dataclasses.replace(t)  # copy
            getattr(t2, i)()
            if t2.x == x2 and t2.y == y2:
                return 0
            r = self._solver(t2, x2, y2)
 
        pass'''
    