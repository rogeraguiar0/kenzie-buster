Kenzie Buster

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

## Rodando os testes de cada tarefa isoladamente

Ao fim de cada tarefa será possível executar uma suite de testes direcionada àquela tarefa específica. Lembre-se de sempre estar com o **virtual enviroment (venv) ativado**.

- Rodando testes da Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Rodando testes da Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Rodando testes da Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Rodando testes da Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
