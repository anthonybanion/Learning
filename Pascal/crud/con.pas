program SQLiteExample;

uses
  SysUtils, sqlite3, SQLdb, DB;

var
  SQLiteDatabase: TSQLConnector;
  SQLiteTransaction: TSQLTransaction;
  Query: TSQLQuery;

begin
  try
    // Crear un objeto para la base de datos SQLite
    SQLiteDatabase := TSQLConnector.Create(nil);
    SQLiteTransaction := TSQLTransaction.Create(nil);

    // Configurar la conexión
    SQLiteDatabase.ConnectorType := 'sqlite';
    SQLiteDatabase.DatabaseName := 'my_database.db';  // Nombre de la base de datos
    SQLiteDatabase.Transaction := SQLiteTransaction;

    // Establecer la conexión
    SQLiteDatabase.Open;

    // Crear una tabla
    Query := TSQLQuery.Create(nil);
    Query.SQL.Text := 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)';
    Query.DataBase := SQLiteDatabase;
    Query.ExecSQL;

    // Insertar datos
    Query.SQL.Text := 'INSERT INTO users (name, age) VALUES (:name, :age)';
    Query.ParamByName('name').AsString := 'Alice';
    Query.ParamByName('age').AsInteger := 30;
    Query.ExecSQL;

    // Realizar una consulta
    Query.SQL.Text := 'SELECT * FROM users';
    Query.Open;

    // Mostrar los resultados
    while not Query.EOF do
    begin
      Writeln('ID: ', Query.FieldByName('id').AsInteger);
      Writeln('Name: ', Query.FieldByName('name').AsString);
      Writeln('Age: ', Query.FieldByName('age').AsInteger);
      Query.Next;
    end;

    // Cerrar la conexión
    Query.Close;
    SQLiteDatabase.Close;
  finally
    // Limpiar recursos
    Query.Free;
    SQLiteTransaction.Free;
    SQLiteDatabase.Free;
  end;
end.
