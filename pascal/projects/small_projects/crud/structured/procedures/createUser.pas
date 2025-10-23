{*
  
  This unit contains the procedure to create 
  a new user in the database.
  
  File: createUser.pas
  Author: Anthony Bañon
  Created: 2025-06-30
  Last Updated: 2025-06-30
*}


unit createUser;

{$mode objfpc}{$H+}

interface
procedure create;

implementation

uses
  serviceToCreateUser, global;

procedure create;
{*
  Creates a new user in the database with the provided details.

  @param firstName The first name of the user.
  @param lastName The last name of the user.
  @param dni The DNI of the user.
  @return A message indicating the success or failure of the operation.
*}

begin
    Write('Enter first name: ');
    ReadLn(global.firstName);
    Write('Enter last name: ');
    ReadLn(global.lastName);
    Write('Enter DNI: ');
    ReadLn(global.dni);
    WriteLn(serviceToCreateUser.creationService(global.firstName, global.lastName, global.dni));
    global.firstName := '';
    global.lastName := '';
    global.dni := '';
end;
end.