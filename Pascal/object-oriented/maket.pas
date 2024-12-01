Program maket;

{$Mode Objfpc}
type
  // Clase base Persona
  TPersona = class
  private
    FNombre: string;
    FEdad: Integer;
  public
    constructor Create(Nombre: string; Edad: Integer);
    procedure MostrarInformacion; virtual;
  end;

  // Clase derivada Cliente
  TCliente = class(TPersona)
  private
    FNumeroCliente: Integer;
  public
    constructor Create(Nombre: string; Edad: Integer; NumeroCliente: Integer);
    procedure MostrarInformacion; override;
  end;

  // Clase derivada Vendedor
  TVendedor = class(TPersona)
  private
    FNumeroEmpleado: Integer;
  public
    constructor Create(Nombre: string; Edad: Integer; NumeroEmpleado: Integer);
    procedure MostrarInformacion; override;
  end;

{ TPersona }

constructor TPersona.Create(Nombre: string; Edad: Integer);
begin
  FNombre := Nombre;
  FEdad := Edad;
end;

procedure TPersona.MostrarInformacion;
begin
  WriteLn('Nombre: ', FNombre);
  WriteLn('Edad: ', FEdad);
end;

{ TCliente }

constructor TCliente.Create(Nombre: string; Edad: Integer; NumeroCliente: Integer);
begin
  inherited Create(Nombre, Edad);
  FNumeroCliente := NumeroCliente;
end;

procedure TCliente.MostrarInformacion;
begin
  inherited MostrarInformacion;
  WriteLn('Numero de Cliente: ', FNumeroCliente);
end;

{ TVendedor }

constructor TVendedor.Create(Nombre: string; Edad: Integer; NumeroEmpleado: Integer);
begin
  inherited Create(Nombre, Edad);
  FNumeroEmpleado := NumeroEmpleado;
end;

procedure TVendedor.MostrarInformacion;
begin
  inherited MostrarInformacion;
  WriteLn('Numero de Empleado: ', FNumeroEmpleado);
end;

var
  Cliente: TCliente;
  Vendedor: TVendedor;

begin
  Cliente := TCliente.Create('Juan Perez', 30, 12345);
  Vendedor := TVendedor.Create('Ana Gomez', 28, 67890);

  WriteLn('Informacion del Cliente:');
  Cliente.MostrarInformacion;

  WriteLn;

  WriteLn('Informacion del Vendedor:');
  Vendedor.MostrarInformacion;

  Cliente.Free;
  Vendedor.Free;
end.