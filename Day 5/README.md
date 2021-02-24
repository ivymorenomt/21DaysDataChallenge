### Day 5: conditional logic and control flows
After purchasing all the supplies they needed to make repairs, Dot's house is starting to look incredible. The floors are patched, and the rooms are painted to perfection. Now all they need is to give the house a good thorough cleaning. The bad news is that the box with their cleaning supplies seems to have been misplaced in the move.

The store in the nearby town does sell cleaning supplies, but their prices can sometimes be a lot higher than Dot's used to. They've already spent so much money on repairs - can you help them figure out which supplies to abstain from buying at the town's store?

Tutorial:

In today's challenge, you'll use two essential programming concepts: conditional logic and control flows.

Conditional Logic:

Conditional logic refers to the execution of different actions based on whether a certain condition is met. In programming, these conditions are expressed by a set of symbols called Boolean Operators.

Boolean Comparator	Example	Meaning

>	x > y	x is greater than y

>=	x >= y	x is greater than or equal to y

><	x < y	x is less than y

><=	x <= y	x is less than or equal to y

>!=	x != y	x is not equal to y

>==	x == y	x is equal to y

Conditional logic is essential to control flow statements. In programming, control flows are expressed in if...else statments. To read more on if...else statements, read this article before proceeding.

#### If Statment
if condition is True:
    
    '''
    execute body of code
    '''

#### If Else Statments
if var > 10: #if var is greater than 10
    
    '''
    execute body of code
    '''
else: 
   
    if none of the above statement is true, execute code
    '''
    execute body of code
    '''

#### Mutliple If...else statements

if var > 10: 

    '''
    if var is greater than 10
    execute body of code
    '''

elif var > 5 and <= 10: 

    '''
    if var is greater than 5 but less than or equal to 10
    execute body of code
    '''
else: 

    '''
    if none of the above statement is true, execute code
    execute body of code
    '''
Note: If...else statements can be executed within a for loop. However, be aware of the indentation.

#### Output:

 Dustpan
 
 Garbage Bags
 
 Glass Cleaner
 
 Vinegar
 
 Floor Cleaner
 
 Paper Towels