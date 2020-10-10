## utility belt
This is a utility package for convenient and easy use.<br/>
It contains different utility functions.</br>
to install it use ``` pip install util-belt ``` and `pip` will install the latest version of the package<br/>
### List of functionalities
1. list to text  <br/> to save a list to txt for later use you can do it using the <br/>
```list_to_txt()``` funtion in the ```file_utils``` module.
   #### example
   ```
   from util_belt.file_utils import list_to_txt

   my_list = [3,5,6,7]
   list_to_txt(my_list , file_dest = './list.txt')

   ```
   file_dest parameter is the file path where the list should be saved at </br>
   by default it is  the current directory and the file name is list.txt <br>
   you can change that to any file path you want. funtion will save your list <br>
   to a file with to worry about details in file handling.
2. file from list</br>
   to get a list saved in a txt file use ``` list_from_txt ``` function in the ``` file_utils `` module <br/>

   #### Example
   ```
   from util_belt.file_utils import list_from_txt

   my_list = list_from_txt('Documents/my_list.txt')

   ```

