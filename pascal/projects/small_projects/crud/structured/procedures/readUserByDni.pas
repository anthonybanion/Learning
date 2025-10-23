{*
  
  This unit provides a procedure to read user 
  details from the database by their DNI.
  
  File: readUserByDni.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit readUserByDni;

{$mode objfpc}{$H+}

interface
Procedure readByDni();

implementation

uses
  serviceToReadUserByDni;

Procedure readByDni();
{*
  Reads user details from the database by their DNI.

  @param dni The DNI of the user to read.
  @return A string with the user details or a "not found" message.
*}

var
  dni: String;
begin
  WriteLn('Enter the DNI of the user to read: ');
  ReadLn(dni);
  if dni = '' then
  begin
    WriteLn('DNI cannot be empty.');
    Exit;
  end;
  WriteLn(serviceToReadUserByDni.readingServiceByDni(dni));
end;

end.