class dog:
    """ This Class is a blueprint for digital dogs """
    def __init__(self,name,Color=['gray','white','black'],state='standing'):
        self._name=name;
        self._Color=Color;
        self._state=state;
        
    def sit(self):
        if self._state='sitting':
            print '%s is already sitting'%self._name;
        else:
            print '%s sits'%slef._name;
            self._state='sitting'

###  Main program that uses the class dog
if __name__ == '__main__':
    D=dog('stan',state='lying down');
    D.sit()

