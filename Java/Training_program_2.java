package com.company;
import java.util.Scanner;

// Расчет доли в процентном отношении.
// Тренировочная программа №2:

public class Main {

    public static void main(String[] args) {

        Scanner num = new Scanner(System.in); // - активирует текстовый интерфейс

        float Y, X, P; // - объявление переменной типа float и присваивание ей имён Y, X, P

        // Ввод исходных данных + инструкции присваивания переменной типа float значений Y, X
        System.out.println("");
        System.out.println(" Расчет доли в процентном отношении.");
        System.out.println(" -----------------------------------");
        System.out.println("");
        System.out.println(" Введите первое число - Y, которое в расчете будет идти за все 100%");
        System.out.println(" ------------------------------------------------------------------");
        System.out.print(" Y = ");
        Y = num.nextFloat();
        System.out.println(" -----------------------------------");
        System.out.println("");
        System.out.println(" Введите второе число - X для вычисления P%,\n P% - это какую долю X в % отношении составляет от первого числа - Y");
        System.out.println(" -------------------------------------------------------------------");
        System.out.print(" X = ");
        X = num.nextFloat();
        System.out.println(" -----------------------------------");

        // Формула расчета доли в процентном отношении (Расчет) и инструкция присваивания переменной float значения P
        P = X / Y  * 100;

        // Вывод результата
        System.out.println("");
        System.out.println(" P% = " + Math.round(P) + "%");
        System.out.println(" -----------------------------------");
        System.out.println("");
        System.out.println(" Доля числа X = " + X + " от полного числа Y = " + Y + " \n c учётом округления (мат.) будет составлять " + Math.round(P) + "%");
        System.out.println(" -------------------------------------------------------------------");
        System.out.println("");
    }
}