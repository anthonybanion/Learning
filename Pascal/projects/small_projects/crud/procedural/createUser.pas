unit createUser;

{$mode objfpc}{$H+}

interface 

procedure createUser;

implementation

uses 
    Classes, SysUtils, sqlite3conn, sqldb, db, databaseConnection; 

procedure createUser;
var
  Query: TSQLQuery;
  firstName, lastName, dni: string;

begin
  // Create the database connection
  Query := TSQLQuery.Create(nil);

  try
    Query.DataBase := SQLiteConn;
    Query.Transaction := SQLTransaction;

    // Get user input
    Write('Enter first name: ');
    ReadLn(firstName);
    Write('Enter last name: ');
    ReadLn(lastName);
    Write('Enter DNI: ');
    ReadLn(dni);

    // Prepare and execute the SQL query
    Query.SQL.Text := 'INSERT INTO users (firstName, lastName, dni) VALUES (:firstName, :lastName, :dni)';
    Query.ParamByName('firstName').AsString := firstName;
    Query.ParamByName('lastName').AsString := lastName;
    Query.ParamByName('dni').AsString := dni;
    Query.ExecSQL;
    SQLTransaction.Commit;
    WriteLn('User created successfully.');

  finally
    Query.Free;
  end;
end;
end.
