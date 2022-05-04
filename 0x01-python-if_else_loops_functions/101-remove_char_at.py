vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python

Command 'python' not found, did you mean:

  command 'python3' from deb python3
  command 'python' from deb python-is-python3

vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> string.ascii_letters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> string.ascii_letters_lowercase
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> string.ascii_letters_lowercase
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'string' is not defined
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'string' has no attribute 'ascii_letters_lowercase'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> 
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3 100-print_tebahpla.py 
  File "100-print_tebahpla.py", line 5
    print(f"{:c}", end="")
          ^
SyntaxError: f-string: empty expression not allowed
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3 100-print_tebahpla.py 
Traceback (most recent call last):
  File "100-print_tebahpla.py", line 5, in <module>
    print(f"{c}", end="")
NameError: name 'c' is not defined
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3 100-print_tebahpla.py 
Traceback (most recent call last):
  File "100-print_tebahpla.py", line 5, in <module>
    print(f"{c}")
NameError: name 'c' is not defined
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3 100-print_tebahpla.py 
  File "100-print_tebahpla.py", line 5
    print(f"{:c}")
          ^
SyntaxError: f-string: empty expression not allowed
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ python3 100-print_tebahpla.py 
zYxWvUtSrQpOnMlKjIhGfEdCbAvagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git add 100-print_tebahpla.py 
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git commit -m "Print alphabet"
[main 41b8241] Print alphabet
 1 file changed, 5 insertions(+)
 create mode 100644 0x01-python-if_else_loops_functions/100-print_tebahpla.py
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 451 bytes | 451.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.        
To https://github.com/jhonbueno/holbertonschool-higher_level_programming.git
   22e3d6a..41b8241  main -> main
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ chmod u+x 100-print_tebahpla.py 
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git add 100-print_tebahpla.py 
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git commit -m "Update"
[main 7a4b8b1] Update
 1 file changed, 0 insertions(+), 0 deletions(-)
 mode change 100644 => 100755 0x01-python-if_else_loops_functions/100-print_tebahpla.py
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 283 bytes | 283.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.        
To https://github.com/jhonbueno/holbertonschool-higher_level_programming.git
   41b8241..7a4b8b1  main -> main
vagrant@ubuntu-focal:~/holbertonschool-higher_level_programming/0x01-python-if_else_loops_functions$ 