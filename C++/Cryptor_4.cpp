#include <conio.h>                                                                                                                                                                                                                                              #include <conio.h>
#include <stdio.h>
#include <ctype.h>
#include <cstdlib>
#include <locale.h>
#include <iostream>
#include <windows.h>

using namespace std;

enum ConsoleColor
{
    Black = 0,
    Blue = 1,
    Green = 2,
    Cyan = 3,
    Red = 4,
    Magenta = 5,
    Brown = 6,
    LightGrey = 7,
    DarkGrey = 8,
    LightBlue = 9,
    LightGreen = 10,
    LightCyan = 11,
    LightRed = 12,
    LightMagenta = 13,
    Yellow = 14,
    White = 15
};

void setColor(ConsoleColor text, ConsoleColor background)
{
    HANDLE hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hStdOut, (WORD)((background << 4) | text));
}
 
 int main() {
 	
 system("color 1F"); 	
 
 char a;
 char *fileName="C:\\Users\\User\\Documents\\input.txt";
 FILE *f=fopen(fileName, "r");
 char *fileOut="C:\\Users\\User\\Documents\\output.txt";
 FILE *fo=fopen(fileOut, "w");
 int  *key, ans, k;
 setlocale(LC_ALL,"Russian"); 
 cout <<"\n";
 setColor(White, Blue);
 cout << " Please enter [1] - for encryption, [0] - for decryption ->\n";
 cout <<"\n";
 cout <<" Enter the number of your choice: ";
 while (!(cin >> ans) || (cin.peek() != '\n') || (ans != 1 && ans != 0)) {
        cin.clear();
        while (cin.get() != '\n');
		cout <<"\n";
		setColor(Yellow, Blue);
		cout <<" Incorrect entry, try entering the number of your choice again!\n";
		cout <<"\n";
		setColor(White, Blue);
		cout <<" Enter the number of your choice: "; }
 
 
  //Cryptor
  if (ans==1) {
  while((k=fgetc(f))!=EOF) {a=k;
  if (((int)a>-65)&&((int)a<0)) {
  if (a==(char)-33) a=(char)-64; else {
  if (a==(char)-1) a=(char)-32; else a+=1; } } 
  else a=a ;
  fprintf(fo, "%c",a); }
  cout <<"\n";
  setColor(LightGreen, Blue);
  cout<<" Encryption process completed! \n";
  cout <<"\n";
  setColor(White, Blue);
  cout<<" Press - [Enter] to exit the program . . . "; } 
  
  //Decryptor
  else if (ans==0) {
  while((k=fgetc(f))!=EOF) {a=k;
  if (((int)a>-65)&&((int)a<0)) {
  if (a==(char)-64) a=(char)-33; else {
  if (a==(char)-32) a=(char)-1; else a-=1; } } 
  else a=a ;
  fprintf(fo, "%c",a); }
  cout <<"\n";
  setColor(LightMagenta, Blue);
  cout<<" Decryption process completed! \n";
  cout <<"\n";
  setColor(White, Blue);
  cout<<" Press - [Enter] to exit the program . . . "; } 
  else {
  setColor(LightRed, Blue);
  printf("\n Error! "); }
  
 fclose(f);
 fclose(fo);
 getch(); }
