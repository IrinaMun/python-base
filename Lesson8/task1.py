"""
1. �������� ������� email_parse(<email_address>), ������� ��� ������ ����������� ��������� ��������� ��� ������������ �
�������� ����� �� email ������ � ���������� �� � ���� �������. ���� ����� �� �������, ��������� ���������� ValueError.
������:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
����������: ��������� � ��������� ������� � ������ � ������������ ������ �� � ���������� ���������;
����� �� ����� � ������ ������ ������������ ������� re.compile()?
"""