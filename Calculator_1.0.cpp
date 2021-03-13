#include <windows.h>
#include <string.h>
#include <iostream>
#include <locale.h>
#include <conio.h>
#include <cstdlib>
#include <math.h>

using namespace std;

float a, b, c, z, n;
string CLS;
char d;
int p;

int main() {

    while (p != 3) {
        
		cout <<"\n";
        cout <<" ====================== MENU ======================\n";
        cout <<"\n";
        cout <<" 1 - Operation calculate the root of a number\n";
        cout <<" 2 - Operation calculate show:[+, -, *, ^, /]\n";
        cout <<" 3 - Exit\n";
        cout <<" ==================================================";
		
        cout <<"\n";
		cout <<" Enter the number of your choice: ";
			
		while (!(cin >> p) || (cin.peek() != '\n') || (p != 1 && p != 2 && p != 3)) {
        cin.clear();
        while (cin.get() != '\n');
		cout <<"\n";
		cout <<" Incorrect entry, try entering the number of your choice again.\n";
		cout <<"\n";
		cout <<" Enter the number of your choice: "; }
		
        switch (p) {
        	
        case 1: {
        	
	        cout <<"\n";
	        cout <<" Enter a number to calculate its square root: ";
	        
	        while (!(cin >> z) || (cin.peek() != '\n')) {
	        cin.clear();
	        while (cin.get() != '\n');
	        cout <<"\n";
	        cout <<" Wrong entry, try entering the number for square root again.\n";
	        cout <<" You can not enter non-numeric symbols and negative numbers.\n";
	        cout <<"\n";
			cout <<" Enter a number to calculate its square root: "; }
	        	
	        n = sqrt(z);
	                            
	        cout <<"\n";
	        cout <<" The square root of "<< z;
	        cout <<" is "<< n;
	        cout <<"\n --------------------------------------------------\n";
	        
	        cout <<" Please enter 'CLS' to clear the screen: ";
	        cin >> CLS;
			if (CLS == "cls") { system("cls"); }
	        else if (CLS != "cls") { system("cls"); } }
	        break;
        	
        case 2: {
        	
            cout <<"\n";
		    cout <<" Enter first number: ";
		    
            while (!(cin >> a) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            cout <<" Incorrect entry, try entering the first number again."<< endl;
            cout <<"\n";
		    cout <<" Enter first number: "; }
		    
            cout <<"\n";
			cout << " Enter operation: ";
            
            while (true) {
			if (!(cin >> d) || (cin.peek() != '\n') || (d != '+' && d != '-' && d != '*' && d != '^' && d != '/')) {
			cin.clear(); 
			while (cin.get() != '\n');
			cout <<"\n";
			cout <<" Operation not recognized, enter operation again."<< endl;
			cout <<"\n";
			cout <<" Enter operation: "; }
			else { break; } }
            
            cout <<"\n";
			cout <<" Enter second number: ";
			
            while (!(cin >> b) || (cin.peek() != '\n')) {
            cin.clear();
            while (cin.get() != '\n');
            cout <<"\n";
            cout <<" Incorrect entry, try entering the second number again."<< endl;
            cout <<"\n";
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
        
        case 3: { break; } }
    }
}
