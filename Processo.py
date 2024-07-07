#from tkinter import *

class Processo:
    def __init__(self, pid, tempo_chegada: int, tempo_execucao: int, deadline: int) -> None:
        self.__pid__ = pid
        self.chegada = tempo_chegada
        self.exec = tempo_execucao
        self.deadline = deadline
    
    def get_pid(self) -> int:
        return self.__pid__
    
    def get_chegada(self) -> int:
        return self.chegada
    
    def get_exec(self) -> int:
        return self.exec
    
    def set_tempo_execucao(self, tempo_execucao: int) -> None:
        self.exec = tempo_execucao
        return None
    
    def get_deadline(self):
        return self.deadline
    
    
    def set_deadline(self, deadline: int) -> None:
        self.deadline = deadline
        return None
    