// See https://aka.ms/new-console-template for more information

using System;

class Calculator
{
    static void Main()
    {
        Console.WriteLine("=== CALCULADORA DE CONSOLA ===");
        Console.WriteLine("Elige una operación:");
        Console.WriteLine("1. Suma");
        Console.WriteLine("2. Resta");
        Console.WriteLine("3. Multiplicación");
        Console.WriteLine("4. División");
        Console.Write("Opción: ");
        
        int opcion = Convert.ToInt32(Console.ReadLine());

        Console.Write("Ingrese el primer número: ");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.Write("Ingrese el segundo número: ");
        double num2 = Convert.ToDouble(Console.ReadLine());

        double resultado = 0;
        bool operacionValida = true;

        switch (opcion)
        {
            case 1:
                resultado = num1 + num2;
                break;
            case 2:
                resultado = num1 - num2;
                break;
            case 3:
                resultado = num1 * num2;
                break;
            case 4:
                if (num2 != 0)
                    resultado = num1 / num2;
                else
                {
                    Console.WriteLine("Error: No se puede dividir por cero.");
                    operacionValida = false;
                }
                break;
            default:
                Console.WriteLine("Opción inválida.");
                operacionValida = false;
                break;
        }

        if (operacionValida)
        {
            Console.WriteLine($"Resultado: {resultado}");
        }

        Console.WriteLine("Presione cualquier tecla para salir...");
        Console.ReadKey();
    }
}
