# Market-list-maker

Market list maker that utilizes your own recepies.


# How to use it

First of all, go in the Files directory and open the Recepies.csv file. Then, proceed to add your own recepies there following these clauses:
- `Each recepie must be displayed in a separeted line`<br>
- `The name of all recepies must be on the first column (column A)`<br>
- `Each ingedient must be displayed in a separated column followd by a colon and then the quantity`<br>

For instance:
A | B | C | D | E | F | G | H | I
--- | --- | --- | --- |--- |--- |--- |--- |---
Mac n cheese | butter:100 | flour:100 | milk:800 | parmesan cheese:100 | cheddar cheese:150 | pasta:350 | salt:1 | pepper:1

The quantities are in grams and mililiters.

Notice that you can put spaces in the name of the ingredients and in the name of the recepies, but you cannot put any spaces between the name the colon and the quantity. Also, the quantities of salt and pepper are 1, that's for a couple of reasons:

1- You maybe already have those ingredients at home

2- It is not a fixed amount, you just need to know that you will use those ingredients in the recepie. By putting 1 in the quantity you will know how much recepies will need those ingredients


If you want your list to show the measurement unit of each ingredient, you can do so following these steps:

1 - Open the Files directory

2- Open the Measures directory

3- Add the name of the ingredient in the corresponding .txt file.

  For instance, you will add 'pasta' in the solids.txt file, doing so, the code will add 'g' in the end of this quantity in your list, 'ml' if they are in liquids.txt and 'x' if they are in units.txt


# Running it

Once you've fished doing the configurations, run the code, it will ask what do you plan on cooking for this week. Then you must proceed to list the recepies and separete them just by a comma.

Whe you've finished listing what you want to cook, press enter and then the code you generate a file called 'List.csv' containing the name and thee quantities of each ingredient.
