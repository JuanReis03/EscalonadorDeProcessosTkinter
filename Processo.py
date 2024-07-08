from tkinter import *

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
    
    def get_tempo_execucao(self) -> int:
        return self.exec
    
    def set_tempo_execucao(self, tempo_execucao: int) -> None:
        self.exec = tempo_execucao
        return None
    
    def get_deadline(self):
        return self.deadline
    
    
    def set_deadline(self, deadline: int) -> None:
        self.deadline = deadline
        return None



if __name__ == "__main__" :
    
    class App(Tk):
        def __init__(self) -> None:
            super().__init__()
            self.geometry('700x450')
            self.title('Simulador SO')
            self.pid_counter = 0

            self.input_widget()
            self.new_process_button = Button(self, text='Criar Processo', command=self.create_process)
            self.new_process_button.grid(row=2, column=0, columnspan=5)
            


        def create_process(self)-> None:
            chegada = int(self.chegada_input.get())
            tempo_execucao = int(self.tempo_execucao_input.get())
            deadline = int(self.deadline_input.get())
            self.new_process = Processo(self.pid_counter, chegada, tempo_execucao, deadline)
            self.output_process(self.new_process)
            self.chegada_input.delete(0, END)
            self.tempo_execucao_input.delete(0, END)
            self.deadline_input.delete(0, END)
            self.pid_counter += 1
        
        def input_widget(self) -> None:
            self.chegada_label = Label(self, text='Tempo de Chegada')
            self.chegada_label.grid(row = 0, column= 0)
            self.chegada_input = Entry(self, width = 10)
            self.chegada_input.grid(row=1, column=0)

            self.tempo_execucao_label = Label(self, text='Tempo de Execução')
            self.tempo_execucao_label.grid(row=0, column=1)
            self.tempo_execucao_input = Entry(self, width = 10)
            self.tempo_execucao_input.grid(row=1, column=1)

            self.deadline_label = Label(self, text = 'Deadline')
            self.deadline_label.grid(row=0, column=2)
            self.deadline_input = Entry(self, width = 10)
            self.deadline_input.grid(row=1, column=2)
        

        def output_process(self, process: Processo) -> None:
            self.output = Label(self, text = f"PID:{process.get_pid()}  Tempo de Chegada:{process.get_chegada()}  Tempo de Execução:{process.get_tempo_execucao()}  Deadline:{process.get_deadline()}")
            self.output.grid(columnspan = 3)
            
    
    ''' p = Processo(0, 1, 2, 3) '''

    ''' print(f"PID:{p.get_pid()}\nTempo de Chegada:{p.get_chegada()}\nTempo de Execução:{p.get_tempo_execucao()}\nDeadline:{p.get_deadline()}") '''

    teste = App()
    teste.mainloop()