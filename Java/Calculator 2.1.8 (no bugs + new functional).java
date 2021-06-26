package com.company;
import java.lang.String;
import java.lang.Runtime;
import java.util.Scanner;
import java.io.IOException;

public class Main {

    public static void clrscr() {
        //Clears Screen in java
        try {
            if (System.getProperty("os.name").contains("Windows"))
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            else
                Runtime.getRuntime().exec("clear");
        } catch (IOException | InterruptedException ex) {}
    }

    //ANSI escape codes for color coding text
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";

    public static void main(String[] args) throws IOException {

        Scanner num = new Scanner(System.in);
        double X, Y, Z, N, result;
        char operation;
        String cls;
        int P;
        P = 0;

        while (P != 5) {

            System.out.println("");
            System.out.println(" ---------------------- MENU ----------------------");
            System.out.println("");
            System.out.println("");
            System.out.println(" 1 - Calculating the square root of a number:   [√]");
            System.out.println(" 2 - Calculating the cube root of a number:    [3√]");
            System.out.println(" 3 - Operations for calculation: [+, -, *, ^, /, %]");
            System.out.println(" 4 - You can see instructions on what not to do:[?]\n 5 - Exit");
            System.out.println(ANSI_YELLOW + " NaN - it means Not-a-Number under math. exceptions" + ANSI_RESET);
            System.out.println(ANSI_YELLOW + " Calculation of the result is more 1E308 - Infinity" + ANSI_RESET);
            System.out.println(" --------------------------------------------------");

            do {
                System.out.println("");
                System.out.print(" Enter the number of your choice: ");
                if (num.hasNextInt()) {
                    P = num.nextInt();
                    num.nextLine();
                    break; }
                else {
                    System.out.println("");
                    System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the number of your choice again." + ANSI_RESET);
                    System.out.println(ANSI_YELLOW + " You cannot enter characters/numbers outside of the menu above." + ANSI_RESET);
                    num.nextLine();
                    continue; }
            } while (1==1);

            switch (P) {

                case 1: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter a number to calculate its square root: ");
                        if (num.hasNextDouble()) {
                            Z = num.nextDouble();
                            num.nextLine();
                            N = Math.sqrt(Z);
                            System.out.println("");
                            System.out.println(" The square root of " + Z + " is " + N);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); }
                            else if (cls != "CLS") { clrscr(); }
                            break; }
                        else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Wrong entry, try entering the number for square root again." + ANSI_RESET);
                            System.out.println(ANSI_YELLOW + " You can not enter non-numeric symbols and negative numbers!" + ANSI_RESET);
                            num.nextLine();
                            continue; }
                    } while (1==1);
                } continue;

                case 2: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter a number to calculate its cube root: ");
                        if (num.hasNextDouble()) {
                            Z = num.nextDouble();
                            num.nextLine();
                            N = Math.cbrt(Z);
                            System.out.println("");
                            System.out.println(" The cube root of " + Z + " is " + N);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); }
                            else if (cls != "CLS") { clrscr(); }
                            break; }
                        else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Wrong entry, try entering the number for cube root again." + ANSI_RESET);
                            num.nextLine();
                            continue; }
                    } while (1==1);
                } continue;

                case 3: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter first number: ");
                        if (num.hasNextDouble()) {
                            X = num.nextDouble();
                            num.nextLine();
                            break; }
                        else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the first number again." + ANSI_RESET);
                            num.nextLine();
                            continue; }
                    } while (1==1);

                    System.out.println("");
                    System.out.print(" Enter operation: ");
                    operation = num.next().charAt(0);
                    num.nextLine();

                    do {
                        System.out.println("");
                        System.out.print(" Enter second number: ");
                        if (num.hasNextDouble()) {
                            Y = num.nextDouble();
                            num.nextLine();
                            break; }
                        else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the second number again." + ANSI_RESET);
                            num.nextLine();
                            continue;}
                    } while (1==1);

                    if (operation == '+') {
                        result = X + Y;
                        System.out.println("");
                        System.out.println(" Operation - [+] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = num.next();
                        num.nextLine();
                        if (cls == "CLS") { clrscr(); break; }
                        else if (cls != "CLS") { clrscr(); break; }
                    } else if (operation == '-') {
                        result = X - Y;
                        System.out.println("");
                        System.out.println(" Operation - [-] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = num.next();
                        num.nextLine();
                        if (cls == "CLS") { clrscr(); break; }
                        else if (cls != "CLS") { clrscr(); break; }
                    } else if (operation == '*') {
                        result = X * Y;
                        System.out.println("");
                        System.out.println(" Operation - [*] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = num.next();
                        num.nextLine();
                        if (cls == "CLS") { clrscr(); break; }
                        else if (cls != "CLS") { clrscr(); break; }
                    } else if (operation == '/') {
                        if (Y != 0) {
                            result = X / Y;
                            System.out.println("");
                            System.out.println(" Operation - [/] Result is - " + result);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); break; }
                            else if (cls != "CLS") { clrscr(); break; }
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_RED + " Division by zero is impossible! " + ANSI_RESET);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); break; }
                            else if (cls != "CLS") { clrscr(); break; }
                        }
                    } else if (operation == '%') {
                        if (Y != 0) {
                            result = X % Y;
                            System.out.println("");
                            System.out.println(" Operation - [%] Result is - " + result);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); break; }
                            else if (cls != "CLS") { clrscr(); break; }
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_RED + " Division by zero is impossible! " + ANSI_RESET);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = num.next();
                            num.nextLine();
                            if (cls == "CLS") { clrscr(); break; }
                            else if (cls != "CLS") { clrscr(); break; }
                        }
                    } else if (operation == '^') {
                        result = Math.pow(X, Y);
                        System.out.println("");
                        System.out.println(" Operation - [^] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = num.next();
                        num.nextLine();
                        if (cls == "CLS") { clrscr(); break; }
                        else if (cls != "CLS") { clrscr(); break; }
                    } else
                        System.out.print(ANSI_YELLOW + " \n Operation not recognized, repeat all over again!"
                                + " \n You cannot enter characters outside of the menu." + ANSI_RESET
                                + " \n --------------------------------------------------"
                                + " \n Please enter 'CLS' to clear the screen: ");
                        cls = num.next();
                        num.nextLine();
                        if (cls == "CLS") { clrscr(); break; }
                        else if (cls != "CLS") { clrscr(); break; }}

                case 4: {

                    System.out.println("");
                    System.out.println(ANSI_YELLOW + " Instructions on what not to do:" + ANSI_RESET);
                    System.out.println(ANSI_YELLOW
                            + " \n NaN - it means Not-a-Number under math. exceptions"
                            + " \n Square root of a negative number for example    ->"
                            + " \n from -1 would be NaN or -1 ^ 0.5 = NaN.       End." + ANSI_RESET);
                    System.out.println(ANSI_YELLOW
                            + " \n Infinity - inability to calculate, for example  ->"
                            + " \n calculation of the result is more 1.0E308(10^308)"
                            + " \n -> always produces in the result - Infinity.  End." + ANSI_RESET);
                    System.out.print(ANSI_YELLOW
                            + " \n At user input, all characters/numbers after a   ->"
                            + " \n whitespace after the first characters/numbers   ->"
                            + " \n will be ignored by this program and removed     ->"
                            + " \n from the data stream. Please keep this in mind  ->"
                            + " \n when entering data, only the first character    ->"
                            + " \n up to the first space is taken into account.  End." + ANSI_RESET
                            + " \n --------------------------------------------------"
                            + " \n Please enter 'CLS' to clear the screen: ");
                    cls = num.next();
                    num.nextLine();
                    if (cls == "CLS") { clrscr(); break; }
                    else if (cls != "CLS") { clrscr(); break; } }

                case 5: {

                    System.out.println("");
                    System.out.println(" Program ended. Exit.");
                    System.out.println(" --------------------------------------------------");
                    break; } }

            if (P > 5) {
                System.out.println("");
                System.out.println(ANSI_YELLOW + " Wrong way, try entering the number again after looking at the instructions." + ANSI_RESET);
                System.out.println(ANSI_YELLOW + " Look in the menu above this message which of the numbers you need to enter." + ANSI_RESET);
                System.out.println(" ---------------------------------------------------------------------------");
                System.out.print(" Please enter 'CLS' to clear the screen: ");
                cls = num.next();
                num.nextLine();
                if (cls == "CLS") { clrscr(); }
                else if (cls != "CLS") { clrscr(); } }
            else if (P < 1) {
                System.out.println("");
                System.out.println(ANSI_YELLOW + " Wrong way, try entering the number again after looking at the instructions." + ANSI_RESET);
                System.out.println(ANSI_YELLOW + " Look in the menu above this message which of the numbers you need to enter." + ANSI_RESET);
                System.out.println(" ---------------------------------------------------------------------------");
                System.out.print(" Please enter 'CLS' to clear the screen: ");
                cls = num.next();
                num.nextLine();
                if (cls == "CLS") { clrscr(); }
                else if (cls != "CLS") { clrscr(); } }
        }
    }
}