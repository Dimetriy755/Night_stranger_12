#include <windows.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <locale.h>
#include <conio.h>
#include <cstdlib>
#include <math.h>
#include <cmath>

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

double a, b, c, x, y;
char root = 251;
string j = " ]";
float n, r, z;
string CLS;
long s, t;
short p;
char d;
char k;

int main() {
	
	system("color 1F");

    while (p != 5) {
        
		cout <<"\n";
		setColor(White, Blue);
        cout <<" ====================== MENU ======================\n";
        cout <<"\n";
        cout <<" 1 - Calculating the square root of a number: [ "<< root << j <<endl;
        cout <<" 2 - Calculating the cube root of a number:  [ 3"<< root << j <<endl;
        cout <<" 3 - All operations for calculation:[+, -, *, ^, /]\n";
        cout <<" 4 - One operation to calculate modulo division:[%]\n";
        cout <<" 5 - Exit\n";
        cout <<"\n";
        setColor(Yellow, Blue);
        cout <<" Instructions on what not to do:\n";
        cout <<"\n";
        cout <<" nan - it means Not-a-Number under math. exceptions\n";
        cout <<" square root of a negative number ->\n";
        cout <<" -> for example from -1 would be nan\n";
        cout <<" -> or -1 ^ 0.5 = nan\n";
        cout <<"\n";
        cout <<" inf - inability to calculate\n";
        cout <<" calculation of the result is more 1e+308(10 ^ 308)\n";
        cout <<" -> gives inf, inf this is infinity ->\n";
        cout <<" -> or 1 / 0 = inf\n";
        setColor(White, Blue);
        cout <<" ==================================================";
		
        cout <<"\n";
		cout <<" Enter the number of your choice: ";
			
		while (!(cin >> p) || (cin.peek() != '\n') || (p != 1 && p != 2 && p != 3 && p != 4 && p != 5)) {
        cin.clear();
        while (cin.get() != '\n');
		cout <<"\n";
		setColor(Yellow, Blue);
		cout <<" Incorrect entry, try entering the number of your choice again.\n";
		cout <<"\n";
		setColor(White, Blue);
		cout <<" Enter the number of your choice: "; }
		
        switch (p) {
        	
        case 1: {
        	
	        cout <<"\n";
	        cout <<" Enter a number to calculate its square root: ";
	        
	        while (!(cin >> z) || (cin.peek() != '\n')) {
	        cin.clear();
	        while (cin.get() != '\n');
	        cout <<"\n";
	        setColor(Yellow, Blue);
	        cout <<" Wrong entry, try entering the number for square root again.\n";
	        cout <<" You can not enter non-numeric symbols and negative numbers.\n";
	        cout <<"\n";
	        setColor(White, Blue);
			cout <<" Enter a number to calculate its square root: "; }
	        	
	        n = sqrt(z);
	                            
	        cout <<"\n";
	        cout <<" The square root of "<< z;
	        cout <<" is "<< n <<endl;
	        cout <<" --------------------------------------------------\n";
	        
	        cout <<" Please enter 'CLS' to clear the screen: ";
	        cin >> CLS;
			if (CLS == "cls") { system("cls"); }
	        else if (CLS != "cls") { system("cls"); } }
	        break;
	        
	    case 2: {
        	
	        cout <<"\n";
	        cout <<" Enter a number to calculate its cube root: ";
	        
	        while (!(cin >> x) || (cin.peek() != '\n')) {
	        cin.clear();
	        while (cin.get() != '\n');
	        cout <<"\n";
	        setColor(Yellow, Blue);
	        cout <<" Wrong entry, try entering the number for cube root again.\n";
	        cout <<"\n";
	        setColor(White, Blue);
			cout <<" Enter a number to calculate its cube root: "; }
	        	
	        y = copysign(exp(log(fabs(x)) / 3.0), x);
	                            
	        cout <<"\n";
	        cout <<" The cube root of "<< x;
	        cout <<" is "<< y;
	        cout <<"\n --------------------------------------------------\n";
	        
	        cout <<" Please enter 'CLS' to clear the screen: ";
	        cin >> CLS;
			if (CLS == "cls") { system("cls"); }
	        else if (CLS != "cls") { system("cls"); } }
	        break;
        	
        case 3: {
        	
            cout <<"\n";
		    cout <<" Enter first number: ";
		    
            while (!(cin >> a) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            setColor(Yellow, Blue);
            cout <<" Incorrect entry, try entering the first number again."<< endl;
            cout <<"\n";
            setColor(White, Blue);
		    cout <<" Enter first number: "; }
		    
            cout <<"\n";
			cout << " Enter operation: ";
            
            while (true) {
			if (!(cin >> d) || (cin.peek() != '\n') || (d != '+' && d != '-' && d != '*' && d != '^' && d != '/')) {
			cin.clear(); 
			while (cin.get() != '\n');
			cout <<"\n";
			setColor(Yellow, Blue);
			cout <<" Operation not recognized, enter operation again."<< endl;
			cout <<"\n";
			setColor(White, Blue);
			cout <<" Enter operation: "; }
			else { break; } }
            
            cout <<"\n";
			cout <<" Enter second number: ";
			
            while (!(cin >> b) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            setColor(Yellow, Blue);
            cout <<" Incorrect entry, try entering the second number again."<< endl;
            cout <<"\n";
            setColor(White, Blue);
		    cout <<" Enter second number: "; }
		    
            if (d == '+')
                c = a + b;
            else if (d == '-')
                c = a - b;
            else if (d == '*')
                c = a * b;
            else if (d == '/')
                c = a / b;
			else if (d == '^')
                c = pow(a, b); 
                
	        cout <<"\n";
			cout <<" Result is -> "<< c <<endl;
			cout <<" --------------------------------------------------\n";
			
			cout <<" Please enter 'CLS' to clear the screen: ";
			cin >> CLS;
			if (CLS == "cls") { system("cls"); }
	        else if (CLS != "cls") { system("cls"); } }
	        break;
	        
	    case 4: {
        	
            cout <<"\n";
		    cout <<" Enter first number: ";
		    
            while (!(cin >> s) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            setColor(Yellow, Blue);
            cout <<" Incorrect entry, try entering the first number again."<< endl;
            cout <<"\n";
            setColor(White, Blue);
		    cout <<" Enter first number: "; }
		    
            cout <<"\n";
			cout << " Enter operation: ";
            
            while (true) {
			if (!(cin >> k) || (cin.peek() != '\n') || (k != '%')) {
			cin.clear(); 
			while (cin.get() != '\n');
			cout <<"\n";
			setColor(Yellow, Blue);
			cout <<" Operation not recognized, enter operation again."<< endl;
			cout <<"\n";
			setColor(White, Blue);
			cout <<" Enter operation: "; }
			else { break; } }
            
            cout <<"\n";
			cout <<" Enter second number: ";
			
            while (!(cin >> t) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            setColor(Yellow, Blue);
            cout <<" Incorrect entry, try entering the second number again."<< endl;
            cout <<"\n";
            setColor(White, Blue);
		    cout <<" Enter second number: "; }
		    
            if (k == '%')
                r = s % t;
                
	        cout <<"\n";
			cout <<" Result is -> "<< r <<endl;
			cout <<" --------------------------------------------------\n";
			
			cout <<" Please enter 'CLS' to clear the screen: ";
			cin >> CLS;
			if (CLS == "cls") { system("cls"); }
	        else if (CLS != "cls") { system("cls"); } }
	        break;
        
        case 5: { break; } }
    }
}
