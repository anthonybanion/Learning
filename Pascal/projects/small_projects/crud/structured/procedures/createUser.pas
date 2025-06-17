unit createUser;

{$mode objfpc}{$H+}

interface
procedure createUser;

implementation

uses
  serviceToCreateUser, global;

procedure createUser;
{ This procedure creates a new user in the database.
  It returns a message indicating the success or failure of the operation. }

begin
    Write('Enter first name: ');
    ReadLn(global.firstName);
    Write('Enter last name: ');
    ReadLn(global.lastName);
    Write('Enter DNI: ');
    ReadLn(global.dni);
    WriteLn(serviceToCreateUser.create(global.firstName, global.lastName, global.dni));
    global.firstName := '';
    global.lastName := '';
    global.dni := '';
end;
end.