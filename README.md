# finalCapstone

Title - Inventory
Content -
Description
Installation
Instruction
Credits
Description
Python program that will read from the text file inventory.txt and perform certian functions on the data. This will help managers organise and keep an eye on the stock levels.

Installation
This program does not require any installation. All you need is to copy paste the code to an IDE of your choice.

Intruction
▪ read_shoes_data (choice 1) - This function will open the file inventory.txt and read the data from this file, then create a shoes object with this data and append this object into the shoes list. One line in this file represents data to create one object of shoes. You must use the try-except in this function for error handling. Remember to skip the first line using your code.

▪ capture_shoes (choice 2) - This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.

▪ view_all (choice 3)- This function will iterate over the shoes list and print the details of the shoes returned from the str function. Optional: you can organise your data in a table format by using Python’s tabulate module.

▪ re_stock (choice 4)- This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.

▪ seach_shoe (choice 5)- This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.

▪ value_per_item (choice 6)- This function will calculate the total value for each item . Please keep the formula for value in mind; value = cost * quantity. Print this information on the console for all the shoes.

▪ highest_qty (choice 7)- Write code to determine the product with the highest quantity and print this shoe as being for sale. ▪ (choice 8) - Exit

Credits N/A
