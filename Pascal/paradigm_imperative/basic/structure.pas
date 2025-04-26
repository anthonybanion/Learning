program structure;

{ ******************************* }
{         Constant Declarations         }
{ ******************************* }
const
  Pi = 3.14159;
  MaxElements = 10;
  WelcomeMessage = 'Welcome to the structured example program';

{ ******************************* }
{         Subrange Declarations         }
{ ******************************* }
type
  TSmallRange = 1..100; // Subrange: values from 1 to 100

{ ******************************* }
{         Type Declarations         }
{ ******************************* }
type
  TIntegerArray = array[1..MaxElements] of Integer;  // One-dimensional array
  TMatrix = array[1..3, 1..3] of Integer;             // 3x3 Matrix
  TCharSet = set of Char;                             // Set of characters
  PInteger = ^Integer;                                // Pointer to Integer

{ ******************************* }
{         Global Variable Declarations         }
{ ******************************* }
var
  i,j: Integer;
  numbers: TIntegerArray;
  matrix: TMatrix;
  letters: TCharSet;
  intPtr: PInteger;

{ ******************************* }
{         Function Declarations         }
{ ******************************* }
function Square(x: Integer): Integer;
begin
  Square := x * x;
end;

{ ******************************* }
{         Procedure Declarations         }
{ ******************************* }
procedure FillArray(var arr: TIntegerArray);
var
  j: Integer;
begin
  for j := 1 to MaxElements do
    arr[j] := j * 2;
end;

procedure PrintMatrix(mat: TMatrix);
var
  row, col: Integer;
begin
  for row := 1 to 3 do
  begin
    for col := 1 to 3 do
      Write(mat[row, col]:4);
    WriteLn;
  end;
end;

{ ******************************* }
{         Main Program Block         }
{ ******************************* }
begin
  WriteLn(WelcomeMessage);

  { Using array and function }
  FillArray(numbers);
  WriteLn('Array filled:');
  for i := 1 to MaxElements do
    Write(numbers[i], ' ');
  WriteLn;

  { Using pointer }
  New(intPtr);       // Allocate memory for the pointer
  intPtr^ := 42;     // Assign value to the pointer
  WriteLn('Value pointed by intPtr: ', intPtr^);
  Dispose(intPtr);   // Free memory

  { Using set }
  letters := ['A', 'B', 'C', 'D'];
  if 'A' in letters then
    WriteLn('Letter A is in the set');

  { Using matrix }
  for i := 1 to 3 do
    for j := 1 to 3 do
      matrix[i, j] := i * j;
  WriteLn('3x3 Matrix:');
  PrintMatrix(matrix);

end.

