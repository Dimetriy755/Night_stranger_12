package com.company;
import java.lang.String;
import java.lang.Runtime;
import java.util.Scanner;
import java.io.IOException;
import java.io.PrintWriter;
import javax.script.ScriptEngine;
import java.util.InputMismatchException;
import javax.script.ScriptEngineManager;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;
import javax.script.ScriptException;

public class Main {

    public static void clrscr() {
        //Clears Screen in java
        try {
            if (System.getProperty("os.name").contains("Windows"))
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            else
                Runtime.getRuntime().exec("clear");
        } catch (IOException | InterruptedException ex) {
        }
    }

    //ANSI escape codes for color coding text
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";

    public static void main(String[] args) throws IOException, ScriptException, InterruptedException {

        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("js");
        PrintWriter printWriter = new PrintWriter(System.out,true);
        Scanner reader = new Scanner(System.in);
        reader.useDelimiter("\n"); // use line feed as the delimiter
        String line = "";
        String output = line.replace(" ", "");
        reader.useDelimiter(System.lineSeparator() + "| \n" );
        double X, Y, Z, N, result;
        String math_expression;
        Object result_1;
        char operation;
        operation = '\0';
        char root = 251;
        String cls;
        int P;
        P = 0;

        while (P != 6) {

            System.out.println("");
            System.out.println(" ---------------------- MENU ----------------------");
            System.out.println("");
            System.out.println("");
            printWriter.println(" 1 - Calculating the square root of a number:   ["+root+"]");
            printWriter.println(" 2 - Calculating the cube root of a number:    [3"+root+"]");
            System.out.println(" 3 - Operations for calculation: [+, -, *, ^, /, %]");
            System.out.println(" 4 - Calculate math. expressions of any complexity!");
            System.out.println(" 5 - You can see instructions on what not to do:[?]\n 6 - Exit");
            System.out.println(ANSI_YELLOW + " NaN - it means Not-a-Number under math. exceptions" + ANSI_RESET);
            System.out.println(ANSI_YELLOW + " Calculation of the result is more 1E308 - Infinity" + ANSI_RESET);
            System.out.println(" --------------------------------------------------");

            do {
                System.out.println("");
                System.out.print(" Enter the number of your choice: ");
                if (reader.hasNextInt() | output != line.replace(" ", "")) {
                    P = reader.nextInt();
                    reader.nextLine();
                    break;
                } else {
                    System.out.println("");
                    System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the number of your choice again." + ANSI_RESET);
                    System.out.println(ANSI_YELLOW + " You cannot enter characters/numbers outside of the menu above." + ANSI_RESET);
                    reader.nextLine();
                    continue;
                }
            } while (1 == 1);

            switch (P) {

                case 1: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter a number to calculate its square root: ");
                        if (reader.hasNextDouble()) {
                            Z = reader.nextDouble();
                            reader.nextLine();
                            N = Math.sqrt(Z);
                            System.out.println("");
                            System.out.println(" The square root of " + Z + " is " + N);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                            } else if (cls != "CLS") {
                                clrscr();
                            }
                            break;
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Wrong entry, try entering the number for square root again." + ANSI_RESET);
                            System.out.println(ANSI_YELLOW + " You can not enter non-numeric symbols and negative numbers!" + ANSI_RESET);
                            reader.nextLine();
                            continue;
                        }
                    } while (1 == 1);
                }
                continue;

                case 2: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter a number to calculate its cube root: ");
                        if (reader.hasNextDouble() | output != line.replace(" ", "")) {
                            Z = reader.nextDouble();
                            reader.nextLine();
                            N = Math.cbrt(Z);
                            System.out.println("");
                            System.out.println(" The cube root of " + Z + " is " + N);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                            } else if (cls != "CLS") {
                                clrscr();
                            }
                            break;
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Wrong entry, try entering the number for cube root again." + ANSI_RESET);
                            reader.nextLine();
                            continue;
                        }
                    } while (1 == 1);
                }
                continue;

                case 3: {

                    do {
                        System.out.println("");
                        System.out.print(" Enter first number: ");
                        if (reader.hasNextDouble() | output != line.replace(" ", "")) {
                            X = reader.nextDouble();
                            reader.nextLine();
                            break;
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the first number again." + ANSI_RESET);
                            reader.nextLine();
                            continue;
                        }
                    } while (1 == 1);

                    do {
                        try {
                            System.out.println("");
                            System.out.print(" Enter operation: ");
                            operation = reader.next(".").charAt(0);
                            reader.nextLine();
                            if (operation == '+' && operation == '-' && operation == '*' && operation == '^' && operation == '/' && operation == '%') {
                                break;
                            } else if (operation != '+' && operation != '-' && operation != '*' && operation != '^' && operation != '/' && operation != '%') {
                                System.out.println("");
                                System.out.println(ANSI_YELLOW + " Operation not recognized, enter operation again." + ANSI_RESET);
                                continue;
                            } else {
                                break;
                            } }
                        catch (StringIndexOutOfBoundsException | InputMismatchException exc) {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Operation not recognized, enter operation again." + ANSI_RESET);
                            reader.nextLine();
                            continue; }
                    } while (1==1);

                    do {
                        System.out.println("");
                        System.out.print(" Enter second number: ");
                        if (reader.hasNextDouble() | output != line.replace(" ", "")) {
                            Y = reader.nextDouble();
                            reader.nextLine();
                            break;
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " Incorrect entry, try entering the second number again." + ANSI_RESET);
                            reader.nextLine();
                            continue;
                        }
                    } while (1 == 1);

                    if (operation == '+') {
                        result = X + Y;
                        System.out.println("");
                        System.out.println(" Operation - [+] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = reader.next();
                        reader.nextLine();
                        if (cls == "CLS") {
                            clrscr();
                            break;
                        } else if (cls != "CLS") {
                            clrscr();
                            break;
                        }
                    } else if (operation == '-') {
                        result = X - Y;
                        System.out.println("");
                        System.out.println(" Operation - [-] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = reader.next();
                        reader.nextLine();
                        if (cls == "CLS") {
                            clrscr();
                            break;
                        } else if (cls != "CLS") {
                            clrscr();
                            break;
                        }
                    } else if (operation == '*') {
                        result = X * Y;
                        System.out.println("");
                        System.out.println(" Operation - [*] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = reader.next();
                        reader.nextLine();
                        if (cls == "CLS") {
                            clrscr();
                            break;
                        } else if (cls != "CLS") {
                            clrscr();
                            break;
                        }
                    } else if (operation == '/') {
                        if (Y != 0) {
                            result = X / Y;
                            System.out.println("");
                            System.out.println(" Operation - [/] Result is - " + result);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                                break;
                            } else if (cls != "CLS") {
                                clrscr();
                                break;
                            }
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_RED + " Division by zero is impossible! " + ANSI_RESET);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                                break;
                            } else if (cls != "CLS") {
                                clrscr();
                                break;
                            }
                        }
                    } else if (operation == '%') {
                        if (Y != 0) {
                            result = X % Y;
                            System.out.println("");
                            System.out.println(" Operation - [%] Result is - " + result);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                                break;
                            } else if (cls != "CLS") {
                                clrscr();
                                break;
                            }
                        } else {
                            System.out.println("");
                            System.out.println(ANSI_RED + " Division by zero is impossible! " + ANSI_RESET);
                            System.out.println(" --------------------------------------------------");
                            System.out.print(" Please enter 'CLS' to clear the screen: ");
                            cls = reader.next();
                            reader.nextLine();
                            if (cls == "CLS") {
                                clrscr();
                                break;
                            } else if (cls != "CLS") {
                                clrscr();
                                break;
                            }
                        }
                    } else if (operation == '^') {
                        result = Math.pow(X, Y);
                        System.out.println("");
                        System.out.println(" Operation - [^] Result is - " + result);
                        System.out.println(" --------------------------------------------------");
                        System.out.print(" Please enter 'CLS' to clear the screen: ");
                        cls = reader.next();
                        reader.nextLine();
                        if (cls == "CLS") {
                            clrscr();
                            break;
                        } else if (cls != "CLS") {
                            clrscr();
                            break;
                        }
                    } else
                        System.out.print(ANSI_YELLOW + " \n Operation not recognized, repeat all over again!"
                                + " \n You cannot enter characters outside of the menu." + ANSI_RESET
                                + " \n --------------------------------------------------"
                                + " \n Please enter 'CLS' to clear the screen: ");
                    cls = reader.next();
                    reader.nextLine();
                    if (cls == "CLS") {
                        clrscr();
                        break;
                    } else if (cls != "CLS") {
                        clrscr();
                        break;
                    }
                }
                continue;

                case 4: {
                    System.out.println("");
                    System.out.println(ANSI_GREEN + " A math expression is something like: 1+(35+5)-(7*8)/9 (without whitespaces)" + ANSI_RESET);
                    do {
                        try {
                            System.out.println("");
                            System.out.print(" Enter a math expression: ");
                            math_expression = reader.next();
                            reader.nextLine();
                            if (math_expression == (math_expression).replace(" ","")) {
                                math_expression = (math_expression).replace(" ", "");
                                result_1 = engine.eval(math_expression);
                                System.out.println("");
                                System.out.println(" Result is - " + result_1);
                                System.out.println(" --------------------------------------------------");
                                System.out.print(" Please enter 'CLS' to clear the screen: ");
                                cls = reader.next();
                                reader.nextLine();
                                if (cls == "CLS") {
                                    clrscr();
                                    break;
                                } else if (cls != "CLS") {
                                    clrscr();
                                    break;
                                }
                            } else {
                                System.out.println("");
                                System.out.println(ANSI_YELLOW + " You entered a string characters or whitespaces, but you need numeric!" + ANSI_RESET);
                                continue; } }
                        catch (ScriptException | NoSuchElementException exc) {
                            System.out.println("");
                            System.out.println(ANSI_YELLOW + " You entered a string characters or whitespaces, but you need numeric!" + ANSI_RESET);
                            continue; }
                    } while (1 == 1);
                }
                continue;

                case 5: {

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
                    System.out.print(" --------------------------------------------------"
                            + " \n Please enter 'CLS' to clear the screen: ");
                    cls = reader.next();
                    reader.nextLine();
                    if (cls == "CLS") {
                        clrscr();
                        break;
                    } else if (cls != "CLS") {
                        clrscr();
                        break;
                    }
                }
                continue;

                case 6: {
                    System.out.println("");
                    System.out.println(" Program ended. Exit.");
                    System.out.println(" --------------------------------------------------");
                    TimeUnit.SECONDS.sleep(4);
                    break;
                }
            }

            if (P > 6) {
                System.out.println("");
                System.out.println(ANSI_YELLOW + " Wrong way, try entering the number again after looking at the instructions." + ANSI_RESET);
                System.out.println(ANSI_YELLOW + " Look in the menu above this message which of the numbers you need to enter." + ANSI_RESET);
                System.out.println(" ---------------------------------------------------------------------------");
                System.out.print(" Please enter 'CLS' to clear the screen: ");
                cls = reader.next();
                reader.nextLine();
                if (cls == "CLS") {
                    clrscr();
                } else if (cls != "CLS") {
                    clrscr();
                }
            } else if (P < 1) {
                System.out.println("");
                System.out.println(ANSI_YELLOW + " Wrong way, try entering the number again after looking at the instructions." + ANSI_RESET);
                System.out.println(ANSI_YELLOW + " Look in the menu above this message which of the numbers you need to enter." + ANSI_RESET);
                System.out.println(" ---------------------------------------------------------------------------");
                System.out.print(" Please enter 'CLS' to clear the screen: ");
                cls = reader.next();
                reader.nextLine();
                if (cls == "CLS") {
                    clrscr();
                } else if (cls != "CLS") {
                    clrscr();
                }
            }
        }
    }
}