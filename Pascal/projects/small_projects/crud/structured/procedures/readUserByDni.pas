unit readUserByDni;

{$mode objfpc}{$H+}

interface
Procedure readByDni();

implementation

uses
  serviceToReadUserByDni;

Procedure readByDni();

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