Session 6
=========

Preparation
-----------

Be ready to share your War game. 

Today's plan
------------

0. Share War games. Check in on anyone who had trouble.

1. Introduce beginning of Java:
   
   - Java is a **compiled language**, which means you need to compile (crunch)
     your program before you can run it. Many programmers use Eclipse, a 
     fancy version of TextWrangler, which can run the compile command for you. 
     But you can do it yourself very easily too: If you have a file called 
     `TeaKettle.java`, you can run `javac TeaKettle.java` to compile the file
     `TeaKettle.class`. Then you can run it with `java TeaKettle`.
   - Java is **statically typed**. This means that every time your program 
     interacts with a value (such as creating a variable, setting a variable, 
     passing values into functions, or returning values from functions), you
     must specify what kind of thing you are dealing with.
   - new syntax
     - Every line ends with a semicolon.
     - Blocks of code (such as class definitions, method definitions, loops,
       or conditionals) are designated by curly braces. (Python uses 
       indentation instead.)

2. Play around with Java TeaKettle.

3. Choose individual projects.

        
Homework
--------

0. How many battles are there, on average, in a game of war? Finish player.py 
   and war.py and use them to answer this question (the `calculate_war.py` 
   script performs the calculation). If you get stuck, email Chris for help 
   or check out the solutions in the solutions folder.

1. This session we introduced Java, a language which is designed to be 
   completely object-oriented. We discussed several differences between Java
   and Python, described above. Try using Java:
     1. Create a file called `TeaKettle.java`, and paste in the contents of 
        `code/java/TeaKettle.java`.
     2. Run `javac TeaKettle.java` to compile your code.
     3. Create another file called `Kitchen.java`. Paste in the contents of 
        `code/java/Kitchen.java`.
     4. Run `javac Kitchen.java` to compile this file. 
     5. Now run Kitchen by typing `java Kitchen`. Notice that each file
        defines a class with the same name as the file. Remember how Java is
        a completely object-oriented langauge? This means you can't just type 
        commands for Java to execute. Instead, when you start a Java program, 
        it looks for a method called `main` and runs it. (PS: Main receives
        a String[] object called args. This means main gets a list (array) of
        strings, which are whatever you type in after `java Kitchen`. For 
        example, if you typed in `java Kitchen bake cake`, main would receive
        ['bake', 'cake'] and could then do whatever it needed to do. 
     6. See if you can change TeaKettle's behavior. When you break something, 
        read the error messages!
      
2. Next session we are going to plan our individual projects. Come to the 
   session with a plan: 
     1. What's your idea? What will it do? Do you want to work with someone
        else, or do you want to work on your own? Do you want to work in 
        Python or Java? (If you work in Java, you'll definitely need to choose
        a simpler project!)
     2. What classes will you need? What will each do? This donsn't have to be 
        a final plan, but do your best to think it through.
     3. What help will you need? Is there part of your project you don't know how
        to do?
